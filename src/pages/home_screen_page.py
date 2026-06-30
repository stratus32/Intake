import flet as ft

def build_home_screen(page: ft.Page):
    # Placeholder values — later these will come from your database
    calories_eaten = 0
    calorie_goal = 2000

    # Progress as a 0-1 float, used to fill the ring
    progress = 0.01 + calories_eaten / calorie_goal

    # The circular progress ring itself
    progress_ring = ft.ProgressRing(
        value=progress,
        width=150,
        height=150,
        stroke_width=12,
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
        bgcolor="#2A2A2A",
        border_radius=20,
        alignment=ft.alignment.Alignment.CENTER,
        padding=20,
    )

    # Button that navigates to the "My Meals" screen when clicked
    view_meals_button = ft.Button(
        content=ft.Text("View My Meals"),
        on_click=lambda e: page.run_task(page.push_route, "/my-meals"),
    )

    return ft.View(
        route="/",
        appbar=ft.AppBar(
            title=ft.Text("Today's Log", size=18),
            center_title=True,
        ),
        controls=[
            ft.Column(
                [
                    calorie_card,         # <- using the card now instead of ring_with_text directly
                    view_meals_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=40,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )