# play_page.py
import flet as ft
from flet import View, Page, AppBar, Text, IconButton, Row, Column, Switch, ElevatedButton, Container
from flet import CrossAxisAlignment, MainAxisAlignment

sound_state = True  
def sound_val():
    return sound_state

def settings_page_view(page: Page):
    def dropdown_changed(e):
        selected_value = e.new_value
        print(f"Dropdown changed to {selected_value}")
        page.update()

    def switch_changed(e):
        global sound_state
        sound_state = not sound_state
        print(f"sound_state in settings_page.py: {sound_state}")
    
    return View(
        route='/settings_page',
        controls=[
            AppBar(title=Text('SETTINGS PAGE'), bgcolor='blue',
                   actions=[
                       Row([
                           IconButton(
                               icon=ft.icons.SETTINGS,
                               icon_color='white',
                               on_click=lambda _: page.go('/settings_page')
                           ),
                           IconButton(
                               icon=ft.icons.ACCOUNT_CIRCLE,
                               icon_color='white',
                               on_click=lambda _: page.go('/profile_page')
                           )
                       ]),
                   ]),    
            Row([
                Text(value="Sound", color='blue', size= 20),
                Switch(
                    value=sound_state,
                    on_change=switch_changed
                )
            ],
            alignment=MainAxisAlignment.CENTER
            ),
            Container(
                height= 20
            ),
            Row([
                Text(value="Theme", color='blue', size=20),
                ft.Text(),
                ft.Dropdown(
                    on_change=dropdown_changed,
                    options=[
                        ft.dropdown.Option("Default Theme"),
                        ft.dropdown.Option("Light Theme"),
                        ft.dropdown.Option("Dark Theme"),
                    ],
                    width=200,
                    value="Default Theme"
                )
            ],
            alignment=MainAxisAlignment.CENTER)  
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=20
    )
