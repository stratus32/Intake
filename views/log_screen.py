# views/log_screen.py
import flet as ft

def build_log_screen(page: ft.Page):
    calories_eaten = 0
    calorie_goal = 2000

    progress = calories_eaten / calorie_goal

    calorie_text = ft.Text(str(calories_eaten), size=32, weight=ft.FontWeight.BOLD)
    goal_text = ft.Text(f"/ {calorie_goal} kcal", size=14)

    progress_ring = ft.ProgressRing(
        value=progress,
        width=150,
        height=150,
        stroke_width=12,
        color=ft.Colors.BLUE,
    )

    calorie_ring = ft.Stack(
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

    def handle_click(e):
        nonlocal calories_eaten
        calories_eaten = calories_eaten + 150

        calorie_text.value = str(calories_eaten)
        progress_ring.value = calories_eaten / calorie_goal

        page.update()

    button_add_food = ft.Button(content=ft.Text("Add Food"), on_click=handle_click)

    return ft.Column(
        [
            ft.Text("Today's Log", size=24),
            ft.Container(content=calorie_ring, alignment=ft.alignment.Alignment.CENTER),
            button_add_food,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=40
    )