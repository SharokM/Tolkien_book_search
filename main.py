from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! Go to <a href='/books'>/books</a>"

@app.route('/books')
def books():
    books_data = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
        {"title": "1984", "author": "George Orwell", "year": 1949},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
    ]
    return render_template('books.html', books=books_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
