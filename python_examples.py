import sqlite3
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/r1")
def function_one():
    id = request.args.get('id')
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    result = cursor.fetchall()
    return str(result)


@app.route("/r2")
def function_two():
    id = request.args.get('id')
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    result = cursor.fetchall()
    return str(result)


@app.route("/r3")
def function_three():
    filename = request.args.get('filename')

    result = os.popen(['cat', filename]).read()
    return str(result)


@app.route("/r4")
def function_four():
    filename = request.args.get('filename')

    with open(filename, 'r') as file:
        result = file.read()
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
