#play_page.py
import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, IconButton, Row
from flet import CrossAxisAlignment, MainAxisAlignment


def settings_page_view(page: Page):
    return View(
        route='/settings_page',
        controls=[
            AppBar(title= Text('SETTINGS PAGE'), bgcolor='blue',
                   actions=[
                            Row([
                                IconButton(
                                    icon = ft.icons.SETTINGS,
                                    icon_color='white',
                                    on_click=lambda _: page.go('/settings_page')
                                ),
                                IconButton(
                                    icon = ft.icons.ACCOUNT_CIRCLE,
                                    on_click=lambda _: page.go('/account_page')
                                )
                            ])
                        ]),
            Text(value='SETTINGS PAGE', size=30),
            ElevatedButton(text='Go Back', on_click=lambda _: page.go('/'))
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=26
    )