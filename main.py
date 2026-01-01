from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello! Go to <a href='/books'>/books</a>"


@app.route('/books', methods=["GET"])
def books():
    response = requests.get(
        "https://openlibrary.org/search.json?author=tolkien")
    response_data = response.json()
    book_data = response_data["docs"]
    print(book_data)
    return render_template('books.html', books=book_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
