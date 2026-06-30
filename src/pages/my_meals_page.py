import flet as ft

def build_my_meals_page(page: ft.Page):
    # The View represents this entire screen
    return ft.View(
        route="/my-meals",  # this view shows when the route is "/my-meals"
        appbar=ft.AppBar(
            title=ft.Text("My Meals", size=18),
            center_title=True,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda e: page.run_task(page.push_route, "/"),
            ),
        ),
        controls=[
            # Placeholder meal sections — these will later show logged food items
            ft.Text("Breakfast"),
            ft.Text("Lunch"),
            ft.Text("Dinner"),
            ft.Text("Snacks"),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )