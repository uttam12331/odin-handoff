import sqlite3
from flask import Flask, jsonify, request
from datetime import date

app = Flask(__name__)
DB = 'books.db'

def isbn_ok(s):
    return isinstance(s, str) and len(s) == 13 and s.isdigit() and sum(int(c) * (3 if i % 2 else 1) for i, c in enumerate(s)) % 10 == 0

def check(d, conn, book_id=0):
    missing = [f for f in ['title', 'author', 'isbn', 'published_year', 'pages'] if not d.get(f)]
    if missing:
        return 'Missing fields: ' + ', '.join(missing), 400
    if not isbn_ok(d['isbn']):
        return 'Invalid ISBN-13', 400
    y, p = d['published_year'], d['pages']
    if type(y) is not int or type(p) is not int or not 1450 <= y <= date.today().year or p < 1:
        return 'Invalid year or pages', 400
    if conn.execute('SELECT 1 FROM books WHERE isbn = ? AND id != ?', (d['isbn'], book_id)).fetchone():
        return 'ISBN already exists', 409

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, isbn TEXT, published_year INTEGER, pages INTEGER)')
    c.execute('SELECT COUNT(*) FROM books')
    if c.fetchone()[0] == 0:
        c.executemany('INSERT INTO books (title, author, isbn, published_year, pages) VALUES (?, ?, ?, ?, ?)', [
            ("The Great Algorithm", "Valerie Vance", "9781491957660", 1843, 300),
            ("Pythonic Ways", "Silas Thorn", "9781593279509", 1991, 412),
            ("Databases Demystified", "Orion Blake", "9780132350884", 1970, 250),
            ("The Web Universe", "Lyra Sterling", "9780201633610", 1989, 180),
            ("Artificial Dreams", "Jaxen Cole", "9780321125217", 1950, 210),
            ("Cybernetic Society", "Thalia Cross", "9780596007126", 1948, 240),
            ("Bits and Bytes", "Zephyr Vance", "9780262033848", 1948, 150),
            ("The Design of Everyday Code", "Rowan Drake", "9781118008188", 1968, 600)
        ])
        conn.commit()
    conn.close()

init_db()

@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    books = [dict(row) for row in conn.execute('SELECT * FROM books').fetchall()]
    conn.close()
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    if not conn.execute('SELECT 1 FROM books WHERE id = ?', (id,)).fetchone():
        return jsonify({'error': 'Book not found'}), 404
    book = dict(conn.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone())
    conn.close()
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    d = request.json
    conn = sqlite3.connect(DB)
    if problem := check(d, conn):
        return jsonify({'error': problem[0]}), problem[1]
    c = conn.cursor()
    c.execute('INSERT INTO books (title, author, isbn, published_year, pages) VALUES (?, ?, ?, ?, ?)',
              (d['title'], d['author'], d['isbn'], d['published_year'], d['pages']))
    conn.commit()
    book_id = c.lastrowid
    conn.close()
    return jsonify({'id': book_id, **d}), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    d = request.json
    conn = sqlite3.connect(DB)
    if not conn.execute('SELECT 1 FROM books WHERE id = ?', (id,)).fetchone():
        return jsonify({'error': 'Book not found'}), 404
    if problem := check(d, conn, id):
        return jsonify({'error': problem[0]}), problem[1]
    conn.execute('UPDATE books SET title = ?, author = ?, isbn = ?, published_year = ?, pages = ? WHERE id = ?',
                 (d['title'], d['author'], d['isbn'], d['published_year'], d['pages'], id))
    conn.commit()
    conn.close()
    return jsonify({'id': id, **d})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = sqlite3.connect(DB)
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(port=5000)
