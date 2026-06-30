import flet as ft
from pages.home_screen_page import build_home_screen
from pages.my_meals_page import build_my_meals_page

def main(page: ft.Page):
    # Basic page/window setup
    page.title = "Intake"
    page.padding = 20
    page.bgcolor = "#1b1e34"
    page.window.width = 360   # phone-like width for desktop testing
    page.window.height = 585  # phone-like height for desktop testing

    # This function runs every time the route changes (e.g. page.go("/my-meals"))
    # It decides which View should be displayed based on the current route
    def route_change(route):
        page.views.clear()  # remove whatever was shown before

        if page.route == "/":
            page.views.append(build_home_screen(page))
        elif page.route == "/my-meals":
            page.views.append(build_my_meals_page(page))

        page.update()  # tell Flet to redraw the screen with the new view

    # Tell Flet to call route_change whenever the route changes
    page.on_route_change = route_change

    # Manually trigger the first render on startup
    # (we call this directly instead of relying on the route-change event,
    # since the event doesn't reliably fire on initial app load)
    route_change(None)

# Starts the Flet app, using main() as the entry point
ft.run(main)