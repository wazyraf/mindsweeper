from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from flet import Image # Import the Image control

def image_page_view(page: Page):
    return View(
        route='/image_page',
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=26,
            controls=[ # Add a list of controls to display on the page
                Image( # Create an Image control
                    src="/images/background.png", # Set the src attribute to the relative path of your image
                    width=200, # Optionally, you can set the width and height of the image
                    height=200
                )
            ]
    )
