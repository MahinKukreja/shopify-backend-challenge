from flask import Flask, request, jsonify
from flask_cors import CORS
from helpers_funcs import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/books', methods=['GET'])
def read():
    return jsonify(get_books())


@app.route('/add_book', methods=['POST'])
def create():
    book = request.get_json()
    return jsonify(add_book(book))


@app.route('/edit_book', methods=['POST'])
def update():
    book = request.get_json()
    return jsonify(edit_book(book))


@app.route('/delete_book/<id>', methods=['DELETE'])
def delete(id):
    return jsonify(delete_book(id))


if __name__ == "__main__":
    checkDbExists()
    app.run(debug=True)
