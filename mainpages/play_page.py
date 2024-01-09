# play_page.py
from flet import View, Page, AppBar, Text, Column, UserControl, Row, Container, border
from flet import CrossAxisAlignment, MainAxisAlignment
import time
import random
import threading

last_grid_instance = None
class GenerateGrid(UserControl):
    def __init__(self, difficulty):
        self.grid = Column(opacity=1, animate_opacity=300)
        self.blue_tiles: int = 0
        self.difficulty: int = difficulty
        self.correct: int = 0
        self.incorrect: int = 0
        self.stage: int = 1
        super().__init__()
        self.generate_grid()

    def generate_grid(self):
        rows = [
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=54,
                        height=54,
                        animate=300,
                        border=border.all(1, 'white'),
                        on_click= None,
                    )
                    for _ in range(5)
                ],
            )
            for _ in range(5)
        ]

        colors = ["#5c443b", "#4cbbb5"]

        for row in rows:
            for container in row.controls:
                container.bgcolor = random.choices(colors, weights=[10, self.difficulty])[0]
                container.data = container.bgcolor
                if container.bgcolor == "#4cbbb5":
                    self.blue_tiles += 1


        self.grid.controls = rows  
        threading.Timer(1.5, self.delete_grid, args=(self.grid,)).start()
 


    def rebuild_grid(self):
        self.blue_tiles = 0
        self.generate_grid()

    def build(self):
        return self.grid

    def delete_grid(self, grid):
        for row in grid.controls:
            for container in row.controls:
                container.on_click = lambda e: self.show_color(e)
                if container.bgcolor == "#4cbbb5":
                    container.bgcolor = "#5c443b"
        grid.update()

    def show_color(self, e):
        if e.control.data == "#4cbbb5":
            e.control.bgcolor = "#4cbbb5"
            e.control.opacity = 1
            e.control.on_click = None
            e.control.update()
            self.blue_tiles -= 1
            self.correct += 1
            e.page.update()
        else:
            e.control.bgcolor = "red"
            e.control.opacity = 1
            e.control.on_click = None
            e.control.update()
            self.incorrect += 1
            e.page.update()
        
        if self.blue_tiles == 0:
            time.sleep(1)
            self.difficulty += 1
            self.stage += 1
            self.rebuild_grid() 
            self.grid.update()
            if self.on_stage_change:
                self.on_stage_change(self.stage)


def play_page_view(page: Page):
    def on_stage_change(new_stage):
        stage_text.value = f'Stage: {new_stage}'
        stage_text.update()

    grid_instance = GenerateGrid(2)
    grid_instance.on_stage_change = on_stage_change

    stage_text = Text(value=f'Stage: {grid_instance.stage}', size=20)
    stage_text = Text(value=f'Stage: {grid_instance.stage}', size=20)
    
    return View(
        route='/play_page',
        controls=[
            AppBar(title=Text('PLAY PAGE'), bgcolor='blue'),
            Text(value='PLAY PAGE', size=30),
            grid_instance,
            stage_text,
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )
