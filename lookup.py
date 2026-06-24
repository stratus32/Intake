import sqlite3

def get_food_info(search_term):
    conn = sqlite3.connect("data/intake.db")
    cursor = conn.cursor()

    # Find matching foods by name (case-insensitive, partial match)
    cursor.execute(
        "SELECT FoodID, \"Food Name\" FROM foods WHERE \"Food Name\" LIKE ?",
        (f"%{search_term}%",)
    )
    matches = cursor.fetchall()

    if not matches:
        print(f"No matches found for '{search_term}'")
        conn.close()
        return

    # Just use the first match for now
    food_id, food_name = matches[0]
    print(f"Found: {food_name} (FoodID: {food_id})")

    # Look up calories (ENERC_KCAL) and carbs (CHOAVLDF) for this FoodID
    cursor.execute(
        """SELECT "Component Identifier", Value FROM nutrients
           WHERE FoodID = ? AND "Component Identifier" IN ('ENERC_KCAL', 'CHOAVLDF')""",
        (food_id,)
    )
    results = cursor.fetchall()

    for component, value in results:
        if component == "ENERC_KCAL":
            print(f"  Calories: {value} kcal (per 100g)")
        elif component == "CHOAVLDF":
            print(f"  Carbs: {value} g (per 100g)")

    conn.close()


if __name__ == "__main__":
    search = input("Enter a food name: ")
    get_food_info(search)