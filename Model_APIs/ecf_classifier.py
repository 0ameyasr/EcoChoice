import os, sys
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model import classifier

@app.route("/")
def base():
    return render_template("ecf_api_docs.html")

@app.route("/predict",methods=["POST"])
def predict():
    io = classifier.interface(estimator=None)
    predictor = classifier.interface(
        estimator = io.ecf_classifier(verbose=False)
    )
    try:
        data = request.json
        prediction = predictor.get_prediction(features=[data.get("features",[])])
    except Exception as error:
        return jsonify(success=False,error=f"{error}")
    return jsonify(success=True,verdict=int(prediction))

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=51000)