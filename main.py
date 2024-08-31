from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h>This Landing Page </h>"

@app.route("/next")
def next_page():
    return "<h>This Second Page </h>"

if __name__ == '__main__':
    app.run(debug=True)


