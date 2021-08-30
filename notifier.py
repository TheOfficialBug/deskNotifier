import time
from plyer import notification

while True:
    if __name__ == "__main__":
        notification.notify(
            title = "TITLE",
            message = "Enter the message that has to be displayed",
            app_icon = "Enter the path of the app icon",
            app_name = "App Name",
            ticker = "Ticker Message",
            timeout = 15,
        )
    time.sleep(86400)   # to receive notification once in 24hrs

	#pythonw.exe .\notifier.py -> To keep th code running even after the terminal is closed.
