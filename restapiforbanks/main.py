from flask import Flask , jsonify
import sqlite3


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/banks')
def get_banks():
    conn = sqlite3.connect('bank_branches.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM myTable')
    banks = cur.fetchall()
    conn.close()
    return jsonify(banks)

@app.route('/branches/<int:bank_id>/')
def get_branches(bank_id):
    conn = sqlite3.connect('bank_branches.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM myTable WHERE bank_id= ?',(bank_id,))
    branches = cur.fetchall()
    conn.close()
    return jsonify(branches)


if __name__=="__main__":
    app.run(debug=True)