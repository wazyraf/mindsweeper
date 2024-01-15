# settings_page.py
import flet as ft
from flet import View, Page, AppBar, Text, IconButton, Row, Column, Switch, ElevatedButton, Container
from flet import CrossAxisAlignment, MainAxisAlignment
from design import on_theme_change, color_variables
mainc, white, red, black, green = color_variables()
sound_state = True
current_color = "Default"


def update_colors():
    global mainc,white, red, black, green
    mainc, white, red, black, green = color_variables()
    
def sound_val():
    return sound_state

def settings_page_view(page: Page):
    app_bar = AppBar(title=Text('SETTINGS PAGE'), bgcolor=mainc,
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
                   ])

    def dropdown_changed(e):
        global current_color, mainc
        selected_value = e.control.value
        print(f"Dropdown changed to {selected_value}")
        current_color = selected_value
        on_theme_change(selected_value)
        update_colors()
        app_bar.bgcolor = mainc
        sound_text.color = mainc
        theme_text.color = mainc
        page.update()

    def switch_changed(e):
        global sound_state
        sound_state = not sound_state
        print(f"sound_state in settings_page.py: {sound_state}")
    
    sound_text = Text(value="Sound", color=mainc, size=20)
    theme_text = Text(value="Theme", color=mainc, size=20)
    
    return View(
        route='/settings_page',
        controls=[
            app_bar,
            Row([
                sound_text,
                Switch(
                    value=sound_state,
                    on_change=switch_changed,
                    active_color = white
                )
            ],
            alignment=MainAxisAlignment.CENTER
            ),
            Container(
                height= 20
            ),
            Row([
                theme_text,
                ft.Text(),
                ft.Dropdown(
                    on_change=dropdown_changed,
                    options=[
                        ft.dropdown.Option("Default"),
                        ft.dropdown.Option("Green"),
                        ft.dropdown.Option("Vegas Gold"),
                        ft.dropdown.Option("Majorelle"),
                    ],
                    width=200,
                    value=current_color,
                    color=white
                )
            ],
            alignment=MainAxisAlignment.CENTER),
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=20
    )
