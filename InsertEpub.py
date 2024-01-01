#!/usr/bin/python
import psycopg2
from config import config

def read_blob(bookid, path_to_file):
    """ read BLOB data from a table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT bookcontent FROM books WHERE bookid = %s", (bookid,))
        blob = cur.fetchone()
        if blob is not None:
            open(path_to_file, 'wb').write(blob[0])
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

