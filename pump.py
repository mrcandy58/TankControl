class Pump:
    def __init__(self, cnv, x, y, state=False, size=40):
        self.x = x
        self.y = y
        self.canvas = cnv
        self.state = state
        self.size = size

        self.shell = self.canvas.oval(self.x - self.size, self.y - self.size,
                                      self.x + self.size, self.y + self.size,
                                      color="grey20",
                                      outline=5, outline_color="gray", )
        self.impeller = self.canvas.triangle(self.x - self.size / 3, self.y - self.size / 2,
                                             self.x - self.size / 3, self.y + self.size / 2,
                                             self.x + self.size / 2, self.y,
                                             color="grey20",
                                             outline=3, outline_color="gray", )
        if self.state:
            self.run()
        else:
            self.stop()

    def run(self):
        self.state = True
        self.canvas.tk.itemconfigure(self.shell, outline="green")
        self.canvas.tk.itemconfigure(self.impeller, outline="green")

    def stop(self):
        self.state = False
        self.canvas.tk.itemconfigure(self.shell, outline="red")
        self.canvas.tk.itemconfigure(self.impeller, outline="red")
