import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS book1 (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, shelfno INTEGER);")
    conn.commit()
    conn.close()

def insert(title,author,year,shelfno):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("INSERT INTO book1 VALUES (NULL,?,?,?,?);",(title,author,year,shelfno))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM book1;")
    rows=curr.fetchall()
    conn.close()
    return rows
    
def search(title="",author="",year="",shelfno=""):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM book1 WHERE title=? OR author=? OR shelfno=? OR year=?;",(title,author,shelfno,year))
    rows=curr.fetchall()
    conn.close()
    return rows
    
def delete(id):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("DELETE FROM book1 WHERE id=?;",(id,))
    conn.commit()
    conn.close()
    
def update(id,title,author,year,shelfno):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("UPDATE book1 SET title=?,author=?,year=?,shelfno=? WHERE id=?;",(title,author,year,shelfno,id))
    conn.commit()
    conn.close()
    
connect()
