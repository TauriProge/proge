from flask import Flask, render_template, request, redirect, url_for, jsonify

home = Flask(__name__, template_folder="templates")

high_scores = {'circle': 0} #Algselt võtab 0 high scoreks

@home.route("/")
def index():
    return render_template("index.html")


@home.route("/circle")
def circle():
    return render_template("circle.html")

@home.route("/symmetry")
def symmetry():
    return render_template("symmetry.html")

@home.route("/update_score", methods = ['POST'])
def update_score():
    data = request.get_json()
    score = data['score']
    
    new_high_score = False
    if score > high_scores['circle']:
        high_scores['circle'] = score
        new_high_score = True
    
    return jsonify({
        'new_high_score': new_high_score,
        'high_score': high_scores['circle']
    })

if __name__ == '__main__':
    home.run(debug=True)
