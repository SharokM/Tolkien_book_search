from flask import Flask, Response, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello! Go to <a href='/books'>/books</a>"


@app.route('/books', methods=["GET"])
def books():
    response = requests.get(
        "https://openlibrary.org/search.json?q=crime+and+punishment&fields=key,title,author_name,editions"
    )
    response_data = response.json()
    book_data = response_data.get("docs", [])
    return render_template('books.html', books=book_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
