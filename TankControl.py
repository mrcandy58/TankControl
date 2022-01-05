# Python script to control fuel transfer and cleaning between tanks
from guizero import App, Drawing

from PID import CreatePID
from data import CreateData
from fsio import fsIO


class FuelSystem:
    def __init__(self, fsApp):
        self.halt = False
        self.refresh = 250  # msec
        self.app = fsApp
        self.io = fsIO(self)
        self.canvas = Drawing(self.app, 1024, 325)
        self.canvas.bg = "grey20"
        self.pid = CreatePID(self)

        # TODO - for testing only
        self.pid.portTank.setLevel(100.0)  # Liters
        self.pid.stbdTank.setLevel(180.0)  # Liters

        self.data = CreateData(self)

    def on_closing(self):
        print("===================\nSystem shutting down")
        self.app.cancel(self.pid.flasher)
        self.halt = True

        self.pid.pump.stop()
        self.pid.allValvesClose()

        print("Killing")
        exit(0)


def main():
    app = App(title='Fuel Tank Control', width=1024, height=600)
    fs = FuelSystem(app)
    app.when_closed = fs.on_closing
    app.repeat(fs.refresh, fs.pid.flasher)
    app.display()


if __name__ == '__main__':
    main()

# TODO
# - Pi is running Python 3.7 or 3.8, not 3.10?
