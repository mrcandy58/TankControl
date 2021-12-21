from valve import Valve
from pump import Pump
from filter import Filter


class CreatePID:
    def __init__(self, cnv):
        self.canvas = cnv

        portTank = self.canvas.rectangle(100, 100, 199, 299, outline=True, outline_color="grey")
        stbdTank = self.canvas.rectangle(800, 100, 899, 299, outline=True, outline_color="gray")

        returnLine = self.canvas.line(125, 75, 875, 75, color="gray", width=3)
        portReturn = self.canvas.line(125, 75, 125, 115, color="gray", width=3)
        stbdReturn = self.canvas.line(875, 75, 875, 115, color="gray", width=3)
        suctionLine = self.canvas.line(175, 290, 825, 290, color="gray", width=3)

        pumpSuctionLine = self.canvas.line(300, 290, 300, 180, color="grey", width=3)
        pumpLine = self.canvas.line(300, 180, 700, 180, color="grey", width=3)
        pumpDischargeLine = self.canvas.line(700, 180, 700, 75, color="grey", width=3)

        self.portSuctionValve = Valve(self.canvas, 250, 290)
        self.stbdSuctionValve = Valve(self.canvas, 750, 290)
        self.portSuctionValve.set_partner(self.stbdSuctionValve)
        self.stbdSuctionValve.set_partner(self.portSuctionValve)

        self.portDischargeValve = Valve(self.canvas, 250, 75)
        self.stbdDischargeValve = Valve(self.canvas, 750, 75)
        self.portDischargeValve.set_partner(self.stbdDischargeValve)
        self.stbdDischargeValve.set_partner(self.portDischargeValve)

        self.filter = Filter(self.canvas, 400, 180)
        self.pump = Pump(self.canvas, 600, 180)