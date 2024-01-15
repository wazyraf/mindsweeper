# play_page.py
import flet as ft
from flet import View, Page, AppBar, Text, Column, UserControl, Row, Container, border,IconButton
from flet import CrossAxisAlignment, MainAxisAlignment
import time
import random
import threading
from design import color_variables, current_theme
from pages.settings_page import sound_state
from pages.settings_page import sound_val
from pages.profile_page import username_container
mainc, white, red, black, green = color_variables()
url_wrong_ans = "sounds/wrong.mp3"
url_lose = "sounds/sad.mp3"
url_correct = "sounds/correct.mp3"
url_music = "sounds/rizz monkey.mp3"
last_grid_instance = None

class ReleaseMode:
    def __init__(self, value):
        self.value = value
        pass

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

    def update_colors(self):
        global mainc,white, red, black, green
        mainc, white, red, black, green = color_variables()
    
    def generate_grid(self):
        self.update_colors()
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

        colors = [black, mainc]
        
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
        self.update_colors()
        for row in grid.controls:
            for container in row.controls:
                container.on_click = lambda e: self.show_color(e)
                if container.bgcolor == mainc:
                    container.bgcolor = black
        grid.update()

    def clear_failed_message(self):
            self.failed_message.value = ''
            self.failed_message.update()
        
    def sound_effect_wrong(self):
        audio_effect = ft.Audio(src = url_wrong_ans, autoplay=True, volume = 0.2)
        self.page.overlay.append(audio_effect)
    
    def sound_effect_lose(self):
        print("Playing lose sound")
        audio_effect = ft.Audio(src = url_lose, autoplay = True, volume = 0.1)
        self.page.overlay.append(audio_effect)
    
    def sound_correct(self):
        audio_effect = ft.Audio(src = url_correct, autoplay = True, volume = 0.75)
        self.page.overlay.append(audio_effect)


    def show_color(self, e):
        if e.control.data == mainc:
            sound_state = sound_val()
            if sound_state:
                self.sound_correct()
            e.control.bgcolor = mainc
            e.control.opacity = 1
            e.control.on_click = None
            e.control.update()
            self.blue_tiles -= 1
            self.correct += 1
            e.page.update()
        else: 
            self.incorrect += 1
            sound_state = sound_val()
            if self.incorrect != 3 and sound_state:
                self.sound_effect_wrong()
            e.control.bgcolor = red
            e.control.opacity = 1
            e.control.on_click = None
            e.control.update()
            if self.incorrect == 3 and sound_state:
                self.sound_effect_lose()
            e.page.update()      
        if self.incorrect == 3:
            self.failed_message.value = "Three squares selected wrong, resetting stage"
            self.failed_message.update()
            threading.Timer(1.5, self.clear_failed_message).start()
            self.incorrect = 0
            self.stage = 1
            self.difficulty = 2
            time.sleep(1)
            self.rebuild_grid()
            self.grid.update()
            self.failed_stage_change(self.stage)
            e.page.update()
        
        if self.blue_tiles == 0:
            time.sleep(1)
            self.incorrect = 0
            self.difficulty += 1
            self.stage += 1
            self.rebuild_grid() 
            self.grid.update()
            if self.on_stage_change:
                self.on_stage_change(self.stage)


def play_page_view(page: Page):
    sound_state = sound_val()
    audio = ft.Audio(src=url_music, autoplay=True, volume=0.08, release_mode=ReleaseMode("loop"))
    if sound_state:
        page.overlay.append(audio)

    stage_message = Text(value = '', size=20, color=green) #textul pentru mesajul de succes
    
    def on_stage_change(new_stage):
        stage_text.value = f'Level: {new_stage}'
        stage_text.update()
        blue_tiles_text.value = f'{tile_color} Tiles: {grid_instance.blue_tiles}'
        blue_tiles_text.update()
        stage_message.value = f"Congrats {username_container['username']}, preparing the next level"   #mesajul in sine
        stage_message.update()  #refresh-ul mesajului
        threading.Timer(1.5, clear_stage_message).start() #pentru pastrarea mesajului de succes doar pentru 3 secunde

    def failed_stage_change(new_stage):
        stage_text.value = f'Level: {new_stage}'
        stage_text.update()
        blue_tiles_text.value = f'{tile_color} Tiles: {grid_instance.blue_tiles}'
        blue_tiles_text.update()
        threading.Timer(1.5, clear_stage_message).start() #pentru pastrarea mesajului de succes doar pentru 3 secunde

    def clear_stage_message():
        stage_message.value=''
        stage_message.update()
    
    grid_instance = GenerateGrid(2)
    grid_instance.on_stage_change = on_stage_change
    grid_instance.failed_stage_change = failed_stage_change
    
    if mainc == '#4A7DFF':
        tile_color = "Blue"
    if mainc == green:
        tile_color = "Green"
    if mainc == '#6050dc':
        tile_color = "Majorelle Purple"
    if mainc == '#c5b358':
        tile_color = "Vegas Gold"

    stage_text = Text(value=f'Level: {grid_instance.stage}', size=20) #pentru refresh
    stage_text = Text(value=f'Level: {grid_instance.stage}', size=20) #pentru prima aparitie
    
    blue_tiles_text = Text(value=f'{tile_color} Tiles: {grid_instance.blue_tiles}',size=30)
    
    def settings_leave():
        audio.volume = 0
        page.go('/settings_page')

    def profile_leave():
        audio.volume = 0
        page.go('/profile_page')
    def on_back_arrow_click():
        audio.volume = 0
        page.go('/')

    return View(
        route='/play_page',
        controls=[
            AppBar(title=Text('MINDSWEEPER'), 
                   bgcolor=mainc, 
                   center_title = True,
                   leading=ft.IconButton(
                       icon = ft.icons.ARROW_BACK,
                       icon_color=white,
                       on_click=lambda _: on_back_arrow_click()
                   ),
                   actions=[
                            
                            Row([
                                IconButton(
                                    icon = ft.icons.SETTINGS,
                                    icon_color=white,
                                    on_click=lambda _: settings_leave()
                                ),
                                IconButton(
                                    icon = ft.icons.ACCOUNT_CIRCLE,
                                    icon_color=white,
                                    on_click=lambda _: profile_leave()
                                )
                            ])   
                        ]),
            Container(height = 30),
            blue_tiles_text,
            grid_instance,
            stage_text,
            grid_instance.failed_message,
            stage_message #control pentru stage_message
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )
