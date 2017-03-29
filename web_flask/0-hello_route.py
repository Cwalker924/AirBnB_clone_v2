"""
This is module 0-hello_route.py

This module starts a web aplication via Flask
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
        return ("Hello HBNB!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
