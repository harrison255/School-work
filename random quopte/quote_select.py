from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_random_quote():
    sq_connect = sqlite3.connect("quotes.db")
    quote_sel = sq_connect.cursor()
    quote_sel.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1;")
    quote = quote_sel.fetchone()
    sq_connect.close()
    return {"text": quote[0], "author": quote[1]}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quote")
def quote():
    return jsonify(get_random_quote())

if __name__ == "__main__":
    app.run(debug=True)