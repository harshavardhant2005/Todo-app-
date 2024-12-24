
import sqlite3
from flask import Flask,url_for,request,redirect,render_template,jsonify
import os
app = Flask(__name__)
app.config["DATABASE"] ="Todo.db"

def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(app.config['DATABASE']):
        with app.app_context():
            conn = get_db_connection()
            with open('schema.sql', 'r') as f:
                conn.executescript(f.read())
            conn.close()

@app.route("/")
def index():
    con = get_db_connection()
    data= con.execute('''select * from task''')
    rows = data.fetchall()
    return render_template("index.html",data = rows)


@app.route("/addTask",methods=["GET","POST"])
def addTask():
    if request.method =="POST":
        title = request.form["Title"]
        desc = request.form["Description"]
        conn = get_db_connection()
        conn.execute('''insert into task(title,description) values (?,?)''',(title,desc))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("addTask.html")

@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    conn = get_db_connection()
    conn.execute('''update task set done=1 where id=(?)''',(task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))
    
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    conn = get_db_connection()
    conn.execute('''delete from task where id= (?)''',(task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index')) 


if __name__ =="__main__":
    init_db()
    app.run(debug=True)