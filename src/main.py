from textual.app import App
from textual.scroll_view import ScrollView
from textual.widgets import Input
from textual.widgets import Button
from textual.containers import Vertical, Horizontal, Grid

class MoboP2P(App):

    CSS_PATH = "messaging/style.css"

    def compose(self):
        with Vertical():
            with Horizontal():#top
                with Vertical(id="chat_container"):#chat
                    yield ScrollView(id="chatLog")
                    yield Input(id="input")
                with Vertical(id="contacts_container"):#contacts view and buttons
                    yield ScrollView(id="contacts")
                    with Horizontal(id="buttons_container"):#button container
                        yield Button(id="add")
                        yield Button(id="remove")
            yield ScrollView(id="systemMessages")#bottom


    def on_mount(self):
        pass


def main():
    MoboP2P().run()

if __name__ == "__main__":
    main()
