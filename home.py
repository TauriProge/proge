from flask import Flask, render_template, request, redirect, url_for

home = Flask(__name__, template_folder="templates")

@home.route("/")
def index():
    return render_template("index.html")


@home.route("/circle")
def circle():
    return render_template("circle.html")

@home.route("/symmetry")
def symmetry():
    return render_template("symmetry.html")

if __name__ == '__main__':
    home.run(debug=True)
