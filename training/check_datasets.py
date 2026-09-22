import pandas as pd

df = pd.read_csv("datasets/heart_disease_uci.csv")

print(df["num"].value_counts())