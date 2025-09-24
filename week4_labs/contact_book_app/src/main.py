# main.py
import flet as ft
from database import init_db
from app_logic import display_contacts, add_contact, filter_contacts

def main(page: ft.Page):
    page.title = "Contact Book"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 450
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.LIGHT  # Default theme

    db_conn = init_db()

    # Inputs
    name_input = ft.TextField(label="Name", width=400)
    phone_input = ft.TextField(label="Phone", width=400)
    email_input = ft.TextField(label="Email", width=400)

    inputs = (name_input, phone_input, email_input)

    # Search bar
    search_input = ft.TextField(
        label="Search contacts...",
        width=400,
        on_change=lambda e: filter_contacts(
            page, contacts_list_view, db_conn, search_input.value
        ),
    )

    # Contacts List
    contacts_list_view = ft.ListView(expand=1, spacing=10, auto_scroll=True)

    # Add button
    add_button = ft.ElevatedButton(
        text="Add Contact",
        on_click=lambda e: add_contact(page, inputs, contacts_list_view, db_conn, search_input.value),
    )

    # Theme toggle button
    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    theme_button = ft.IconButton(icon=ft.Icons.DARK_MODE, on_click=toggle_theme)

    # Layout
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Enter Contact Details:", size=20, weight=ft.FontWeight.BOLD),
                        theme_button,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                name_input,
                phone_input,
                email_input,
                add_button,
                ft.Divider(),
                search_input,
                ft.Text("Contacts:", size=20, weight=ft.FontWeight.BOLD),
                contacts_list_view,
            ]
        )
    )

    display_contacts(page, contacts_list_view, db_conn)

if __name__ == "__main__":
    ft.app(target=main)
