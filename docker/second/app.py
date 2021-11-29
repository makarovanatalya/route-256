from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)


class Comment(object):
    def __init__(self, author, record):
        self.author = author
        self.record = record


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        author = request.form["author"]
        comment = request.form["comment"]

        conn = psycopg2.connect(dbname='postgres', user='postgres',
                                password='postgres', host='db', port='5432')
        cursor = conn.cursor()

        cursor.execute('CREATE TABLE if not exists comments(author text,comment text)')
        conn.commit()

        cursor.execute(f"INSERT INTO comments(author,comment) VALUES('{author}', '{comment}')")
        conn.commit()

        conn.close()

        return redirect("/comments")

    return render_template("index.html")


@app.route("/comments", methods=["GET"])
def comments():
    conn = psycopg2.connect(dbname='postgres', user='postgres',
                            password='postgres', host='db', port='5432')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM comments')
    records = cursor.fetchall()
    conn.close()

    example = []

    for record in records:
        example.append(Comment(record[0], record[1]))

    return render_template("comments.html", comments=example)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
