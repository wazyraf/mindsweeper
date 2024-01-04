import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from mainpages.play_page import play_page_view
from mainpages.settings_page import settings_page_view
from mainpages.account_page import account_page_view

def main(page: Page) -> None:
    page.title = "MAIN PAGE"

    def route_change(e:RouteChangeEvent) -> None:
        page.views.clear()

        #HOME
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title= Text('HOME'), bgcolor='blue'),
                    Text(value='HOME', size=30),
                    ElevatedButton(text='Play', on_click=lambda _: page.go('/play_page')),
                    ElevatedButton(text='Account', on_click=lambda _: page.go('/account_page')),
                    ElevatedButton(text='Settings', on_click=lambda _: page.go('/settings_page'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
            )
        )

        #play_page
        if page.route == '/play_page':
            page.views.append(play_page_view(page))

        #settings_page
        if page.route == '/settings_page':
            page.views.append(settings_page_view(page))

        #account_page
        if page.route == '/account_page':
            page.views.append(account_page_view(page))
    page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__== '__main__':
    ft.app(target=main)
    #requirements.txt