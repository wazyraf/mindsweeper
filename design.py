current_theme = 'Default Theme'

def on_theme_change(new_theme):
    global current_theme
    current_theme = new_theme

def color_variables():
    mainc='#4A7DFF' #(blue) appbar
    red = 'red'
    black = '#4C4E52'
    white  = 'white'
    green = '#355e3b'
    vegas_gold = '#c5b358'
    blue = '#4A7DFF'
    majorelle = '#6050dc'
    if current_theme == "Green":
        mainc = green
    if current_theme == "Default":
        mainc = blue
    if current_theme == "Vegas Gold":
        mainc = vegas_gold
    if current_theme == "Majorelle":
        mainc = majorelle
    return mainc, white, red, black, green
