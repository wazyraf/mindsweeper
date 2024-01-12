# theme.py
class Theme:
    def __init__(self, name):
        self.name = name
        self.primary_color = None
        self.secondary_color = None
        

light_theme = Theme(name="Light")
light_theme.primary_color = "#3498db"
light_theme.secondary_color = "#2ecc71"
light_theme.text_color = "#333333"
light_theme.background_color = "#ffffff"

dark_theme = Theme(name="Dark")
dark_theme.primary_color = "#2c3e50"
dark_theme.secondary_color = "#e74c3c"
dark_theme.text_color = "#ffffff"
dark_theme.background_color = "#333333"