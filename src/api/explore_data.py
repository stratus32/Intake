import pandas as pd

names_df = pd.read_excel("data/raw/NAME.FT.xlsx", skiprows=1)
codes_df = pd.read_excel("data/raw/Standard CODE.FT.xlsx", skiprows=1)
data_df = pd.read_excel("data/raw/Standard DATA.FT.xlsx", skiprows=1)

print("--- NAMES ---")
print(names_df.columns.tolist())

print("\n--- CODES ---")
print(codes_df.columns.tolist())

print("\n--- DATA ---")
print(data_df.columns.tolist())