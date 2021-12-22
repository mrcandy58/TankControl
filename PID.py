from valve import Valve
from pump import Pump
from filter import Filter


class CreatePID:
    def __init__(self, cnv):
        self.canvas = cnv
        self.canvas.bg = "grey20"
        self.flash = False

        self.portTank = self.canvas.rectangle(100, 100, 199, 299, outline=True, outline_color="grey")
        self.stbdTank = self.canvas.rectangle(800, 100, 899, 299, outline=True, outline_color="gray")

        self.returnLine = self.canvas.line(125, 75, 875, 75, color="gray", width=3)
        self.portReturn = self.canvas.line(125, 75, 125, 115, color="gray", width=3)
        self.stbdReturn = self.canvas.line(875, 75, 875, 115, color="gray", width=3)
        self.suctionLine = self.canvas.line(175, 290, 825, 290, color="gray", width=3)

        self.pumpSuctionLine = self.canvas.line(300, 290, 300, 180, color="grey", width=3)
        self.pumpLine = self.canvas.line(300, 180, 700, 180, color="grey", width=3)
        self.pumpDischargeLine = self.canvas.line(700, 180, 700, 75, color="grey", width=3)

        self.portSuctionValve = Valve(self, 250, 290, "port suction")
        self.stbdSuctionValve = Valve(self, 750, 290, "stbd suction")
        self.portSuctionValve.set_partner(self.stbdSuctionValve)
        self.stbdSuctionValve.set_partner(self.portSuctionValve)

        self.portDischargeValve = Valve(self, 250, 75, "port discharge")
        self.stbdDischargeValve = Valve(self, 750, 75, "stbd discharge")
        self.portDischargeValve.set_partner(self.stbdDischargeValve)
        self.stbdDischargeValve.set_partner(self.portDischargeValve)

        self.filter = Filter(self, 400, 180)
        self.pump = Pump(self, 600, 180)

        self.canvas.when_clicked = self.clicked

    def flasher(self):
        self.flash = not self.flash
        if self.pump.alarm:
            self.pump.updatePID()

    def clicked(self, event):
        if self.pump.isPumpHit(event.x, event.y):
            if self.pump.alarm:
                self.pump.alarm = False
                self.pump.updatePID()
            else:
                self.pump.toggle()

    def isPathOpen(self):
        if (self.portSuctionValve.state or self.stbdSuctionValve.state) and\
                (self.portDischargeValve.state or self.stbdDischargeValve.state):
            return True
        else:
            return False
