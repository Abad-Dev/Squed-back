from db import connect

def register_user(id, email):
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO USERS (ID, EMAIL) VALUES (%s, %s)", (id, email))
    conn.commit()
    conn.close

def registered(email):
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM USERS WHERE EMAIL = %s", (email))
        res = cursor.fetchall()
    return bool(res)
