class Tank:
    def __init__(self, fs, name, x, y, width, height, suction, discharge):
        self.x = x
        self.y = y
        self.fs = fs
        self.name = name
        self.width = width
        self.height = height
        self.mySuction = suction
        self.myDischarge = discharge
        self.permissive = False
        self.alarm = False
        self._level = 0.0
        self._percent = 0.0

        self.shell = self.fs.canvas.rectangle(self.x, self.y,
                                              self.x + self.width, self.y + self.height,
                                              outline=True, outline_color="gray")

    def checkLevel(self):
        if (self._percent > 95.0 and self.myDischarge.state and not self.mySuction.state) or \
                (self._percent < 5.0 and self.mySuction.state and not self.myDischarge.state):
            if self.fs.pid.pump.state:
                self.alarm = True
                self.fs.pid.pump.stop()
                print("stopped pump: {:s} tank level {:3.1f}%".format(self.name, self._percent))
            self.permissive = False
        else:
            if not self.alarm:
                self.permissive = True

    def isTankHit(self, x, y):
        return self.x <= x <= self.x + self.width and \
               self.y <= y <= self.y + self.height

    # TODO - remove once we get level and percent from N2k
    def setLevel(self, level):
        self._level = level
        self._percent = level / 200.0 * 100.0

    def incLevel(self, amt):
        self.setLevel(self._level + amt)

    def getLevel(self):
        return self._level

    def getPercent(self):
        return self._percent
