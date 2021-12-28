class Filter:
    def __init__(self, fs, x, y, state=True, size=40, offset=20):
        self.x = x
        self.y = y
        self.fs = fs
        self.state = state
        self.size = size
        self.offset = offset

        self.shell1 = self.fs.canvas.oval(self.x - self.size / 2, self.y - self.size + self.offset,
                                          self.x + self.size / 2, self.y + self.size + self.offset,
                                          color="grey20",
                                          outline=5, outline_color="gray")
        self.shell2 = self.fs.canvas.rectangle(self.x - self.size / 2, self.y + self.offset,
                                               self.x + self.size / 2, self.y - self.size + self.offset,
                                               color="grey20",
                                               outline=5, outline_color="gray")
        if self.state:
            self.clear()
        else:
            self.plugged()

    def clear(self):
        self.state = True
        self.fs.canvas.tk.itemconfigure(self.shell1, outline="green2")
        self.fs.canvas.tk.itemconfigure(self.shell2, outline="green2")

    def plugged(self):
        self.state = False
        self.fs.canvas.tk.itemconfigure(self.shell1, outline="red")
        self.fs.canvas.tk.itemconfigure(self.shell2, outline="red")
