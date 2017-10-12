from flask import Flask, g, request, render_template, redirect
import sqlite3
import time

app = Flask(__name__)
DATABASE = 'growls.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def db_read_growls():
    c = get_db().cursor()
    c.execute("SELECT * FROM growls")
    return c.fetchall()

def db_add_growl(name, growl):
    c = get_db().cursor()
    t = str(time.time())
    growl_info = (name, t, growl)
    c.execute("INSERT INTO growls VALUES (?, ?, ?)", growl_info)
    get_db().commit()


@app.route("/")
def hello():
    growls = db_read_growls()
    print(growls)
    # return app.send_static_file('index.html')
    return render_template('index.html', growls=growls)


@app.route("/api/growl", methods=["POST"])
def receive_growl():
    print(request.form)
    db_add_growl(request.form['name'], request.form['growl'])
    # return "Success!"
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
