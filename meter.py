class Meter:
    def __init__(self, fs, x, y, name):
        self.filterK = 4.0
        self.bypass = 3.0  # Seconds
        self.fs = fs
        self.x = x
        self.y = y
        self.name = name
        self.alarm = False
        self.startupBypass = 0
        self.flowrate = 0.0
        self.filter = 0.0

        self.shell = self.fs.canvas.rectangle(self.x - 10, self.y - 30, self.x + 10, self.y + 30,
                                              color="grey20", outline=3, outline_color="gray")
        self.imp_top = self.fs.canvas.oval(self.x - 6, self.y - 25, self.x + 6, self.y,
                                           color="gray20", outline=3, outline_color="gray")
        self.imp_btm = self.fs.canvas.oval(self.x - 6, self.y + 25, self.x + 6, self.y,
                                           color="gray20", outline=3, outline_color="gray")
        self.flowRateStr = self.fs.canvas.text(self.x + 30, self.y + 10, self.flowrate,
                                               color="white", size=20)

    def isMeterHit(self, x, y):
        return self.x - 10 <= x <= self.x + 10 and \
               self.y - 30 <= y <= self.y + 30

    def updateFlowrate(self, i_flow):
        self.flowrate = (i_flow + self.flowrate * self.filter) / (self.filter + 1.0)
        if self.fs.halt is not True:
            self.fs.canvas.tk.itemconfigure(self.flowRateStr,
                                            text="{:3.1f} L/m".format(self.flowrate))

    def startBypassTimer(self):
        self.startupBypass = self.bypass * 1000.0

    def checkMinFlow(self):
        if self.startupBypass > 0:
            self.startupBypass -= self.fs.refresh
            if self.startupBypass <= 0:
                self.startupBypass = 0
        elif self.flowrate < 3.0 and self.fs.pid.pump.state is True:
            self.alarm = True
            self.fs.pid.pump.stop()
