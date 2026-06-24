import pandas as pd
import sqlite3

# Load the three source files
names_df = pd.read_excel("data/raw/NAME.FT.xlsx", skiprows=1)
codes_df = pd.read_excel("data/raw/Standard CODE.FT.xlsx", skiprows=1)
data_df = pd.read_excel("data/raw/Standard DATA.FT.xlsx", skiprows=1)

# Keep only the columns we actually need for now
names_df = names_df[["FoodID", "Food Name"]]
codes_df = codes_df[["Code", "Description", "Unit Code"]]
data_df = data_df[["FoodID", "Component Identifier", "Value"]]

# Connect to (or create) the SQLite database file
conn = sqlite3.connect("data/intake.db")

# Write each dataframe into its own table
names_df.to_sql("foods", conn, if_exists="replace", index=False)
codes_df.to_sql("codes", conn, if_exists="replace", index=False)
data_df.to_sql("nutrients", conn, if_exists="replace", index=False)

conn.close()

print("Database built: data/intake.db")