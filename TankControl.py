# Python script to control fuel transfer and cleaning between tanks
from guizero import App, Drawing
from PID import CreatePID
from data import CreateData

if __name__ == '__main__':

    app = App(title='Fuel Tank Control', width=1024, height=600)

    canvas = Drawing(app, 1024, 325)
    canvas.bg = "grey20"

    pid = CreatePID(canvas)
    canvas.repeat(500, pid.flasher)

    data = CreateData(app, pid)

    app.display()
