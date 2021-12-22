class Pump:
    def __init__(self, pid, x, y, state=False, size=40):
        self.x = x
        self.y = y
        self.pid = pid
        self.state = state
        self.size = size
        self.permissive = False
        self.alarm = False

        self.shell = self.pid.canvas.oval(self.x - self.size, self.y - self.size,
                                          self.x + self.size, self.y + self.size,
                                          color="grey20",
                                          outline=5, outline_color="gray", )
        self.impeller = self.pid.canvas.triangle(self.x - self.size / 3, self.y - self.size / 2,
                                                 self.x - self.size / 3, self.y + self.size / 2,
                                                 self.x + self.size / 2, self.y,
                                                 color="grey20",
                                                 outline=3, outline_color="gray", )
        if self.state:
            self.run()
        else:
            self.stop()

    def toggle(self):
        if self.state:
            self.stop()
        else:
            self.run()

    def run(self):
        if self.permissive and not self.alarm:
            self.state = True
            print("pump start")
        self.updatePID()

    def stop(self):
        self.state = False
        print("pump stop")
        self.updatePID()

    def setPermissive(self, perm):
        self.permissive = perm
        if not perm and self.state:
            self.stop()
            self.alarm = True
        self.updatePID()

    def updatePID(self):
        if self.alarm:  # Alarm
            if self.pid.flash:
                color = "yellow"
            else:
                color = "grey"
        elif self.permissive:
            if self.state:
                color = "green"  # Running
            else:
                color = "red"  # Permitted to start
        else:
            if self.state:
                color = "purple"  # Error
                print("Got error state")
            else:
                color = "grey"  # Not ready

        self.pid.canvas.tk.itemconfigure(self.shell, outline=color)
        self.pid.canvas.tk.itemconfigure(self.impeller, outline=color)

    def isPumpHit(self, x, y):
        return self.x - self.size <= x <= self.x + self.size and \
               self.y - self.size <= y <= self.y + self.size
