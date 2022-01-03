class Filter:
    def __init__(self, fs, x, y, name, state=True, size=40, offset=20):
        self.x = x
        self.y = y
        self.fs = fs
        self.name = name
        self.state = state
        self.size = size
        self.offset = offset
        self.permissive = False
        self.alarm = False

        self.shell1 = self.fs.canvas.oval(self.x - self.size / 2, self.y - self.size + self.offset,
                                          self.x + self.size / 2, self.y + self.size + self.offset,
                                          color="grey20",
                                          outline=5, outline_color="gray")
        self.shell2 = self.fs.canvas.rectangle(self.x - self.size / 2, self.y + self.offset,
                                               self.x + self.size / 2, self.y - self.size + self.offset,
                                               color="grey20",
                                               outline=5, outline_color="gray")

    def clear(self):
        self.state = True
        if not self.alarm:
            self.permissive = True

    def plugged(self):
        self.state = False
        if self.fs.pid.pump.state:
            self.alarm = True
            self.fs.pid.pump.stop()
        self.permissive = False

    def isFilterHit(self, x, y):
        return self.x - self.size <= x <= self.x + self.size and \
               self.y - self.size <= y <= self.y + self.size
