#play_page.py
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment


def account_page_view(page: Page):
    return View(
        route='/account_page',
        controls=[
            AppBar(title= Text('ACCOUNT PAGE'), bgcolor='blue'),
            Text(value='ACCOUNT PAGE', size=30),
            ElevatedButton(text='Go Back', on_click=lambda _: page.go('/'))
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=26
    )