from messaging import ui
import threading
import time
import signal
import sys


def signal_handler(sig, frame):
    print("\n[!] MoboP2P shutting down...")
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)

    #ui
    ui_thread = threading.Thread(target=ui.main_ui, daemon=True)
    ui_thread.start()


    #test
    i = 0
    while True:
        ui.send_SYS_message(f"Heartbeat {i}")
        time.sleep(2)
        i += 1


if __name__ == "__main__":
    main()
