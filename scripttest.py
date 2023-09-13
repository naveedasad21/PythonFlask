from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Web stie contents goes here"

if __name__ == "main":
    app.run(debug=True)