import requests

def get_product_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
    headers = {
        "User-Agent": "Intake - Calorie Tracker App - Version 0.1 - github.com/stratus32/Intake"
    }
    response = requests.get(url, headers=headers)

    # print("Status code:", response.status_code)
    # print("Response text:", response.text[:300])

    data = response.json()

    if data.get("status") != 1:
        print(f"No product found for barcode {barcode}")
        return None

    product = data["product"]
    name = product.get("product_name", "Unknown")
    nutriments = product.get("nutriments", {})

    calories = round(nutriments.get("energy-kcal_100g", 0), 1)
    carbs = nutriments.get("carbohydrates_100g")
    fat = nutriments.get("fat_100g")
    sugars = nutriments.get("sugars_100g")
    added_sugars = nutriments.get("added-sugars_100g")
    protein = nutriments.get("proteins_100g")


    print(f"Found: {name}")
    print(f"  Calories: {calories} kcal (per 100g)")
    print(f"  Carbs: {carbs} g (per 100g)")
    print(f"  Fat: {fat} g (per 100g)")
    print(f"  Sugars: {sugars} g (per 100g)")
    print(f"  Added Sugars: {added_sugars} g (per 100g)")
    print(f"  Protein: {protein} g (per 100g)")


    return {
        "name": name,
        "calories": calories,
        "carbs": carbs,
        "fat": fat,
        "sugars": sugars,
        "added_sugars": added_sugars,
        "protein": protein
    }

if __name__ == "__main__":
    barcode = input("Enter a barcode: ")
    get_product_by_barcode(barcode)