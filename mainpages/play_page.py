#play_page.py
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from flet import Column, UserControl, Row, Container, border

class GenerateGrid(UserControl):
    def __init__(self):
        #variabilele mai tarziu
        self.grid = Column(opacity=1, animate_opacity=300)
        super().__init__()
    def build(self):
        rows: list=[
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=54,
                        height=54,
                        animate=300,
                        border=border.all(1,'white'),
                        on_click= None #schimbam imediat
                    )
                    for _ in range(5)
                ],
            )
            for _ in range(5)
        ]
        self.grid.controls = rows
        return self.grid

        pass

def play_page_view(page: Page):
    return View(
        route='/play_page',
        controls=[
            AppBar(title= Text('PLAY PAGE'), bgcolor='blue'),
            Text(value='PLAY PAGE', size=30),
            GenerateGrid(),
            ElevatedButton(text='Go Back', on_click=lambda _: page.go('/'))
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=26
    )