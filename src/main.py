#TEXTUAL
from textual.app import App, ComposeResult
from textual.scroll_view import ScrollView
from textual.widgets import Button, RichLog, Input, ListView, ListItem, Label, Static
from textual.containers import Vertical, Horizontal
from textual.screen import ModalScreen
from textual import on
#DATETIME
from datetime import datetime
#RICH
from rich.text import Text
#ASYNCIO
import asyncio

#===========POP UP===========
class NameContactPopup(ModalScreen):


    def compose(self) -> ComposeResult:
        with Vertical(id="popup_container"):
            yield Label("Enter contact name:", id="popup_label")
            yield Input(placeholder="Contact name...", id="contact_name_input")
            with Horizontal(id="popup_buttons"):
                yield Button("Confirm", id="confirm_add")
                yield Button("Cancel", id="cancel_add")

    def on_mount(self) -> None:
        self.styles.width = "50%"
        self.styles.height = "30%"
        self.styles.align = ("center", "middle")
        self.styles.border = ("round", "cyan")
        self.styles.background = "black"


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
                    yield ListView(id="contacts")
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

#===========EVENTS===========

    @on(Button.Pressed, "#add")
    def show_add_popup(self):
        self.push_screen(NameContactPopup())

    @on(Button.Pressed, "#cancel_add")
    def cancel_popup(self):
        self.pop_screen()

    @on(Button.Pressed, "#confirm_add")
    def confirm_add_contact(self):
        popup = self.screen
        input_field = popup.query_one("#contact_name_input", Input)
        name = input_field.value.strip()
        if not name:
            self.send_SYS_message("[yellow]No name entered.[/yellow]")
            return
        self.query_one("#contacts", ListView).append(ListItem(Label(name)))
        self.pop_screen()
        self.send_SYS_message(f"[green]Added contact: [bold]{name}[/bold][/green]")



#Booted up
def main():
    MoboP2P().run()

if __name__ == "__main__":
    main()
