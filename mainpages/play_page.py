#play_page.py
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from flet import Column, UserControl, Row, Container, border
import random

class GenerateGrid(UserControl):
    def __init__(self, difficulty):
        #variabilele mai tarziu
        self.grid = Column(opacity=1, animate_opacity=300)
        self.blue_tiles: int = 0
        self.difficulty: int = difficulty
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


        colors: list = ["#5c443b", "#4cbbb5"]

        for row in rows: 
            for container in row.controls[:]:
                container.bgcolor = random.choices(colors, weights = [10, self.difficulty])[0]
                container.data = container.bgcolor
                if container.bgcolor == "#4cbbb5":
                    self.blue_tiles += 1
 
        self.grid.controls = rows
        return self.grid

        pass

    

def play_page_view(page: Page):
    return View(
        route='/play_page',
        controls=[
            AppBar(title= Text('PLAY PAGE'), bgcolor='blue'),
            Text(value='PLAY PAGE', size=30),
            GenerateGrid(2),
            ElevatedButton(text='Start', on_click=lambda _: page.go('/')),
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=26
    )