from flet import *

def main(page: Page):
    page.bgcolor(colors.GREEN_900)
    page.add(Text("Success"))

app(main, view = WEB_BROWSER)