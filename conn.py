import psycopg2
from time import sleep

def conn(dbname, user, password, port, encoding):
    connection = psycopg2.connect(
    f"dbname={dbname} user={user} password={password} client_encoding={encoding} port={port}"
    )

    cursor = connection.cursor()

    cursor.execute(str)
    dataset = cursor.fetchall()

    cursor.close()
    connection.close()