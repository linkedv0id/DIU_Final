
from flask import Flask, abort, request, render_template, redirect, make_response, send_from_directory
import sqlite3 as sql 
import json

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')