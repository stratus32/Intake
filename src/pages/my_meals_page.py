import flet as ft
from datetime import date
import sys
import os

# Add src/ to the path so we can import from api/
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from api.log_food import get_meals_for_date


def build_my_meals_page(page: ft.Page):
    # Get today's date as a string e.g. "2026-07-01"
    today = date.today().isoformat()

    # Fetch all meals for today from the database
    meals = get_meals_for_date(today)

    def build_meal_section(meal_type, items):
        # Build a list of food item rows for this meal
        if items:
            food_rows = [
                ft.Text(f"{item['food_name']} — {item['weight_grams']}g — {item['calories']} kcal", size=12)
                for item in items
            ]
        else:
            food_rows = [ft.Text("No items logged yet", size=12, color=ft.Colors.GREY_500)]

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(meal_type.capitalize(), size=16, weight=ft.FontWeight.BOLD),
                    *food_rows,  # unpacks the list of food rows into the column
                ],
                spacing=6,
            ),
            bgcolor="#272b40",
            border_radius=12,
            padding=16,
            width=320,
        )

    return ft.View(
        route="/my-meals",
        bgcolor="#1b1e34",
        appbar=ft.AppBar(
            title=ft.Text("My Meals", size=18),
            center_title=True,
            bgcolor="#1b1e34",
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda e: page.run_task(page.push_route, "/"),
            ),
        ),
        controls=[
            ft.Column(
                [
                    build_meal_section("breakfast", meals["breakfast"]),
                    build_meal_section("lunch", meals["lunch"]),
                    build_meal_section("dinner", meals["dinner"]),
                ],
                spacing=16,
                scroll=ft.ScrollMode.AUTO,  # allows scrolling if content overflows
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )