from flask import Flask, render_template, request, jsonify
from models.marks.marks import marks_prediction, get_dataset


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
        if hours.isnumeric():
            marks = marks_prediction(hours)
            return jsonify({"marks": round(marks, 2), "status": "success"})
    return render_template("index.html")

@app.route("/dataset", methods=["GET"])
def dataset():
    dataset = get_dataset()
    data = {
        "data": dataset[0],
        "description": dataset[1],
        "status": "success",
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
