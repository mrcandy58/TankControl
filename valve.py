class Valve:
    def __init__(self, cnv, x, y, state=False, size=20):
        self.x = x
        self.y = y
        self.canvas = cnv
        self.state = state
        self.size = size
        self.partner = None

        self.left = self.canvas.triangle(self.x - self.size, self.y - self.size,
                                         self.x - self.size, self.y + self.size, x, y,
                                         outline=True, outline_color="gray", )
        self.right = self.canvas.triangle(self.x + self.size, self.y - self.size,
                                          self.x + self.size, self.y + self.size, x, y,
                                          outline=True, outline_color="gray", )
        if self.state:
            self.open()
        else:
            self.close()

    def set_partner(self, partner):
        self.partner = partner

    def open(self):
        if self.partner is not None:
            self.partner.close()
        self.state = True
        self.canvas.tk.itemconfigure(self.left, fill="green")
        self.canvas.tk.itemconfigure(self.right, fill="green")

    def close(self):
        self.state = False
        self.canvas.tk.itemconfigure(self.left, fill="red")
        self.canvas.tk.itemconfigure(self.right, fill="red")
