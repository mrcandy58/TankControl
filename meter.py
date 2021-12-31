

class Meter:
    def __init__(self, fs, x, y, name):
        self.fs = fs
        self.x = x
        self.y = y
        self.name = name

        self.fs.canvas.rectangle(self.x - 10, self.y - 30, self.x + 10, self.y + 30, color="grey20",
                                 outline=3, outline_color="gray")
        self.fs.canvas.oval(self.x - 6, self.y - 25, self.x + 6, self.y, color="gray20",
                            outline=3, outline_color="gray")
        self.fs.canvas.oval(self.x - 6, self.y + 25, self.x + 6, self.y, color="gray20",
                            outline=3, outline_color="gray")
        self.flowRate = self.fs.canvas.text(self.x + 30, self.y + 10, "test", color="white")

