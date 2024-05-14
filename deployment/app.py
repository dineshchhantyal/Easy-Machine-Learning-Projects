from flask import Flask, render_template, request
from models.marks.marks import marks_prediction


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/sub", methods=["POST"])
def sub():
    if request.method == "POST":
        name = request.form["username"]
        return render_template("sub.html", name=name)
    return render_template("index.html")


@app.route("/marks", methods=["POST"])
def marks():
    if request.method == "POST":
        hours = request.form["hours"]
        marks = marks_prediction(hours)
        return render_template("marks.html", marks=marks)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
