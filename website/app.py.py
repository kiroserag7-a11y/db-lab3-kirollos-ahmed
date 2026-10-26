import os
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# ---------------- Database ---------------- #

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='library'
    )


# ---------------- Home ---------------- #

@app.route('/')
def index():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()

    cursor.execute("SELECT * FROM author")
    authors = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'library.html',
        books=books,
        authors=authors
    )


# ---------------- Add Book ---------------- #

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM author")
    authors = cursor.fetchall()

    if request.method == 'POST':

        title = request.form.get('title')
        price = request.form.get('price')
        author_id = request.form.get('author_id')

        try:

            cur = conn.cursor()

            cur.execute(
                """
                INSERT INTO book(title, price, author_id)
                VALUES (%s, %s, %s)
                """,
                (title, price, author_id)
            )

            conn.commit()

            cur.close()
            cursor.close()
            conn.close()

            return redirect(url_for('index'))

        except Exception as e:

            return render_template(
                'book_form.html',
                book=None,
                authors=authors,
                errors=[str(e)]
            )

    cursor.close()
    conn.close()

    return render_template(
        'book_form.html',
        book=None,
        authors=authors,
        errors=[]
    )


# ---------------- Edit Book ---------------- #

@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM author")
    authors = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM book WHERE book_id=%s",
        (book_id,)
    )

    book = cursor.fetchone()

    if request.method == 'POST':

        title = request.form.get('title')
        price = request.form.get('price')
        author_id = request.form.get('author_id')

        cur = conn.cursor()

        cur.execute(
            """
            UPDATE book
            SET title=%s,
                price=%s,
                author_id=%s
            WHERE book_id=%s
            """,
            (title, price, author_id, book_id)
        )

        conn.commit()

        cur.close()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    cursor.close()
    conn.close()

    return render_template(
        'book_form.html',
        book=book,
        authors=authors,
        errors=[]
    )


# ---------------- Delete Book ---------------- #

@app.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM book WHERE book_id=%s",
        (book_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('index'))


# ---------------- Add Author ---------------- #

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():

    if request.method == 'POST':

        name = request.form.get('name')
        country = request.form.get('country')

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO author(name, country)
            VALUES(%s, %s)
            """,
            (name, country)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    return render_template(
        'author_form.html',
        author=None,
        errors=[]
    )


# ---------------- Edit Author ---------------- #

@app.route('/edit_author/<int:author_id>', methods=['GET', 'POST'])
def edit_author(author_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM author WHERE author_id=%s",
        (author_id,)
    )

    author = cursor.fetchone()

    if request.method == 'POST':

        name = request.form.get('name')
        country = request.form.get('country')

        cur = conn.cursor()

        cur.execute(
            """
            UPDATE author
            SET name=%s,
                country=%s
            WHERE author_id=%s
            """,
            (name, country, author_id)
        )

        conn.commit()

        cur.close()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    cursor.close()
    conn.close()

    return render_template(
        'author_form.html',
        author=author,
        errors=[]
    )


# ---------------- Delete Author ---------------- #

@app.route('/delete_author/<int:author_id>', methods=['POST'])
def delete_author(author_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM author WHERE author_id=%s",
        (author_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('index'))


# ---------------- Bonus Images ---------------- #

@app.context_processor
def utility_processor():

    def image_url(folder, item_id):

        for ext in ['jpg', 'jpeg', 'png', 'webp']:

            path = os.path.join(
                app.static_folder,
                'images',
                folder,
                f'{item_id}.{ext}'
            )

            if os.path.exists(path):

                return url_for(
                    'static',
                    filename=f'images/{folder}/{item_id}.{ext}'
                )

        return None

    return {
        'csrf_token': lambda: '',
        'image_url': image_url
    }


# ---------------- Run ---------------- #

if __name__ == '__main__':
    app.run(debug=True)