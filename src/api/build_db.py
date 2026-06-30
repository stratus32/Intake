import pandas as pd
import sqlite3
import os

# This script lives in src/api/, so go up two levels to reach the project root,
# then into assets/data/ to find the raw files and database
script_dir = os.path.dirname(os.path.abspath(__file__))
raw_data_dir = os.path.join(script_dir, "..", "..", "assets", "data", "raw")
db_path = os.path.join(script_dir, "..", "..", "assets", "data", "intake.db")

# Load the three source files, skipping the copyright row
names_df = pd.read_excel(os.path.join(raw_data_dir, "NAME.FT.xlsx"), skiprows=1)
codes_df = pd.read_excel(os.path.join(raw_data_dir, "Standard CODE.FT.xlsx"), skiprows=1)
data_df = pd.read_excel(os.path.join(raw_data_dir, "Standard DATA.FT.xlsx"), skiprows=1)

# Keep only the columns we actually need for now
names_df = names_df[["FoodID", "Food Name"]]
codes_df = codes_df[["Code", "Description", "Unit Code"]]
data_df = data_df[["FoodID", "Component Identifier", "Value"]]

# Connect to (or create) the SQLite database file
conn = sqlite3.connect(db_path)

# Write each dataframe into its own table
names_df.to_sql("foods", conn, if_exists="replace", index=False)
codes_df.to_sql("codes", conn, if_exists="replace", index=False)
data_df.to_sql("nutrients", conn, if_exists="replace", index=False)

conn.close()

print(f"Database built: {db_path}")