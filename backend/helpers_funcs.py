from sqlite3 import *
from os.path import isfile


DATABASE_NAME = "./books.db"


def checkDbExists():
    if not isfile(DATABASE_NAME):
        createNewDb()

    createNewDb()
    createTable()


def createNewDb():
    conn = None
    try:
        conn = connect(DATABASE_NAME)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def createTable():
    sql_create_book_table = """ CREATE TABLE IF NOT EXISTS Books (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            name text UNIQUE NOT NULL,
                                            author text NOT NULL,
                                            publisher text NOT NULL
                                        ); """

    conn = connect(DATABASE_NAME)

    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_create_book_table)
        except Error as e:
            print(e)
    else:
        print("Error! cannot create the database connection.")


def connect_to_db():
    connection = connect("./books.db")
    return connection


def add_book(book):
    connection = connect_to_db()
    problem = False
    try:
        db = connection.cursor()
        db.execute("SELECT * FROM Books")
        db.execute("INSERT INTO books (name, author, publisher) VALUES (?, ?, ?)",
                   (book['name'], book['author'], book['publisher'],))
        db.execute("SELECT id FROM Books WHERE name = ?", (book["name"],))
        last_id = db.fetchone()
        connection.commit()
    except Error as error:
        print(error)
        problem = True
    return {"message": f"{book['name']} has been added!", "id": last_id[0]} if not problem else "Unable to add"


def get_books():
    books = []
    try:
        connection = connect_to_db()
        connection.row_factory = Row
        db = connection.cursor()
        db.execute("SELECT * FROM Books")
        rows = [dict(row) for row in db.fetchall()]
        for i in rows:
            book = {}
            book["id"] = i["id"]
            book["name"] = i["name"]
            book["author"] = i["author"]
            book["publisher"] = i["publisher"]
            books.append(book)

    except:
        books = []

    return books


def edit_book(book):
    connection = connect_to_db()
    problem = False
    try:
        db = connection.cursor()
        db.execute("UPDATE books SET name = ?, author = ?, publisher = ? WHERE id = ?",
                   (book['name'], book['author'], book['publisher'], book["id"]))
        connection.commit()
    except Error as error:
        print(error)
        problem = True
    return f"Book Number {book['id']} has been edited!" if not problem else "Unable to edit"


def delete_book(id):
    problem = False
    try:
        connection = connect_to_db()
        connection.execute("DELETE from books WHERE id = ?", (id,))
        connection.commit()
    except Error as error:
        print(error)
        problem = True
    return f"Book Number {id} has been deleted!" if not problem else "Unable to delete"
