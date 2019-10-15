from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>hi<h1>"