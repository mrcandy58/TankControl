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
        if self.permissive and not self.alarm:
            self.state = True
            self.fs.io.pumpStart(self.name)
            #  The following is only for testing, needs to be removed
            self.fs.flowrate = 100

    def stop(self):
        if self.state:
            self.state = False
            self.fs.io.pumpStop(self.name)
            #  The following is only for testing, needs to be removed
            self.fs.flowrate = 0

    def setPermissive(self, perm):
        self.permissive = perm
        if not perm and self.state:
            self.stop()
            self.alarm = True
            print("alarm on")

    def isPumpHit(self, x, y):
        return self.x - self.size <= x <= self.x + self.size and \
               self.y - self.size <= y <= self.y + self.size
