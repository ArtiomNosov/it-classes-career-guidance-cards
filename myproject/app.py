from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/error")
def error():
    return render_template("error.html")


@app.route('/<string:profession>')
def skills(profession):
    return render_template("skills.html")


@app.route('/<string:profession>/<string:skills>')
def test(profession, skills):
    return render_template("test.html")


@app.route('/<string:profession>/<string:skills>/description')
def description(profession, skills):
    return render_template("skill-description.html")


@app.route('/<string:profession>/<string:skills>/answer')
def answer(profession, skills):
    return render_template("answer.html")


if __name__ == "__main__":
    app.run(debug = True)