# Python script to control fuel transfer and cleaning between tanks
from guizero import App, Drawing
from PID import CreatePID
from data import CreateData
from fsio import fsIO


class FuelSystem:
    def __init__(self, fsApp):
        self.refresh = 250  # msec

        self.app = fsApp

        self.io = fsIO(self)

        self.canvas = Drawing(self.app, 1024, 325)
        self.canvas.bg = "grey20"

        self.pid = CreatePID(self)
        self.pid.portTank.setLevel(100.0)     # Liters
        self.pid.stbdTank.setLevel(180.0)   # Liters
        self.canvas.repeat(self.refresh, self.pid.flasher)

        self.data = CreateData(self)


if __name__ == '__main__':
    app = App(title='Fuel Tank Control', width=1024, height=600)
    fs = FuelSystem(app)
    app.display()

# TODO
# - add stop button
# - make valve's hit targets and turn on/off
# - publish/lookup host name??
# - start pigpiod at Pi boot
# - Pi is running Python 3.7 or 3.8, not 3.10?

