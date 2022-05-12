from csv_xl_to_mysql import CSVXLToMySQL
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_to_mysql():
    host = request.form['host']
    database = request.form['database']
    table = request.form['table']
    username = request.form['username']
    password = request.form['password']
    file = request.form['file']

    db_load = CSVXLToMySQL(file, table, host, database, username, password)
    db_load.load_to_db()

    return render_template("index.html", log=db_load.log)


if __name__ == '__main__':
    app.run()
