import sqlite3

strSQLiteDBAddr="C:/Users/Soheil/PycharmProjects/Roxi-Lib/MyLibrary/MyBookLibrary.db"
#strSQLiteDBAddr="C:/Users/KianRayaneh/PycharmProjects/PythonProject1/MyLibrary/MyBookLibrary.db"

def create_table():
    conn = sqlite3.connect(strSQLiteDBAddr)
    cursor1 = conn.cursor()
    cursor1.execute("""CREATE TABLE IF NOT EXISTS 
MyBookLibrary1
        (id INTEGER PRIMARY KEY autoincrement,
        title TEXT,
        author TEXT,
        years INTEGER,
        isbn INTEGER)""")
    conn.commit()
    conn.close()
    print("Table created successfully")

def insert(title, author, years, isbn):
    conn = sqlite3.connect(strSQLiteDBAddr)
    cursor1 = conn.cursor()
    cursor1.execute("INSERT INTO MyBookLibrary1 (title,author,years,isbn) VALUES (?,?,?,?)", (title, author, years, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect(strSQLiteDBAddr)
    cursor1 = conn.cursor()
    cursor1.execute("SELECT * FROM MyBookLibrary1")
    rows = cursor1.fetchall()
    conn.close()
    return rows

def search(title=None, author=None, years=None, isbn=None):
    conn = sqlite3.connect(strSQLiteDBAddr)
    cursor1 = conn.cursor()
    cursor1.execute("SELECT title=? OR author=? OR years=? OR isbn=? FROM MyBookLibrary1", (title, author, years, isbn))
    rows = cursor1.fetchall()
    conn.close()
    return rows

def update(title=None, author=None, years=None, isbn=None, i=None):
    conn = sqlite3.connect(strSQLiteDBAddr)
    cursor1 = conn.cursor()
    cursor1.execute("UPDATE MyBookLibrary1 SET title=?, author=?, years=?, isbn=? WHERE id=?",(title, author, years, isbn, i,))
    conn.commit()
    conn.close()

def delete(i):
    conn = sqlite3.connect(strSQLiteDBAddr)
    cursor1 = conn.cursor()
    cursor1.execute("DELETE FROM MyBookLibrary1 WHERE id=?", (i,))
    conn.commit()
    conn.close()
