from flask import Flask, render_template, request, redirect, url_for, jsonify

home = Flask(__name__, template_folder="templates")

volume = 50 #Algne heli
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



@home.route("/get_volume", methods=["GET"]) #Võtab valitud heliväärtuse
def get_volume():
    return jsonify(volume=volume)

@home.route("/update_volume", methods=["POST"]) #Uuendab heliväärtust, lehtede vahel
def update_volume():
    global volume
    data = request.get_json()
    volume = data.get('volume', 50)
    return jsonify(success=True)


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
