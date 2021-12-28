import json
from flask import Flask, request

from config import DB_TABLE_WIDGETS_NAME
from db import init_db

app = Flask(__name__)

MYDB = init_db()


@app.route('/')
def hello_world():
    return 'Hello, Docker!'


@app.route('/widgets', methods=["GET"])
def get_widgets():
    cursor = MYDB.cursor()

    cursor.execute("SELECT * FROM widgets")

    row_headers = [x[0] for x in cursor.description]  # this will extract row headers

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))

    cursor.close()

    return json.dumps(json_data)


@app.route('/widgets', methods=["POST"])
def post_widget():
    cursor = MYDB.cursor()
    body = request.get_json()

    cursor.execute(f"INSERT INTO {DB_TABLE_WIDGETS_NAME} VALUES {tuple(body.values())}")
    MYDB.commit()
    cursor.close()
    return "widget created", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
