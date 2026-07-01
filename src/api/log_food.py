import sqlite3
import os
from datetime import date

today = date.today().isoformat()  # returns "2026-07-01" as a string

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "..", "..", "assets", "data", "intake.db")


def get_or_create_meal(cursor, date, meal_type):
    cursor.execute(
        "SELECT id FROM logged_meals WHERE date = ? AND meal_type = ?",
        (date, meal_type)
    )
    result = cursor.fetchone()

    if result:
        return result[0]  # existing meal's id

    cursor.execute(
        "INSERT INTO logged_meals (date, meal_type) VALUES (?, ?)",
        (date, meal_type)
    )
    return cursor.lastrowid  # id of the row we just created


def log_food_item(date, meal_type, food_name, weight_grams, calories, carbs, fat, protein):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    meal_id = get_or_create_meal(cursor, date, meal_type)

    cursor.execute(
        """INSERT INTO logged_food_items
           (meal_id, food_name, weight_grams, calories, carbs, fat, protein)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (meal_id, food_name, weight_grams, calories, carbs, fat, protein)
    )

    conn.commit()
    conn.close()

def get_meals_for_date(date):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """SELECT logged_meals.id, logged_meals.meal_type,
                  logged_food_items.food_name, logged_food_items.weight_grams,
                  logged_food_items.calories, logged_food_items.carbs,
                  logged_food_items.fat, logged_food_items.protein
           FROM logged_meals
           JOIN logged_food_items ON logged_meals.id = logged_food_items.meal_id
           WHERE logged_meals.date = ?""",
        (date,)
    )
    rows = cursor.fetchall()
    conn.close()

    # Organize the flat rows into a dict grouped by meal_type
    meals = {"breakfast": [], "lunch": [], "dinner": []}

    for row in rows:
        meal_id, meal_type, food_name, weight_grams, calories, carbs, fat, protein = row
        meals[meal_type].append({
            "food_name": food_name,
            "weight_grams": weight_grams,
            "calories": calories,
            "carbs": carbs,
            "fat": fat,
            "protein": protein
        })

    return meals


if __name__ == "__main__":
    result = get_meals_for_date("2026-07-01")
    print(result)