# main.py
import flet as ft
from views.log_screen import build_log_screen

def main(page: ft.Page):
    page.title = "Intake"
    page.padding = 20
    page.window.width = 360
    page.window.height = 585
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(build_log_screen(page))

ft.run(main)