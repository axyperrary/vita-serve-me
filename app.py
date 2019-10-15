from flask import Flask, render_template, request, make_response
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello<h1>"

@app.route('/api', methods=['POST'])
def main():
    print (request.form['param'])
    response = make_response(json.dumps('Done!'))
    response.headers['Access-Control-Allow-Origin'] = '*'
    # sendMail(request.form['param'])
    return(response)

if __name__ == "__main__":
    app.run()