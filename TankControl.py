# Python script to control fuel transfer and cleaning between tanks
from guizero import App, Drawing
from PID import CreatePID
from data import CreateData


class FuelSystem:
    def __init__(self):
        self.refresh = 50      # msec
        self.tankSize = 200     # L

        self.flowrate = 0       # L/m
        self.portLevel = 50     # L
        self.stbdLevel = 150    # L

    def getPortPercent(self):
        return self.portLevel/self.tankSize*100

    def getStbdPercent(self):
        return self.stbdLevel/self.tankSize*100


if __name__ == '__main__':

    app = App(title='Fuel Tank Control', width=1024, height=600)
    fs = FuelSystem()

    canvas = Drawing(app, 1024, 325)
    canvas.bg = "grey20"

    pid = CreatePID(canvas, fs)
    canvas.repeat(fs.refresh, pid.flasher)

    data = CreateData(app, pid)
    pid.data = data

    app.display()
