import configparser
import pandas
from tqdm import tqdm
from pymongo import MongoClient

def commit_food_products(path:str):
    try:
        try:
            config = configparser.ConfigParser()
            config.read("config.cfg")
            mongo = MongoClient(config["mongodb"]["uri"])
            food = mongo["products"]["food"]
        except Exception as error:
            print(f"Error: {error}")

        food_products = pandas.read_csv(path)
        for _,row in food_products.iterrows():
            food.insert_one(
                {
                    "PRODUCT_ID":row["PRODUCT_ID"],
                    "PRODUCT_NAME":row["PRODUCT_NAME"],
                    "BRAND":row["BRAND"],
                    "PRICE":row["PRICE"],
                    "AVG_RATING":row["AVG_RATING"],
                    "NUM_RATING":row["NUM_RATING"],
                    "PACKAGING":row["PACKAGING"],
                    "CFOOT":row["CFOOT"],
                    "RECYCLE":row["RECYCLE"],
                    "BIODEG":row["BIODEG"],
                    "ORGANIC":row["ORGANIC"],
                    "EMISSIONS":row["EMISSIONS"],
                    "IMPORTED":row["IMPORTED"],
                    "PROCESSED":row["PROCESSED"]
                }
            )
            print(f"Inserted PRODUCT_ID {row['PRODUCT_ID']} ")
        print("Commit successful.")
    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    commit_food_products("model/data/ec_food.csv")