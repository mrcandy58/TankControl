from valve import Valve
from pump import Pump
from filter import Filter


class CreatePID:
    def __init__(self, fs):
        self.fs = fs
        self.flash = False

        self.portTank = self.fs.canvas.rectangle(100, 100, 199, 299, outline=True, outline_color="grey")
        self.stbdTank = self.fs.canvas.rectangle(800, 100, 899, 299, outline=True, outline_color="gray")

        self.returnLine = self.fs.canvas.line(125, 75, 875, 75, color="gray", width=3)
        self.portReturn = self.fs.canvas.line(125, 75, 125, 115, color="gray", width=3)
        self.stbdReturn = self.fs.canvas.line(875, 75, 875, 115, color="gray", width=3)
        self.suctionLine = self.fs.canvas.line(175, 290, 825, 290, color="gray", width=3)

        self.pumpSuctionLine = self.fs.canvas.line(300, 290, 300, 180, color="grey", width=3)
        self.pumpLine = self.fs.canvas.line(300, 180, 700, 180, color="grey", width=3)
        self.pumpDischargeLine = self.fs.canvas.line(700, 180, 700, 75, color="grey", width=3)

        self.portSuctionValve = Valve(self.fs, 250, 290, "port suction")
        self.stbdSuctionValve = Valve(self.fs, 750, 290, "stbd suction")
        self.portSuctionValve.set_partner(self.stbdSuctionValve)
        self.stbdSuctionValve.set_partner(self.portSuctionValve)

        self.portDischargeValve = Valve(self.fs, 250, 75, "port discharge")
        self.stbdDischargeValve = Valve(self.fs, 750, 75, "stbd discharge")
        self.portDischargeValve.set_partner(self.stbdDischargeValve)
        self.stbdDischargeValve.set_partner(self.portDischargeValve)

        self.filter = Filter(self.fs, 400, 180)
        self.pump = Pump(self.fs, 600, 180)

        self.portFuel = self.fs.canvas.rectangle(101, 101, 198, 298, outline=False, color="deepskyblue")
        self.stbdFuel = self.fs.canvas.rectangle(801, 101, 898, 298, outline=False, color="deepskyblue")

        self.fs.canvas.when_clicked = self.clicked

    def flasher(self):
        self.flash = not self.flash
        self.updatePID()

    def clicked(self, event):
        if self.pump.isPumpHit(event.x, event.y):
            if self.pump.alarm:
                self.pump.alarm = False
                print("alarm off")
                self.updatePID()
            else:
                self.pump.toggle()

    def isPathOpen(self):
        if (self.portSuctionValve.state or self.stbdSuctionValve.state) and\
                (self.portDischargeValve.state or self.stbdDischargeValve.state):
            return True
        else:
            return False

    def updatePID(self):
        # The following is only for testing, needs to be removed
        self.updateTanks()

        if self.fs.data is not None:
            self.fs.data.updateData()

        if self.pump.alarm:  # Alarm
            if self.flash:
                color = "yellow"
            else:
                color = "grey"
        elif self.pump.permissive:
            if self.pump.state:
                color = "green2"  # Running
            else:
                color = "red"  # Permitted to start
        else:
            if self.pump.state:
                color = "purple"  # Error
                print("Got error state")
            else:
                color = "grey"  # Not ready

        self.fs.canvas.tk.itemconfigure(self.pump.shell, outline=color)
        self.fs.canvas.tk.itemconfigure(self.pump.impeller, outline=color)

        x0, y0, x1, y1 = self.fs.canvas.tk.coords(self.portTank)
        x0 += 1
        y0 += 1
        y0 = y0 + ((y1 - y0) * (100 - self.fs.getPortPercent()) / 100)
        self.fs.canvas.tk.coords(self.portFuel, x0, y0, x1, y1)

        x0, y0, x1, y1 = self.fs.canvas.tk.coords(self.stbdTank)
        x0 += 1
        y0 += 1
        y0 = y0 + ((y1 - y0) * (100 - self.fs.getStbdPercent()) / 100)
        self.fs.canvas.tk.coords(self.stbdFuel, x0, y0, x1, y1)

    def updateTanks(self):
        if self.pump.state:
            if self.portSuctionValve.state:
                self.fs.portLevel = self.fs.portLevel - self.fs.flowrate / 60 * self.fs.refresh / 1000
            if self.stbdSuctionValve.state:
                self.fs.stbdLevel = self.fs.stbdLevel - self.fs.flowrate / 60 * self.fs.refresh / 1000
            if self.portDischargeValve.state:
                self.fs.portLevel = self.fs.portLevel + self.fs.flowrate / 60 * self.fs.refresh / 1000
            if self.stbdDischargeValve.state:
                self.fs.stbdLevel = self.fs.stbdLevel + self.fs.flowrate / 60 * self.fs.refresh / 1000

    def allValvesClose(self):
        if self.portSuctionValve.state:
            self.portSuctionValve.close()
        if self.stbdSuctionValve.state:
            self.stbdSuctionValve.close()
        if self.portDischargeValve.state:
            self.portDischargeValve.close()
        if self.stbdDischargeValve.state:
            self.stbdDischargeValve.close()
