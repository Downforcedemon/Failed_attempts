# The aim of this script is to insert the content of a book into a database column 

# convert epub to binary
def read_file_as_binary(path):                     
    with open(path, 'rb') as file:                  
        return file.read()              

binary_content = read_file_as_binary('/home/kali/Downloads/Culture_Series/ConsiderPhlebas.epub')          


# insert data into database
import psycopg2

# Connect to your database. this database is in seperate from this machine. The database is located in 192.168.0.48 and the database name is 'Sci-fi/postgres@Sci-fi1' 
#  and the table name is 'Books' and the column name is 'bookcontent'  
conn = psycopg2.connect("dbname=Sci-fi user=postgres host=192.168.0.48 password=")          


# Create a cursor object
cur = conn.cursor()               

# Assuming 'binary_content' contains your ePub file read as binary
binary_content = read_file_as_binary('/home/kali/Downloads/Culture_Series/ThePlayerOfGames.epub')

# Prepare your INSERT statement
query = """                      
UPDATE Books
SET bookcontent = %s              
WHERE bookid = 9 and title = 'The Player of Games: A Culture Novel';
"""

# Execute the query
cur.execute(query, (psycopg2.Binary(binary_content),))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
