import psycopg2
import os

# Replace with your actual database connection details
conn = psycopg2.connect("dbname=Sci-fi user=postgres host=192.168.0.48 password=")

try:
    with conn.cursor() as cur:
        cur.execute("SELECT bookcontent FROM Books WHERE bookid = 11")
        result = cur.fetchone()

        if result is not None:
            # Assuming the binary data is in the first column of the result
            with open("output.epub", "wb") as file:
                file.write(result[0])

            print("The file has been written to output.epub")
        else:
            print("No data found for bookid 11.")

except psycopg2.Error as e:
    print("An error occurred:", e)

finally:
    conn.close()
