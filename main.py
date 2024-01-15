import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, IconButton, Row, Column, Container
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from pages.play_page import play_page_view
from pages.settings_page import settings_page_view
from pages.profile_page import profile_page_view
from design import color_variables

def main(page: Page) -> None:
    def update_colors():
        global mainc,white, red, black, green
        mainc, white, red, black, green = color_variables()

    page.title = "MAIN PAGE"

    def route_change(e:RouteChangeEvent) -> None:
        
        page.views.clear()
        update_colors()

        #home_page design
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(
                        title= Text('MINDSWEEPER'), 
                        bgcolor=mainc,
                        center_title=True,
                        actions=[
                            Row([
                                IconButton(
                                    icon = ft.icons.SETTINGS,
                                    icon_color=white,
                                    on_click=lambda _: page.go('/settings_page')
                                ),
                                IconButton(
                                    icon = ft.icons.ACCOUNT_CIRCLE,
                                    icon_color=white,
                                    on_click=lambda _: page.go('/profile_page')
                                )
                            ])
                        ]
                    ),
                    Column(
                        [
                            Text(value='M I N D S W E E P E R', size=30, weight=ft.FontWeight.BOLD),
                            Text(value="The game that blows your mind",size=15,italic=True)
                        ],
                        spacing=10,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                    Container(
                        height=25,
                    ),
                    ElevatedButton(
                        text='Play',
                        color = white,
                        on_click=lambda _: page.go('/play_page'),
                        icon= ft.icons.GAMEPAD,
                        icon_color=mainc),
                    ElevatedButton(
                        text='Settings',
                        color = white,
                        on_click=lambda _: page.go('/settings_page'),
                        icon = ft.icons.SETTINGS,
                        icon_color=mainc),
                    ElevatedButton(
                        text='Profile',
                        color = white,
                        on_click=lambda _: page.go('/profile_page'),
                        icon = ft.icons.ACCOUNT_BOX,
                        icon_color=mainc),
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
            )
        )

        #ruta catre play_page
        if page.route == '/play_page':
            page.views.append(play_page_view(page))

        #ruta catre settings_page
        if page.route == '/settings_page':
            page.views.append(settings_page_view(page))

        #ruta catre profile_page
        if page.route == '/profile_page':
            page.views.append(profile_page_view(page))
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