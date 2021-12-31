# Python script to control fuel transfer and cleaning between tanks
from guizero import App, Drawing
from PID import CreatePID
from data import CreateData
from fsio import fsIO


class FuelSystem:
    def __init__(self, fsApp):
        self.refresh = 250  # msec
        self.tankSize = 200  # L

        self.portLevel = 50  # L
        self.stbdLevel = 150  # L

        self.app = fsApp

        self.io = fsIO(self)

        self.canvas = Drawing(self.app, 1024, 325)
        self.canvas.bg = "grey20"

        self.pid = CreatePID(self)
        self.canvas.repeat(self.refresh, self.pid.flasher)

        self.data = CreateData(self)

    def getPortPercent(self):
        return self.portLevel / self.tankSize * 100

    def getStbdPercent(self):
        return self.stbdLevel / self.tankSize * 100


if __name__ == '__main__':
    app = App(title='Fuel Tank Control', width=1024, height=600)
    fs = FuelSystem(app)
    app.display()

# TODO
# - check for hh/ll tank limits and shutdown with alarm
# - check for filter alarm and shutdown
# - add stop button
# - make valve's hit targets and turn on/off
# - publish/lookup host name??
# - start pigpiod at Pi boot
# - Pi is running Python 3.7 or 3.8, not 3.10?

