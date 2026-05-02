import psycopg2, csv, json
from connect import connect

def run_sql(file, cur, con):
    with open(file, encoding="utf-8") as f:
        cur.execute(f.read())
        con.commit()

def group_id(cur, name):
    cur.execute("INSERT INTO groups(name) VALUES (%s) ON CONFLICT DO NOTHING", (name,))
    cur.execute("SELECT id FROM groups WHERE name=%s", (name,))
    return cur.fetchone()[0]

def add_contact(cur, con):
    n = input("Name: ").strip()
    e = input("Email: ").strip()
    b = input("Birthday (YYYY-MM-DD): ").strip()
    g = input("Group: ").strip() or "Other"

    gid = group_id(cur, g)

    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s,%s,%s,%s)
        ON CONFLICT (name)
        DO UPDATE SET email=EXCLUDED.email, birthday=EXCLUDED.birthday
    """, (n, e, b, gid))
    con.commit()

    while True:
        p = input("Phone: ").strip()
        t = input("Type (mobile/work/home): ").strip()

        cur.execute("CALL add_phone(%s,%s,%s)", (n, p, t))
        con.commit()

        if input("More? (yes/no): ").lower() != "yes":
            break

def paginate(cur):
    limit, offset = 5, 0

    while True:
        cur.execute("SELECT * FROM get_contacts_page(%s,%s,%s)", (limit, offset, "name"))
        rows = cur.fetchall()

        if not rows:
            print("No more data")
            break

        for r in rows:
            print(r)

        cmd = input("next / prev / quit: ").lower()

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break

def import_csv(cur, con):
    with open("contacts.csv", encoding="utf-8") as f:
        reader = csv.reader(f)

        next(reader)  # пропускаем header

        for row in reader:
            if not row or len(row) < 6:
                continue

            name, email, bday, grp, phone, ptype = row

            # убираем лишние пробелы
            name = name.strip()
            email = email.strip()
            bday = bday.strip()
            grp = grp.strip()
            phone = phone.strip()
            ptype = ptype.strip()

            gid = group_id(cur, grp)

            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s,%s,%s,%s)
                ON CONFLICT (name) DO UPDATE SET email=EXCLUDED.email
                RETURNING id
            """, (name, email, bday, gid))

            cid = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s,%s,%s)
            """, (cid, phone, ptype))

    con.commit()
    print("CSV imported successfully")

def export_json(cur):
    cur.execute("SELECT id, name, email, birthday FROM contacts")

    data = []

    for cid, n, e, b in cur.fetchall():
        cur.execute("SELECT phone, type FROM phones WHERE contact_id=%s", (cid,))
        phones = [{"phone": p, "type": t} for p, t in cur.fetchall()]

        data.append({
            "name": n,
            "email": e,
            "birthday": str(b),
            "phones": phones
        })

    json.dump(data, open("export.json", "w"), indent=4)
    print("Exported to export.json")

def import_json(cur, con):
    data = json.load(open("contacts.json"))

    for item in data:
        gid = group_id(cur, item.get("group", "Other"))

        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES (%s,%s,%s,%s)
            ON CONFLICT (name)
            DO UPDATE SET email=EXCLUDED.email, birthday=EXCLUDED.birthday
            RETURNING id
        """, (item["name"], item.get("email"), item.get("birthday"), gid))

        cid = cur.fetchone()[0]

        cur.execute("DELETE FROM phones WHERE contact_id=%s", (cid,))

        for p in item.get("phones", []):
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s,%s,%s)
            """, (cid, p["phone"], p["type"]))

    con.commit()
    print("JSON imported successfully")

# --- MAIN ---

con = connect()
cur = con.cursor()

run_sql("schema.sql", cur, con)
run_sql("procedures.sql", cur, con)

while True:
    print("""
1: Add
2: Search
3: Pagination
4: Import CSV
5: Export JSON
6: Import JSON
0: Exit
""")

    choice = input("Choice: ")

    try:
        if choice == "1":
            add_contact(cur, con)

        elif choice == "2":
            q = input("Search: ")
            cur.execute("SELECT * FROM search_contacts(%s)", (q,))
            for r in cur.fetchall():
                print(r)

        elif choice == "3":
            paginate(cur)

        elif choice == "4":
            import_csv(cur, con)

        elif choice == "5":
            export_json(cur)

        elif choice == "6":
            import_json(cur, con)

        elif choice == "0":
            break

    except Exception as e:
        con.rollback()
        print("Error:", e)

cur.close()
con.close()