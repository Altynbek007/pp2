from connect import connect
import json

# ================= EXPORT =================
def export_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM public.contacts c
        LEFT JOIN public.groups g ON c.group_id = g.id
        LEFT JOIN public.phones p ON c.id = p.contact_id
    """)

    rows = cur.fetchall()

    data = []
    for r in rows:
        data.append({
            "name": r[0],
            "email": r[1],
            "birthday": str(r[2]),
            "group": r[3],
            "phone": r[4],
            "type": r[5]
        })

    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Export done")

    cur.close()
    conn.close()


# ================= IMPORT =================
def import_json():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for item in data:
        name = item["name"]

        cur.execute("SELECT id FROM public.contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists (skip/overwrite): ")

            if choice == "skip":
                continue
            elif choice == "overwrite":
                cur.execute("DELETE FROM public.contacts WHERE name=%s", (name,))

        cur.execute("""
            INSERT INTO public.contacts(name, email, birthday)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (name, item["email"], item["birthday"]))

        contact_id = cur.fetchone()[0]

        # group
        cur.execute("SELECT id FROM public.groups WHERE name=%s", (item["group"],))
        g = cur.fetchone()

        if not g:
            cur.execute("INSERT INTO public.groups(name) VALUES (%s) RETURNING id", (item["group"],))
            group_id = cur.fetchone()[0]
        else:
            group_id = g[0]

        cur.execute("UPDATE public.contacts SET group_id=%s WHERE id=%s", (group_id, contact_id))

        # phone
        cur.execute("""
            INSERT INTO public.phones(contact_id, phone, type)
            VALUES (%s, %s, %s)
        """, (contact_id, item["phone"], item["type"]))

    conn.commit()
    print("✅ Import done")

    cur.close()
    conn.close()


# ================= SEARCH =================
def search():
    conn = connect()
    cur = conn.cursor()

    q = input("Search: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


# ================= FILTER =================
def filter_group():
    conn = connect()
    cur = conn.cursor()

    g = input("Group: ")

    cur.execute("""
        SELECT c.name, g.name
        FROM public.contacts c
        JOIN public.groups g ON c.group_id = g.id
        WHERE LOWER(g.name) = LOWER(%s)
    """, (g,))

    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


# ================= SORT =================
def sort_contacts():
    conn = connect()
    cur = conn.cursor()

    print("1 - name")
    print("2 - birthday")
    choice = input()

    if choice == "1":
        cur.execute("SELECT name, birthday FROM public.contacts ORDER BY name")
    elif choice == "2":
        cur.execute("SELECT name, birthday FROM public.contacts ORDER BY birthday")
    else:
        print("❌ Введи 1 или 2")
        return

    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


# ================= PAGINATION (FIXED) =================
def paginate():
    conn = connect()
    cur = conn.cursor()

    limit = 3
    offset = 0

    cur.execute("SELECT COUNT(*) FROM public.contacts")
    total = cur.fetchone()[0]

    if total == 0:
        print("❌ Нет данных")
        return

    while True:
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
        rows = cur.fetchall()

        page = offset // limit + 1
        total_pages = (total + limit - 1) // limit

        print(f"\n--- PAGE {page}/{total_pages} ---")

        for r in rows:
            print(r)

        cmd = input("next / prev / quit: ").lower()

        if cmd == "next":
            if offset + limit >= total:
                print("❌ Это последняя страница")
            else:
                offset += limit

        elif cmd == "prev":
            if offset == 0:
                print("❌ Это первая страница")
            else:
                offset -= limit

        elif cmd == "quit":
            break

        else:
            print("❌ Неверная команда")

    cur.close()
    conn.close()


# ================= MENU =================
def menu():
    while True:
        print("""
1 Export JSON
2 Import JSON
3 Search
4 Filter by group
5 Sort
6 Pagination
0 Exit
        """)

        c = input()

        if c == "1":
            export_json()
        elif c == "2":
            import_json()
        elif c == "3":
            search()
        elif c == "4":
            filter_group()
        elif c == "5":
            sort_contacts()
        elif c == "6":
            paginate()
        elif c == "0":
            print("Bye 👋")
            break
        else:
            print("Invalid option")


menu()