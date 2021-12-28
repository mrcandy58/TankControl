class Valve:
    def __init__(self, fs, x, y, name, state=False, size=20):
        self.x = x
        self.y = y
        self.fs = fs
        self.state = state
        self.size = size
        self.partner = None
        self.name = name

        self.left = self.fs.canvas.triangle(self.x - self.size, self.y - self.size,
                                            self.x - self.size, self.y + self.size, self.x, self.y,
                                            outline=2, outline_color="gray")
        self.right = self.fs.canvas.triangle(self.x + self.size, self.y - self.size,
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
        self.fs.io.valveOpen(self.name)
        self.fs.canvas.tk.itemconfigure(self.left, fill="green2")
        self.fs.canvas.tk.itemconfigure(self.right, fill="green2")
        self.fs.pid.pump.setPermissive(self.fs.pid.isPathOpen())

    def close(self, doCheck=True):
        self.state = False
        self.fs.io.valveClose(self.name)
        self.fs.canvas.tk.itemconfigure(self.left, fill="red")
        self.fs.canvas.tk.itemconfigure(self.right, fill="red")
        if doCheck:
            self.fs.pid.pump.setPermissive(self.fs.pid.isPathOpen())
