# EcoChoice

EcoChoice is a smart tagging and personalized recommendation system designed to help consumers make eco-friendly and health-conscious food choices. By leveraging advanced machine learning models, EcoChoice tags products based on environmental sustainability and recommends personalized dietary options tailored to individual preferences.

## Features

### EcoChoice Food Tagging
- **Environmental Evaluation**: Analyzes products based on factors like plastic usage, carbon footprint, recyclability, and more.
- **Sustainability Classification**: Uses a Support Vector Machine Classifier (SVC) to tag products as EcoChoice items.

### Personalized Food Recommendations
- **Dietary Profiling**: Collects user dietary preferences through a survey.
- **Custom Recommendations**: Utilizes an artificial neural network (ANN) to match products with user dietary goals, including overall health improvement, vitamin essentials, increased protein intake, and low sodium diets.

## Technical Implementation

- **Food Tagging Classifier**: Implemented using SVC from the sklearn library in Python.
- **User Profile Classification**: Managed by an ANN built with PyTorch.
- **User Interface**: Built using Flask for the back-end, and HTML, CSS, and JavaScript for the front-end.
- **APIs**: 
  - **EcoChoice Food (ECF) Classifier API**: For tagging products.
  - **EcoChoice Dietary Profile Torch (DPT) Classifier API**: For managing user profiles and product-diet matching.
- **Database**: MongoDB hosted on Atlas Cloud.
- **Containerization**: Docker used for API containerization.

# API Docs

## EcoChoice ECF API

This API provides predictions on whether a food item qualifies as an EcoChoice item based on its environmental and sustainability features.

### Endpoint

- **URL**: `http://localhost:5000/predict`
- **Method**: POST
- **Content-Type**: application/json

### Example JSON Payload

To make a prediction, POST a JSON payload to the `/predict` route. Ensure your request is formatted as follows:

```json
{
    "features": [0, 1, 1, 1, 0, 0, 1, 1]
}
```

### Response Format
For successful predictions, the response will be:

0 for negative, 
```json
{
    "success": true,
    "verdict": 0
}
```

1 for positive,
```json
{
    "success": true,
    "verdict": 1
}
```

For unsuccessful predictions, the response will be:

```json
{
    "success": false,
    "error": error
}
```

### **Features**
- PACKAGING: How much plastic packaging the item requires (0 for low, 1 for normal, 2 for high)
- CFOOT: The item's carbon footprint (0 for low, 1 for normal, 2 for high)
- RECYCLE: Extent of recyclability (0 for low, 1 for normal, 2 for high)
- BIODEG: How biodegradable the item or its packaging itself is (0 for low, 1 for normal, 2 for high)
- ORGANIC: Is the item organic? (0 for true, 1 for false)
- EMISSIONS: Scale of emissions in production and transport (0 for low, 1 for normal, 2 for high), highly correlated with CFOOT
- IMPORTED: Is the item imported?
- PROCESSED: To what extent has the item been processed? (0 for low, 1 for normal, 2 for high)

## EcoChoice DPT Classifier API

This API runs on port 9000 by default. You can make predictions by sending JSON payloads to the /classify_profile or /best_diets routes. Ensure your requests are formatted as shown below:

### POST ```/classify_profile```
This route classifies a user's profile based on their preferences and needs. It uses the following 7 features: [DESCAL, DESFAT, MONCHOL, MONSUG, MONPROT, MONVIT, MONMIN].

### Endpoint

- **URL**: `http://localhost:9000/classify_profile`
- **Method**: POST
- **Content-Type**: application/json

### Example JSON payload:
```json{"features": [0, 1, 1, 1, 0, 0, 1]}```

### (Example) Response format:

```json
{
    "success": true,
    "verdict": "HLTI"
}
```
**NOTE**: A successful verdict can be "HLTI", "VIT_ESS", "PROT_IN" or "LOW_SOD".
        
or

```json
{
    "success": false,
    "error": ""
}
```
        
### POST ```/best_diets```
This route recommends the best diets based on the user's profile. It uses 14 features: [CHOL, TOTALCARB, ADDSUG, PROT, VITD, VITA, VITB2, VITB12, VITC, CALC, SOD, IRON, POT, PHOS].

### Example JSON payload:
```json
{"features": [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1]}
```

### (Example) Response format:

```json
{
    "success": true,
    "verdict": [
        [
            0.42032456398010254,
            0.27680620551109314,
            0.4458279609680176,
            0.4440215826034546
        ]
    ]
}
```

**NOTE**: A successful verdict is a vector of probabilities that suggest how well the given product matches the specific
diet on the particular index. That is, 0 is for "HLTI", 1 for "VIT_ESS", 2 for "PROT_IN" and 3 for "LOW_SOD" diet profiles.

or

```json
{
    "success": false,
    "error": ""
}
```
        
### About the API
The POST ```/classify_profile``` route:
This route will take 7 **derived** features as input. They are as follows,
- **DESCAL**: Desired calorie intake.
- **DESFAT**: Desired fat intake.
- **MONCHOL**: Monitoring in cholesterol levels.
- **MONSUG**: Monitoring in sugar levels.
- **MONPROT**: Monitoring in protein levels.
- **MONVIT**: Monitoring in vitamin (overall B2,B12,C,D,A) levels.
- **MONMIN**: Monitoring in mineral (calcium, sodium, iron, potassium, phosphorous) levels.

Based on special calculations and recognizing patterns, the verdict (prediction) will be:
- **"HLTI"** - The user's profile is closest to the overall Health Improvement Diet
- **"VIT_ESS"** - The user's profile is closest to the overall Vitamin Essentials Diet
- **"PROT_IN"** - The user's profile is closest to the increased Balanced Protein Intake Diet
- **"LOW_SOD"** - The user's profile best fits a Low Sodium Diet.

The POST ```/best_diets``` route:
This route will take 14 features as input. They are as follows,

- **CHOL**: cholesterol per daily value in food item
- **TOTALCARB**: total carbohydrates per daily value in food item
- **ADDSUG**: added sugar per daily value in food item
- **PROT**: protein per daily value in food item
- **VITD**: vitamin D per daily value in food item
- **VITA**: vitamin A per daily value in food item
- **VITB2**: vitamin B2 per daily value in food item
- **VITB12**: vitamin B12 per daily value in food item
- **VITC**: vitamin C per daily value in food item
- **CALC**: calcium per daily value in food item
- **SOD**: sodium per daily value in food item
- **IRON**: iron per daily value in food item
- **POT**: potassium per daily value in food item
- **PHOS**: phosphorous per daily value in food item

**NOTE**: Each of these inputs in the dataset has been represented in ordinal form. That is, 0 for low presence, 1 for normal to medium, 2 for high and above.

Based on special calculations and recognizing patterns, the verdict (prediction) will be an array of probabilities of matches for the various diets in the form given as (matchings in scale < 1) [HLTI,VIT_ESS,PROT_IN,LOW_SOD]. The diet with the highest likelihood matching (probability) can be flagged to the item, or you can alternatively use a confidence threshold, say 0.45, which is 
as good as calling 90% confidence in the prediction (this is because the matchings are at most in close corrections to 0.50 (+ 0.2 at most). 

**Integration Workflow**
- Allow the user to fill in their preferences details through a form.
- Based on their responses, fill in ordinal values for each feature.
- POST /classify_profile to the API
- Once you have the profile verdict, store it.
- For items displayed, POST /best_diets for each item efficiently
- Once you get the matchings array through the verdict, extract probabilities for the user's diet profile stored previously.
- Display the items in sorted order of their matchings to the user's profile.

### Form to be Integrated
**Each option is tagged with the ordinal value to be fit into the API.**

**Nutritional Intake**
-  Desired calorie intake:
2 - Increase
1 - Stay normal
0 - Decrease
- Desired total fat intake:
2 - Increase
1 - Stay normal
0 - Decrease

**Monitoring Information**
- Monitor cholesterol level to:
0 - Decrease in general
1 - Remain normal
- Monitor added sugar levels to:
0 - Decrease in general
1 - Remain normal

**Vitamins & Nutrients**
- Monitor protein levels to:
2 - Increase
1 - Stay normal
0 - Decrease

**Monitor vitamin levels for**:
- Vitamin D:
1 - Increase
0 - Stay normal
- Vitamin A:
1 - Increase
0 - Stay normal
- Vitamin B2 (Riboflavin):
1 - Increase
0 - Stay normal
- Vitamin B12:
1 - Increase
0 - Stay normal
- Vitamin C:
1 - Increase
0 - Stay normal
- Vitamin E:
1 - Increase
0 - Stay normal

**Minerals**
- Monitor mineral levels for:
- Calcium:
2 - Increase
1 - Stay normal
0 - Decrease
- Sodium (salt):
2 - Increase
1 - Stay normal
0 - Decrease
- Iron:
2 - Increase
1 - Stay normal
0 - Decrease
- Potassium:
2 - Increase
1 - Stay normal
0 - Decrease
- Phosphorous:
2 - Increase
1 - Stay normal
0 - Decrease

## Running the API and Web Server
To run the web server, clone this repository. Then, proceed to move to the ```Flask``` folder, using a suitable command on your relevant OS. Next, run the bundled python Flask module, the most common invokation being ```python -m flask --app walmart run --debug --port 7000```. The port ```7000``` can be any port of your choice, other than ```5000``` or ```9000```, on which both the ECF as well as the DPT classifier will operate, respectively.

Both APIs have been created on Flask, and containerized using Docker. You must pull these images and run them in separate virtual containers. 
- ECF API: ```docker pull ameyasrivastava/ecf-classifier-api```
- DPT API: ```docker pull ameyasrivastav/dpt-classifier-api```

**NOTE**: Before pulling, make sure you login using ```docker login```.

To run the containerized images, use
- ECF API: ```docker run -p <free_port>:5000 ameyasrivastava/ecf-classifier-api```
- DPT API: ```docker run -p <free_port>:9000 ameyasrivastav/dpt-classifier-api```

**NOTE**: ```<free_port>``` recommended is 5000 for ECF API and 9000 for DPT API. You might find some conflicts in available ports if you are on Linux or Mac OS. You may also specify ```--platform linux/amd64``` in such cases.
