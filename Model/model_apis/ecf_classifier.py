import os, sys
from flask import Flask, request, jsonify

app = Flask(__name__)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model import classifier

@app.route("/")
def base():
    information = """The EcoChoice Food Classifier API is active!\n\n
    If you're willing to run the Flask API on your local machine, beware that by
    default this API will use port 5000. You can make a prediction by directing a 
    JSON payload on the /predict route. It is mandatory to send your requests 
    jsonified in the following format (as an example):

    {"features" : [0,1,1,1,0,0,1,1]}

    NOTE: Make sure to use a 1D array. The response is usually a json object as follows:
    {"success": true, "verdict": 0 or 1} [FOR SUCCESSFUL PREDICTIONS], or
    {"success": false, "error": <error>} [FOR UNSUCCESSFUL PREDICTIONS]

    """
    return information

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
    app.run(host="0.0.0.0",debug=True)