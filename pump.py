class Pump:
    def __init__(self, fs, x, y, name, state=False, size=40):
        self.fs = fs
        self.x = x
        self.y = y
        self.name = name
        self.state = state
        self.size = size
        self.permissive = False
        self.alarm = False

        self.shell = self.fs.canvas.oval(self.x - self.size, self.y - self.size,
                                         self.x + self.size, self.y + self.size,
                                         color="grey20",
                                         outline=5, outline_color="gray", )
        self.impeller = self.fs.canvas.triangle(self.x - self.size / 3, self.y - self.size / 2,
                                                self.x - self.size / 3, self.y + self.size / 2,
                                                self.x + self.size / 2, self.y,
                                                color="grey20",
                                                outline=3, outline_color="gray", )

    def toggle(self):
        if self.state:
            self.stop()
        else:
            self.run()

    def run(self):
        if not self.state and not self.alarm and self.permissive \
                and self.fs.pid.filter.permissive \
                and self.fs.pid.stbdTank.permissive and self.fs.pid.portTank.permissive:
            self.state = True
            self.fs.pid.meter.filter = 4.0  # Add some averaging into the meter flowrate
            self.fs.io.pumpStart(self.name)
            self.fs.pid.meter.startBypassTimer()

    def stop(self):
        if self.state:
            self.state = False
            self.fs.pid.meter.filter = 0.0  # Remove averaging from meter flowrate
            self.fs.pid.meter.startupBypass = 0
            self.fs.io.pumpStop(self.name)

    def setPermissive(self, perm):
        self.permissive = perm
        if not perm and self.state:
            self.stop()
            self.alarm = True

    def isPumpHit(self, x, y):
        return self.x - self.size <= x <= self.x + self.size and \
               self.y - self.size <= y <= self.y + self.size
