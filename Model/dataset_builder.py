import pandas
import random
import numpy

def make_features():
    PRICE = pandas.DataFrame([numpy.round(random.uniform(1,8),decimals=2) for _ in range(100)],columns=["PRICE"])
    AVG_RATING = pandas.DataFrame([numpy.round(random.uniform(1,5),1) for _ in range(100)],columns=["AVG_RATING"])
    NUM_RATING = pandas.DataFrame([random.randint(100,2000) for _ in range(100)],columns=["NUM_RATING"])
    PACKAGING = pandas.DataFrame([random.randint(0,2) for _ in range(100)],columns=["PACKAGING"])
    CFOOT = pandas.DataFrame([random.randint(0,2) for _ in range(100)],columns=["CFOOT"])
    RECYCLE = pandas.DataFrame([random.randint(0,2) for _ in range(100)],columns=["RECYCLE"])
    BIODEG = pandas.DataFrame([random.randint(0,1) for _ in range(100)],columns=["BIODEG"])
    ORGANIC = pandas.DataFrame([random.randint(0,1) for _ in range(100)],columns=["ORGANIC"])
    EMISSIONS = pandas.DataFrame([random.randint(0,2) for _ in range(100)],columns=["EMISSIONS"])
    IMPORTED = pandas.DataFrame([random.randint(0,1) for _ in range(100)],columns=["IMPORTED"])
    PROCESSED = pandas.DataFrame([random.randint(0,2) for _ in range(100)],columns=["PROCESSED"])
    features = pandas.concat([PRICE, AVG_RATING, NUM_RATING, PACKAGING, CFOOT, RECYCLE, BIODEG, ORGANIC, EMISSIONS, IMPORTED, PROCESSED], axis=1)
    return features

def commit_dataset(features,path="model/ec_food_dataset.csv"):
    try:
        features.to_csv(path)
        print(f"Dataset successfully commited to {path}")
    except Exception as e:
        print(f"commit_dataset() > An error was encountered: {e}")