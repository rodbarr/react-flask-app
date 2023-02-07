from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"fruits": ["apple", "banana", "grape"]}


if __name__ == "__main__":
    app.run(debug=True)
