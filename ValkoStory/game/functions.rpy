init python:
    def apply_theme(theme):
        preferences.theme = theme
        gui.main_menu_background = im.Scale(f"gui/{preferences.theme}_main_menu.png", 1920, 1080)
        gui.accent_color = red if theme == "red" else green
        gui.rebuild()