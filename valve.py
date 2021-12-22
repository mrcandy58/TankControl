class Valve:
    def __init__(self, pid, x, y, name, state=False, size=20):
        self.x = x
        self.y = y
        self.pid = pid
        self.state = state
        self.size = size
        self.partner = None
        self.name = name

        self.left = self.pid.canvas.triangle(self.x - self.size, self.y - self.size,
                                             self.x - self.size, self.y + self.size, self.x, self.y,
                                             outline=2, outline_color="gray")
        self.right = self.pid.canvas.triangle(self.x + self.size, self.y - self.size,
                                              self.x + self.size, self.y + self.size, self.x, self.y,
                                              outline=2, outline_color="gray")
        if self.state:
            self.open()
        else:
            self.close(doCheck=False)

    def set_partner(self, partner):
        self.partner = partner

    def open(self):
        if self.partner is not None:
            self.partner.close()
        self.state = True
        print(self.name, "open")
        self.pid.canvas.tk.itemconfigure(self.left, fill="green2")
        self.pid.canvas.tk.itemconfigure(self.right, fill="green2")
        self.pid.pump.setPermissive(self.pid.isPathOpen())

    def close(self, doCheck=True):
        self.state = False
        print(self.name, "close")
        self.pid.canvas.tk.itemconfigure(self.left, fill="red")
        self.pid.canvas.tk.itemconfigure(self.right, fill="red")
        if doCheck:
            self.pid.pump.setPermissive(self.pid.isPathOpen())
