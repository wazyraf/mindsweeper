# play_page.py
import flet as ft
from flet import View, Page, AppBar, Text, Column, UserControl, Row, Container, border,IconButton
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

        #variables for colors

        colors = ["#4C4E52", "blue"]

        for row in rows:
            for container in row.controls:
                container.bgcolor = random.choices(colors, weights=[10, self.difficulty])[0]
                container.data = container.bgcolor
                if container.bgcolor == "blue":
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
                if container.bgcolor == "blue":
                    container.bgcolor = "#4C4E52"
        grid.update()

    def show_color(self, e):
        if e.control.data == "blue":
            e.control.bgcolor = "blue"
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
    stage_message = Text(value = '', size=20, color='green') #textul pentru mesajul de succes
    def on_stage_change(new_stage):
        stage_text.value = f'Stage: {new_stage}'
        stage_text.update()
        stage_message.value = "Congrats, preparing the next level"   #mesajul in sine
        stage_message.update()  #refresh-ul mesajului
        threading.Timer(1.5, clear_stage_message).start() #pentru pastrarea mesajului de succes doar pentru 3 secunde

    def clear_stage_message():
        stage_message.value=''
        stage_message.update()

    grid_instance = GenerateGrid(2)
    grid_instance.on_stage_change = on_stage_change

    stage_text = Text(value=f'Level: {grid_instance.stage}', size=20) #pentru refresh
    stage_text = Text(value=f'Level: {grid_instance.stage}', size=20) #pentru prima aparitie
    
    return View(
        route='/play_page',
        controls=[
            AppBar(title=Text('PLAY PAGE'), bgcolor='blue',
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
                                    on_click=lambda _: page.go('/account_page')
                                )
                            ])
                        ]),
            Text(value='PLAY PAGE', size=30),
            grid_instance,
            stage_text,
            stage_message #control pentru stage_message
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )
