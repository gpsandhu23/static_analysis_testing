import sqlite3
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/r1")
def vulnerable_sqli():
    id = request.args.get('id')
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM users WHERE id = {id}")
    result = cursor.fetchall()
    return str(result)


@app.route("/r2")
def secure_sqli():
    id = request.args.get('id')
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    result = cursor.fetchall()
    return str(result)


@app.route("/r3")
def vulnerable_cmd_injection():
    filename = request.args.get('filename')

    result = os.popen(f'cat {filename}').read()
    return str(result)


@app.route("/r4")
def secure_cmd_injection():
    filename = request.args.get('filename')

    with open(filename, 'r') as file:
        result = file.read()
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
