#play_page.py
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment


def play_page_view(page: Page):
    return View(
        route='/play_page',
        controls=[
            AppBar(title= Text('PLAY PAGE'), bgcolor='blue'),
            Text(value='PLAY PAGE', size=30),
            ElevatedButton(text='Go Back', on_click=lambda _: page.go('/'))
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=26
    )