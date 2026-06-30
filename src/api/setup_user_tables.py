import sqlite3
import os

# This script lives in src/api/, so go up two levels to reach the project root,
# then into assets/data/ to find the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "..", "..", "assets", "data", "intake.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# One row per meal-section-on-a-day (e.g. "Breakfast, 2026-07-01")
cursor.execute("""
CREATE TABLE IF NOT EXISTS logged_meals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    meal_type TEXT NOT NULL
);
""")

# One row per food item logged inside a meal, linked back via meal_id
cursor.execute("""
CREATE TABLE IF NOT EXISTS logged_food_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_id INTEGER NOT NULL,
    food_name TEXT NOT NULL,
    weight_grams REAL NOT NULL,
    calories REAL,
    carbs REAL,
    fat REAL,
    protein REAL,
    FOREIGN KEY (meal_id) REFERENCES logged_meals (id)
);
""")

conn.commit()  # save changes to the database file
conn.close()

print(f"User tables created successfully at: {db_path}")