from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'root' route"

@app.route("/")
def hello():
    return "Hello World!!! ;D"

@app.route("/goodbye/")
def goodbye():
    return "Farewell cruel world! :(("

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
