from valve import Valve
from pump import Pump
from filter import Filter
from meter import Meter
from tank import Tank


class CreatePID:
    def __init__(self, fs):
        self.fs = fs
        self.flash = False

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

        self.portTank = Tank(self.fs, "port", 100, 100, 99, 199,
                             self.portSuctionValve, self.portDischargeValve)
        self.stbdTank = Tank(self.fs, "stbd", 800, 100, 99, 199,
                             self.stbdSuctionValve, self.stbdDischargeValve)

        self.filter = Filter(self.fs, 400, 180, "primary filter")
        self.pump = Pump(self.fs, 500, 180, "xfer pump")
        self.meter = Meter(self.fs, 600, 180, "fuel flow")

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
                self.updatePID()
            else:
                self.pump.toggle()

        if self.filter.isFilterHit(event.x, event.y):
            if self.filter.alarm:
                self.filter.alarm = False
                self.updatePID()

        if self.portTank.isTankHit(event.x, event.y):
            if self.portTank.alarm:
                self.portTank.alarm = False
                self.updatePID()

        if self.stbdTank.isTankHit(event.x, event.y):
            if self.stbdTank.alarm:
                self.stbdTank.alarm = False
                self.updatePID()

        if self.meter.isMeterHit(event.x, event.y):
            if self.meter.alarm:
                self.meter.alarm = False
                self.updatePID()

        if self.portSuctionValve.isValveHit(event.x, event.y):
            self.portSuctionValve.toggle()

        if self.portDischargeValve.isValveHit(event.x, event.y):
            self.portDischargeValve.toggle()

        if self.stbdSuctionValve.isValveHit(event.x, event.y):
            self.stbdSuctionValve.toggle()

        if self.stbdDischargeValve.isValveHit(event.x, event.y):
            self.stbdDischargeValve.toggle()

    def isPathOpen(self):
        if (self.portSuctionValve.state or self.stbdSuctionValve.state) and \
                (self.portDischargeValve.state or self.stbdDischargeValve.state):
            return True
        else:
            return False

    def updatePID(self):
        # Update all the data
        if self.fs.data is not None:
            self.fs.data.updateData()

        # Check for filter alarm
        if self.filter.alarm:
            if self.flash:
                color = "yellow"
            else:
                color = "grey"
        elif self.filter.state:
            color = "green2"
        else:
            color = "red"

        self.fs.canvas.tk.itemconfigure(self.filter.shell1, outline=color)
        self.fs.canvas.tk.itemconfigure(self.filter.shell2, outline=color)

        # Check for pump alarm
        if self.pump.alarm:
            if self.flash:
                color = "yellow"
            else:
                color = "grey"
        elif self.pump.permissive and self.filter.permissive and self.portTank.permissive and self.stbdTank.permissive:
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

        # Check for meter alarm
        if self.meter.alarm:
            if self.flash:
                color = "yellow"
            else:
                color = "grey"
        else:
            color = "grey"

        self.fs.canvas.tk.itemconfigure(self.meter.shell, outline=color)
        self.fs.canvas.tk.itemconfigure(self.meter.imp_top, outline=color)
        self.fs.canvas.tk.itemconfigure(self.meter.imp_btm, outline=color)

        # Check for tank alarm
        if self.portTank.alarm:
            if self.flash:
                color = "yellow"
            else:
                color = "grey"
        else:
            color = "grey"
        self.fs.canvas.tk.itemconfigure(self.portTank.shell, outline=color)

        if self.stbdTank.alarm:
            if self.flash:
                color = "yellow"
            else:
                color = "grey"
        else:
            color = "grey"
        self.fs.canvas.tk.itemconfigure(self.stbdTank.shell, outline=color)

        # Update contents of the tanks
        x0, y0, x1, y1 = self.fs.canvas.tk.coords(self.portTank.shell)
        x0 += 1
        y0 += 1
        y0 = y0 + ((y1 - y0) * (100 - self.fs.pid.portTank.getPercent()) / 100)
        self.fs.canvas.tk.coords(self.portFuel, x0, y0, x1, y1)

        x0, y0, x1, y1 = self.fs.canvas.tk.coords(self.stbdTank.shell)
        x0 += 1
        y0 += 1
        y0 = y0 + ((y1 - y0) * (100 - self.fs.pid.stbdTank.getPercent()) / 100)
        self.fs.canvas.tk.coords(self.stbdFuel, x0, y0, x1, y1)

    def allValvesClose(self):
        if self.portSuctionValve.state:
            self.portSuctionValve.close()
        if self.stbdSuctionValve.state:
            self.stbdSuctionValve.close()
        if self.portDischargeValve.state:
            self.portDischargeValve.close()
        if self.stbdDischargeValve.state:
            self.stbdDischargeValve.close()
