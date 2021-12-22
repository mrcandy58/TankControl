# Python script to control fuel transfer and cleaning between tanks
from guizero import App, Drawing
from PID import CreatePID
from data import CreateData

if __name__ == '__main__':

    app = App(title='Fuel Tank Control', width=1024, height=600, layout="grid")

    canvas = Drawing(app, 1024, 315, grid=[0, 0])
    canvas.bg = "grey70"

    pid = CreatePID(canvas)
    canvas.repeat(500, pid.flasher)

    data = CreateData(app, pid)

    app.display()
