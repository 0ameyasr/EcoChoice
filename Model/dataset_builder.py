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

def make_diet_features():
    ENERGY = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["ENERGY"])
    TOTFAT = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["TOTFAT"])
    CHOL = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["CHOL"])
    TOTALCARB = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["TOTALCARB"])
    ADDSUG = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["ADDSUG"])
    PROT = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["PROT"])
    VITD = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["VITD"])
    VITA = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["VITA"])
    VITB2 = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["VITB2"])
    VITB12 = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["VITB12"])
    VITC = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["VITC"])
    CALC = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["CALC"])
    SOD = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["SOD"])
    IRON = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["IRON"])
    POT = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["POT"])
    PHOS = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["PHOS"])
    
    features = pandas.concat([ENERGY,TOTFAT,CHOL,TOTALCARB,ADDSUG,PROT,VITD,VITA,VITB2,VITB12,VITC,CALC,SOD,IRON,POT,PHOS], axis=1)
    return features

def make_profile_features():
    DESCAL = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["DESCAL"])
    DESFAT = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["DESFAT"])
    MONCHOL = pandas.DataFrame([random.randint(0,1) for _ in range(2000)],columns=["MONCHOL"])
    MONSUG = pandas.DataFrame([random.randint(0,1) for _ in range(2000)],columns=["MONSUG"])
    MONPROT = pandas.DataFrame([random.randint(0,2) for _ in range(2000)],columns=["MONPROT"])
    MONVIT = pandas.DataFrame([random.randint(0,1) for _ in range(2000)],columns=["MONVIT"])
    MONMIN = pandas.DataFrame([random.randint(0,1) for _ in range(2000)],columns=["MONMIN"])
    features = pandas.concat([DESCAL,DESFAT,MONCHOL,MONSUG,MONPROT,MONVIT,MONMIN],axis=1)
    return features

def commit_dataset(features,path="Model/data/ec_profile_dataset.csv"):
    try:
        features.to_csv(path)
        print(f"Dataset successfully commited to {path}")
    except Exception as e:
        print(f"commit_dataset() > An error was encountered: {e}")

if __name__ == "__main__":
    commit_dataset(make_profile_features())