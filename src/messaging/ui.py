from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from datetime import datetime
import time

console = Console()

messages = []
sysMSG = []
contacts = []

def make_layout() -> Layout:
    layout = Layout(name="base")
    layout.split_column(
        Layout(name="header", size=1),
        Layout(name="main", ratio=8),
        Layout(name="system", ratio=3)
    )

    layout["main"].split_row(
        Layout(name="messages", ratio=3),
        Layout(name="contacts", size=30)
    )

    return layout


def send_message(sender, msg, color):
    messages.append((sender, msg, color))

def send_SYS_message(msg):
    sysMSG.append(("SYSTEM", msg, "red"))


def render_message(sender, msg, color):
    timestamp = datetime.now().strftime("%H:%M")
    text = Text(f"[{timestamp}] {sender}: ", style=f"bold {color}")
    text.append(msg, style=color)
    return text

def main_ui():
    layout = make_layout()

    with Live(layout, refresh_per_second=10, screen=True):
        while True:
            #header
            header_text = Text("MoboP2P — Secure Terminal Messenger", style="bold green")
            layout["header"].update(header_text)

            # chat messages
            msg_panel = Panel(
                Text("\n").join([render_message(s, m, c) for s, m, c in messages]),
                title="Chat Feed",
            )
            layout["messages"].update(msg_panel)

            # system messages
            sys_panel = Panel(
                Text("\n").join([render_message(s, m, c) for s, m, c in sysMSG]),
                title="System Feed",
            )
            layout["system"].update(sys_panel)


            # contacts
            contact_text = Text()
            for name, status in contacts:
                color = "green" if status == "online" else "red"
                contact_text.append(f"● {name}\n", style=color)
            layout["contacts"].update(Panel(contact_text, title="Contacts"))

            time.sleep(0.1)
