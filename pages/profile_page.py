import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import CrossAxisAlignment, MainAxisAlignment, IconButton, Row
from design import color_variables

username_container = {'username':'Player1'}
username_field = ft.TextField(label='Username')
def update_colors():
    global mainc,white, red, black, green
    mainc, white, red, black, green = color_variables()
def profile_page_view(page: Page):
    update_colors()
    def save_username(e):
        global username_container
        username_container['username'] = username_field.value

    return View(
        route='/profile_page',
        controls=[
            AppBar(title= Text('ACCOUNT PAGE'), bgcolor=mainc,
                   actions=[
                            Row([
                                IconButton(
                                    icon = ft.icons.SETTINGS,
                                    icon_color='white',
                                    on_click=lambda _: page.go('/settings_page')
                                ),
                                IconButton(
                                    icon = ft.icons.ACCOUNT_CIRCLE,
                                    icon_color='white',
                                    on_click=lambda _: page.go('/profile_page')
                                )
                            ])
                        ]),
            Text(value='ACCOUNT PAGE', size=30),
            username_field,
            ElevatedButton(text = 'Save', on_click=save_username,color = mainc),
            ElevatedButton(text='Go Back', on_click=lambda _: page.go('/'), color= mainc)
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=26,
    )
