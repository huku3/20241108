from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Flask!"


@app.route("/user/<name>")
def greet(name):
    return render_template("user.html", name=name)


@app.route("/fruits")
def fruits():
    fruits = ["りんご", "バナナ", "オレンジ", "いちご", "ぶどう"]
    return render_template("fruits.html", fruits=fruits)


@app.route("/omikuji")
def omikuji():
    result = random.choice(["大吉", "中吉", "吉", "凶", "大凶"])
    return render_template("omikuji.html", result=result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
