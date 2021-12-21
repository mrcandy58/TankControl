# Python script to control fuel transfer and cleaning between tanks
from guizero import App, Drawing
from PID import CreatePID


if __name__ == '__main__':

    app = App(title='Fuel Tank Control', width=1024, height=600)

    canvas = Drawing(app, 1024, 500)
    canvas.bg = "grey20"
    pid = CreatePID(canvas)

    pid.stbdSuctionValve.open()
    pid.portDischargeValve.open()

    app.display()
