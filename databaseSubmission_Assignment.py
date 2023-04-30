import sqlite3

conn = sqlite3.connect ('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_string TEXT \
        )")
    conn.commit #Create the table for the assignent
conn.close #close connection

conn = sqlite3.connect ('test.db') #ooen connection


#list of files
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
#iterate through the tuple and if the filename ends in .txt add it to
#the database.
for i in fileList:
    if i.endswith('.txt'):
        with conn:
            cur = conn.cursor() #grab cursor for command.
            cur.execute("INSERT INTO tbl_files (col_string) VALUES (?)", (i,))
            print(i)
conn.close()
