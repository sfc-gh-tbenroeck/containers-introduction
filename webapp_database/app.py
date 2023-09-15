# app.py
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="example",
        host="db"
    )

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/records', methods=['GET', 'POST'])
def manage_records():
    connection = connect_db()
    cursor = connection.cursor()

    if request.method == 'POST':
        new_record = request.get_json()
        cursor.execute(
            sql.SQL("INSERT INTO records (name, age) VALUES (%s, %s)"),
            [new_record['name'], new_record['age']]
        )
        connection.commit()
        return jsonify(status="success"), 201

    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    return jsonify(records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
