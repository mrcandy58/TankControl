# Python script to control fuel transfer and cleaning between tanks
from guizero import App, Drawing
from PID import CreatePID
from data import CreateData
from fsio import fsIO


class FuelSystem:
    def __init__(self, fsApp):
        self.refresh = 250  # msec
        self.tankSize = 200  # L

        self.flowrate = 0  # L/m
        self.portLevel = 50  # L
        self.stbdLevel = 150  # L

        self.app = fsApp

        self.io = fsIO(self)

        self.canvas = Drawing(self.app, 1024, 325)
        self.canvas.bg = "grey20"

        self.pid = CreatePID(self)
        self.canvas.repeat(self.refresh, self.pid.flasher)

        self.data = CreateData(self)

#        self.file_read = io.open("/dev/i2c-" + str(self.bus), "rb", buffering=0)
#        self.file_write = io.open("/dev/i2c-" + str(self.bus), "wb", buffering=0)
#        I2C_SLAVE = 0x703
#        fcntl.ioctl(self.file_read, I2C_SLAVE, self.addr)
#        fcntl.ioctl(self.file_write, I2C_SLAVE, self.addr)

    def getPortPercent(self):
        return self.portLevel / self.tankSize * 100

    def getStbdPercent(self):
        return self.stbdLevel / self.tankSize * 100


if __name__ == '__main__':
    app = App(title='Fuel Tank Control', width=1024, height=600)
    fs = FuelSystem(app)
    app.display()
