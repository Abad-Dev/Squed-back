from db import connect


def register_user(id, email):
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO USERS (ID, EMAIL) VALUES (%s, %s)", (id, email))
    conn.commit()
    conn.close


def get_id(email):
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM USERS WHERE EMAIL = %s", (email))
        res = cursor.fetchone()
    conn.close()
    if res:
        return res[0]
    else:
        return False


def register_note(id, user_id, name):
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO NOTES (CONTAINER_ID, USER_ID, NAME, CONTENT) VALUES (%s, %s, %s, %s)", (id, user_id, name, ''))
    conn.commit()
    conn.close()


def get_notes(user_id):
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("SELECT CONTAINER_ID, NAME FROM NOTES WHERE USER_ID = %s", (user_id))
        res = cursor.fetchall()
    conn.close()
    return res


def modify_note(note_id, new_value):
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE NOTES SET CONTENT = %s WHERE CONTAINER_ID = %s", (new_value, note_id))
    conn.commit()
    conn.close()
    
