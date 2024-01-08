# play_page.py
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from flet import Column, UserControl, Row, Container, border
import time
import random

last_grid_instance = None
class GenerateGrid(UserControl):
    def __init__(self, difficulty):
        self.grid = Column(opacity=1, animate_opacity=300)
        self.blue_tiles: int = 0
        self.difficulty: int = difficulty
        self.correct: int = 0
        self.incorrect: int = 0
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
                        on_click= lambda e: self.show_color(e),
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

    def rebuild_grid(self):
        self.blue_tiles = 0
        self.generate_grid()

    def build(self):
        return self.grid
    
    def show_color(self, e):
        if e.control.data == "#4cbbb5":
            e.control.bgcolor = "#5c443b"
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
            self.rebuild_grid() 
            self.grid.update()

def play_page_view(page: Page):
    grid_instance = GenerateGrid(2)
    #def on_start_button_click(e):

        #print("Start button clicked!")
        #e.source.enabled = False
        #new_grid_instance = GenerateGrid(2)  #creeaza o noua instanta a grid-ului 
        #new_view = play_page_view(page)  # creaza un nou view cu noul grid
        #new_view.controls[2] = new_grid_instance  # inlocuieste grid-ul existent cu cel nou
        #page.views[-1] = new_view  # inlocuieste ce se vede(view vechi cu cel nou)
        
        #page.update()


    return View(
        route='/play_page',
        controls=[
            AppBar(title=Text('PLAY PAGE'), bgcolor='blue'),
            Text(value='PLAY PAGE', size=30),
            grid_instance,
            #ElevatedButton(text='Start', on_click=on_start_button_click),
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )
