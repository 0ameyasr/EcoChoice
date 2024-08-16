import os, sys
from flask import Flask, request, session, redirect, render_template, flash
import requests
import configparser
from pymongo import MongoClient
import json


app = Flask(__name__)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

config = configparser.ConfigParser()
config.read("../config.cfg")
app.secret_key = config["app"]["secret_key"]
client = MongoClient(config["mongodb"]["uri"])

db = client['products']
collection = db['food']

@app.route("/")
def home():
    return render_template("home.html")
from flask import Flask, request, session, render_template

@app.route("/food")
def index():
    user_profile = session.get('PROFILE')

    categories = {
        'fruit': [],
        'veg': [],
        'egg': [],
        'dairy': [],
        'vegan Dairy': [],
        'meat': [],
        'seafood': [],
        'snack': [],
        'packaged': [],
        'grain': [],
        'bread': [],
        'beverage': []
    }
    suggested = []

    all_products = collection.find()

    session['explanations'] = {
        'HLTI': (
            "We noticed that your profile highlights a focus on general health improvement. "
            "Hence, we suggest the following items that are rich in nutrients and have been shown "
            "to contribute positively to overall health. These products are selected to help you "
            "maintain a healthy lifestyle and support your well-being."
        ),
        'VIT_ESS': (
            "We noticed that your profile emphasizes the importance of essential vitamins. "
            "Therefore, we recommend these items that are packed with crucial vitamins to support "
            "your daily nutritional needs. Incorporating these products into your diet will help ensure "
            "you get the vital nutrients necessary for optimal health."
        ),
        'PROT_IN': (
            "We see that your profile indicates a focus on increasing protein intake. "
            "To assist with this, we have suggested these items that are high in protein. "
            "These products are ideal for building and repairing tissues, making them a great addition "
            "to your diet if you're looking to boost your protein consumption."
        ),
        'LOW_SOD': (
            "Your profile suggests a preference for low sodium options. "
            "In response, we have recommended these items that are low in sodium. "
            "Reducing sodium intake is beneficial for managing blood pressure and overall heart health. "
            "These products will help you keep your sodium levels in check while still enjoying flavorful foods."
        )
    }

    for product in all_products:
        product['_id'] = str(product['_id'])

        payload = {
            "features": [
                product["CHOL"],
                product["TOTALCARB"],
                product["ADDSUG"],
                product["PROT"],
                product["VITD"],
                product["VITA"],
                product["VITB2"],
                product["VITB12"],
                product["VITC"],
                product["CALC"],
                product["SOD"],
                product["IRON"],
                product["POT"],
                product["PHOS"]
            ]
        }

        api_url = "http://localhost:9000/best_diets"
        response = requests.post(api_url, json=payload)
        response = response.json()
        if response["success"] == True:
            verdict = response["verdict"][0]
            HLTI = verdict[0]
            VIT_ESS = verdict[1]
            PROT_IN = verdict[2]
            LOW_SOD = verdict[3]
            collection.update_one({"_id":product["_id"]},{"$set":{
                "HLTI":HLTI,
                "VIT_ESS":VIT_ESS,
                "PROT_IN":PROT_IN,
                "LOW_SOD":LOW_SOD
            }})

        product_class = product.get('CLASS')
        if product_class in categories:
            categories[product_class].append(product)

            hlti = product.get('HLTI', 0)
            vit_ess = product.get('VIT_ESS', 0)
            prot_in = product.get('PROT_IN', 0)
            low_sod = product.get('LOW_SOD', 0)

            product_match=product.get(user_profile,"NULL") 
            
            if product_match > 0.45:
                suggested.append(product)

    session['suggested'] = suggested

    return render_template('products.html', categories=categories, suggested=suggested)

@app.route("/session")
def sessiondata():
    for key in session:
        print(key,session[key])
    return "check terminal"

@app.route("/clearsession")
def clearsessiondata():
    session['DESCAL'] = -1
    session['DESFAT'] = -1
    session['MONCHOL'] = -1
    session['MONSUG'] = -1
    session['MONPROT'] = -1
    session['MONVIT'] = -1
    session['MONMIN'] = -1
    session['SURVEY'] = False
    return "cleared session data"

@app.route("/profile_survey", methods=["POST"])
def survey():
    descale = int(request.form.get('calorie_intake'))
    desfat = int(request.form.get('fat_intake'))
    monchol = int(request.form.get('cholesterol_monitor'))
    monsug = int(request.form.get('sugar_monitor'))
    monprot = int(request.form.get('protein_monitor'))

    vitamin_d = int(request.form.get('vit_d_monitor'))
    vitamin_a = int(request.form.get('vit_a_monitor'))
    vitamin_b2 = int(request.form.get('vit_b2_monitor'))
    vitamin_b12 = int(request.form.get('vit_b12_monitor'))
    vitamin_c = int(request.form.get('vit_c_monitor'))
    vitamin_e = int(request.form.get('vit_e_monitor'))

    calcium = int(request.form.get('calcium_monitor'))
    sodium = int(request.form.get('sodium_monitor'))
    iron = int(request.form.get('iron_monitor'))
    potassium = int(request.form.get('potassium_monitor'))
    phosphorous = int(request.form.get('phosphorous_monitor'))

    vitamins = [vitamin_d, vitamin_a, vitamin_b2, vitamin_b12, vitamin_c, vitamin_e]
    monvit = 1 if sum(vitamin == 1 for vitamin in vitamins) >= 3 else 0

    minerals = [calcium, sodium, iron, potassium, phosphorous]
    monmin = 1 if sum(mineral >= 1 for mineral in minerals) >= 3 else 0

    payload = {
        "features": [descale, desfat, monchol, monsug, monprot, monvit, monmin]
    }

    session['DESCAL'] = descale
    session['DESFAT'] = desfat
    session['MONCHOL'] = monchol
    session['MONSUG'] = monsug
    session['MONPROT'] = monprot
    session['MONVIT'] = monvit
    session['MONMIN'] = monmin
    session['SURVEY'] = True

    api_url = "http://localhost:9000/classify_profile"
    response = requests.post(api_url, json=payload)
    
    if response.ok:
        data = response.json()
        if data.get('success'):
            session['PROFILE'] = data.get('verdict')
            flash("Great! We've updated your profile!", "success")
        else:
            flash("Error: " + data.get('error', 'Unknown error'), "danger")
    else:
        flash("Failed to reach the API", "danger")

    return redirect("/")