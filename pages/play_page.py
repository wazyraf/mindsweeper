# play_page.py
import flet as ft
from flet import View, Page, AppBar, Text, Column, UserControl, Row, Container, border,IconButton
from flet import CrossAxisAlignment, MainAxisAlignment
import time
import random
import threading
from design import color_variables
from pages.profile_page import username_container
mainc, white, red, black, green = color_variables()

last_grid_instance = None
class GenerateGrid(UserControl):
    def __init__(self, difficulty):
        self.grid = Column(opacity=1, animate_opacity=300)
        self.blue_tiles: int = 0
        self.difficulty: int = difficulty
        self.correct: int = 0
        self.incorrect: int = 0
        self.stage: int = 1
        self.failed_message = Text(value = '', size=20, color=red)
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
                        border=border.all(1, white),
                        on_click= None,
                    )
                    for _ in range(5)
                ],
            )
            for _ in range(5)
        ]

        colors = [black, mainc] #prima pentru patratele goale si a doua pentru cele colorate

        for row in rows:
            for container in row.controls:
                container.bgcolor = random.choices(colors, weights=[10, self.difficulty])[0]
                container.data = container.bgcolor
                if container.bgcolor == mainc:
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
                if container.bgcolor == mainc:
                    container.bgcolor = black
        grid.update()

    def clear_failed_message(self):
            self.failed_message.value = ''
            self.failed_message.update()

    def show_color(self, e):
        if e.control.data == mainc:
            e.control.bgcolor = mainc
            e.control.opacity = 1
            e.control.on_click = None
            e.control.update()
            self.blue_tiles -= 1
            self.correct += 1
            e.page.update()
        else:
            e.control.bgcolor = red
            e.control.opacity = 1
            e.control.on_click = None
            e.control.update()
            self.incorrect += 1
            e.page.update()
        
        if self.incorrect == 3:
            self.failed_message.value = "Three squares selected wrong, resetting stage",
            self.failed_message.update()
            threading.Timer(1.5, self.clear_failed_message).start()
            self.incorrect = 0
            self.stage = 1
            self.difficulty = 2
            time.sleep(1)
            self.rebuild_grid()
            self.grid.update()
            self.failed_stage_change(self.stage)
        
        if self.blue_tiles == 0:
            time.sleep(1)
            self.difficulty += 1
            self.stage += 1
            self.rebuild_grid() 
            self.grid.update()
            if self.on_stage_change:
                self.on_stage_change(self.stage)


def play_page_view(page: Page):
    stage_message = Text(value = '', size=20, color=green) #textul pentru mesajul de succes
    def on_stage_change(new_stage):
        stage_text.value = f'Level: {new_stage}'
        stage_text.update()
        stage_message.value = f"Congrats {username_container['username']}, preparing the next level"   #mesajul in sine
        stage_message.update()  #refresh-ul mesajului
        threading.Timer(1.5, clear_stage_message).start() #pentru pastrarea mesajului de succes doar pentru 3 secunde

    def failed_stage_change(new_stage):
        stage_text.value = f'Level: {new_stage}'
        stage_text.update()
        threading.Timer(1.5, clear_stage_message).start() #pentru pastrarea mesajului de succes doar pentru 3 secunde

    def clear_stage_message():
        stage_message.value=''
        stage_message.update()

    grid_instance = GenerateGrid(2)
    grid_instance.on_stage_change = on_stage_change
    grid_instance.failed_stage_change = failed_stage_change

    stage_text = Text(value=f'Level: {grid_instance.stage}', size=20) #pentru refresh
    stage_text = Text(value=f'Level: {grid_instance.stage}', size=20) #pentru prima aparitie
    
    return View(
        route='/play_page',
        controls=[
            AppBar(title=Text('MINDSWEEPER'), 
                   bgcolor=mainc, 
                   center_title = True,
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
                        ]),
            Text(value='DIFFICULTY: ', size=30),
            grid_instance,
            stage_text,
            grid_instance.failed_message,
            stage_message #control pentru stage_message
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )
