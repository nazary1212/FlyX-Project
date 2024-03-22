#CREATING A TABLE AND DATABASE (DB) IN PYTHON FOR SQL
import sqlite3
connection = sqlite3.connect('testing.db')        #name/create a db file to use with sql 
cursor = connection.cursor()        #lets us send and recieve commands back and forth

cursor.execute( 
    """ CREATE TABLE data (
        iteration INTEGER,
        multiplier REAL
    )""")

connection.commit() #saves changes 2121
connection.close() #close the connection 
