import os, sys
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model import dp_torch_classifier

@app.route("/")
def base():
    return render_template("dpt_api_docs.html")

@app.route("/classify_profile",methods=["POST"])
def predict_profile():
    try:
        data = request.json
        prediction = dp_torch_classifier.profile_classifier(user_requirements=[data.get("features",[])])
    except Exception as error:
        return jsonify(success=False,error=f"{error}")
    return jsonify(success=True,verdict=prediction)

@app.route("/best_diets",methods=["POST"])
def predict_diets():
    try:
        data = request.json
        prediction = dp_torch_classifier.diet_classifier(item_facts=[data.get("features",[])])
    except Exception as error:
        return jsonify(success=False,error=f"{error}")
    return jsonify(success=True,verdict=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=9000)