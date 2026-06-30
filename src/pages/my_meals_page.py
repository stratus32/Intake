import flet as ft

def build_my_meals_page(page: ft.Page):
    # The View represents this entire screen
    return ft.View(
        route="/my-meals",  # this view shows when the route is "/my-meals"
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
            # Placeholder meal sections — these will later show logged food items
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )