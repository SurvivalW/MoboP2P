#TEXTUAL
from textual.app import App
from textual.scroll_view import ScrollView
from textual.widgets import Input
from textual.widgets import Button
from textual.widgets import RichLog
from textual.containers import Vertical, Horizontal, Grid
#DATETIME
from datetime import datetime
#RICH
from rich.text import Text
#ASYNCIO
import asyncio


#===========MAIN===========
class MoboP2P(App):

    CSS_PATH = "messaging/style.css"

    def compose(self):
        with Vertical():
            with Horizontal():#top
                with Vertical(id="chat_container"):#chat
                    yield RichLog(id="chatLog")
                    yield Input(id="input")
                with Vertical(id="contacts_container"):#contacts view and buttons
                    yield ScrollView(id="contacts")
                    with Horizontal(id="buttons_container"):#button container
                        yield Button(id="add")
                        yield Button(id="remove")
            yield RichLog(id="systemMessages")#bottom


    def on_mount(self):
        self.sysms_view = self.query_one("#systemMessages", RichLog)
        self.sysms_view.clear()
        self.send_SYS_message("[bold red]MoboP2P started...[/bold red]")#start up msg

        self.chat_view = self.query_one("#chatLog", RichLog)
        self.chat_view.clear()


    def send_SYS_message(self, msg: str):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        styled_text = Text.from_markup(f"[dim]{timestamp}[/dim] {msg}")
        self.sysms_view.write(styled_text)

#Booted up
def main():
    MoboP2P().run()

if __name__ == "__main__":
    main()
