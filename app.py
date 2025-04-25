from flask import Flask, make_response, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return make_response(render_template("index.html"))

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True``)