DROP FUNCTION IF EXISTS search_contacts(TEXT);
DROP FUNCTION IF EXISTS get_contacts_page(INT, INT, TEXT);
DROP PROCEDURE IF EXISTS add_phone(VARCHAR, VARCHAR, VARCHAR);
DROP PROCEDURE IF EXISTS move_to_group(VARCHAR, VARCHAR);

-- add_phone
CREATE OR REPLACE PROCEDURE add_phone(p_contact_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE cid INT;
BEGIN
    SELECT id INTO cid FROM contacts WHERE name = p_contact_name;
    IF cid IS NULL THEN RAISE EXCEPTION 'Contact not found'; END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;

-- move_to_group
CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE gid INT;
BEGIN
    INSERT INTO groups(name) VALUES (p_group_name) ON CONFLICT DO NOTHING;

    SELECT id INTO gid FROM groups WHERE name = p_group_name;

    UPDATE contacts SET group_id = gid WHERE name = p_contact_name;
END;
$$;

-- search
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id INT,
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phone VARCHAR,
    phone_type VARCHAR,
    date_added DATE
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.email, c.birthday,
           g.name, p.phone, p.type, c.date_added::DATE
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%'
       OR g.name ILIKE '%' || p_query || '%'
    ORDER BY c.name;
END;
$$ LANGUAGE plpgsql;

-- pagination
CREATE OR REPLACE FUNCTION get_contacts_page(p_limit INT, p_offset INT, p_sort TEXT)
RETURNS TABLE (
    id INT,
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phones TEXT,
    date_added DATE
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.email, c.birthday,
           g.name,
           COALESCE(string_agg(p.phone || ' (' || p.type || ')', ', '), ''),
           c.date_added::DATE
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    GROUP BY c.id, g.name
    ORDER BY c.name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;