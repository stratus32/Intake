import flet as ft
import sys
from datetime import date
import os

# Add src/ to the path so we can import from api/
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from api.log_food import get_meals_for_date

def build_home_screen(page: ft.Page):

    def calculate_totals():
        today = date.today().isoformat()
        meals = get_meals_for_date(today)

        total_calories = 0
        total_carbs = 0
        total_fat = 0
        total_protein = 0

        for meal_items in meals.values():  # loops through breakfast, lunch, dinner lists
            for item in meal_items:        # loops through each food item in that meal
                total_calories += item["calories"] or 0
                total_carbs += item["carbs"] or 0
                total_fat += item["fat"] or 0
                total_protein += item["protein"] or 0

        return total_calories, total_carbs, total_fat, total_protein
    

    # Placeholder values — later these will come from your database
    calories_eaten, total_carbs, total_fat, total_protein = calculate_totals()
    calorie_goal = 2000

    # Progress as a 0-1 float, used to fill the ring
    progress = calories_eaten / calorie_goal

    # The circular progress ring itself
    progress_ring = ft.ProgressRing(
        value=progress,
        width=150,
        height=150,
        bgcolor="#474b5e",
        stroke_cap=ft.StrokeCap.ROUND,
        color="#1a6efd",
        stroke_width=15,
    )

    # Text controls for the calorie numbers
    calorie_text = ft.Text(str(calories_eaten), size=32, weight=ft.FontWeight.BOLD)
    goal_text = ft.Text(f"/ {calorie_goal} kcal", size=14)

    # Stack layers the ring and text on top of each other
    ring_with_text = ft.Stack(
        [
            progress_ring,
            ft.Container(
                content=ft.Column(
                    [calorie_text, goal_text],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                ),
                width=150,
                height=150,
                alignment=ft.alignment.Alignment.CENTER,
            ),
        ],
        width=150,
        height=150,
    )

    # NEW: rounded card wrapped around the ring
    calorie_card = ft.Container(
        content=ring_with_text,
        width=200,
        height=200,
        bgcolor="#272b40",
        border_radius=20,
        alignment=ft.alignment.Alignment.CENTER,
        padding=20,
    )

    # --- Macro tracking (carbs/fat/protein) ---

    carbs_eaten, carbs_goal = total_carbs, 250
    fat_eaten, fat_goal = total_fat, 70
    protein_eaten, protein_goal = total_protein, 100

    def build_macro_row(label, eaten, goal, color):
        return ft.Column(
            [
                ft.Text(label, size=12),
                ft.Text(f"{eaten}/{goal}g", size=10),
                ft.ProgressBar(
                    value=eaten / goal,
                    width=55,
                    height=6,
                    border_radius=5,
                    track_gap=1,
                    color=color,
                    bgcolor="#3A3A3A",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
        )

    macro_card = ft.Container(
        content=ft.Row(
            [
                build_macro_row("Carbs", carbs_eaten, carbs_goal, ft.Colors.ORANGE),
                build_macro_row("Fat", fat_eaten, fat_goal, ft.Colors.YELLOW),
                build_macro_row("Protein", protein_eaten, protein_goal, ft.Colors.GREEN),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        width=300,
        bgcolor="#272b40",
        border_radius=20,
        padding=20,
    )

    # Button that navigates to the "My Meals" screen when clicked
    view_meals_button = ft.Button(
        content=ft.Text("View My Meals"),
        on_click=lambda e: page.run_task(page.push_route, "/my-meals"),
        style=ft.ButtonStyle(
        bgcolor="#272b40",
        color=ft.Colors.WHITE,  # text color
        ),
    )

    return ft.View(
        route="/",
        bgcolor="#1b1e34",
        appbar=ft.AppBar(
            title=ft.Text("Today", size=18),
            center_title=True,
            bgcolor="#1b1e34",
        ),
        controls=[
            ft.Column(
                [
                    calorie_card,
                    macro_card,
                    view_meals_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=40,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )