import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='company'
    )
    return connection


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Books
    cursor.execute("SELECT * FROM BOOK")
    books = cursor.fetchall()

    # Authors
    try:
        cursor.execute("SELECT * FROM AUTHOR")
        authors = cursor.fetchall()
    except:
        authors = []

    cursor.close()
    conn.close()

    return render_template(
        'library.html',
        books=books,
        authors=authors
    )


# ---- BOOK ROUTES ----

@app.route('/add_book')
def add_book():
    return "Add Book Page"


@app.route('/edit_book/<int:book_id>')
def edit_book(book_id):
    return f"Edit Book {book_id}"


@app.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    return f"Delete Book {book_id}"


# ---- AUTHOR ROUTES ----

@app.route('/add_author')
def add_author():
    return "Add Author Page"


@app.route('/edit_author/<int:author_id>')
def edit_author(author_id):
    return f"Edit Author {author_id}"


@app.route('/delete_author/<int:author_id>', methods=['POST'])
def delete_author(author_id):
    return f"Delete Author {author_id}"


# ---- TEMPLATE HELPERS ----

@app.context_processor
def utility_processor():
    return {
        'csrf_token': lambda: '',
        'image_url': lambda folder, item_id: None
    }


if __name__ == '__main__':
    app.run(debug=True)