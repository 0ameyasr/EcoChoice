import pandas as pd

path = "Model/data/ec_diet_dataset_v3.csv"
df = pd.read_csv(path)

columns_to_process = ['HLTI', 'VIT_ESS', 'PROT_IN', 'LOW_SOD']

def normalize_column(column):
    return (column - column.min()) / (column.max() - column.min())

for column in columns_to_process:
    df[column] = normalize_column(df[column])

df.to_csv("Model/data/ec_diet_dataset_v3.csv", index=False)

print("Processing complete. The modified data has been saved.")
