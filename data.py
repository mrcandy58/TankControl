from guizero import Box, Text, TextBox, CheckBox, PushButton


class CreateData:
    def __init__(self, app, pid):
        self.app = app
        self.pid = pid
        self.box = Box(self.app, layout="grid")
        self.portSrc = self.portDst = self.stbdSrc = self.stbdDst = None
        self.volume = 0
        self.time = 0

        Text(self.box, text="Port", size=24, color="red", grid=[0, 0])
        Text(self.box, text="xx.x", size=24, color="white", grid=[0, 1])
        Text(self.box, text="xxx", size=24, color="white", grid=[0, 2])

        Text(self.box, text="%", size=24, color="white", grid=[1, 1])
        Text(self.box, text="L", size=24, color="white", grid=[1, 2])

        Text(self.box, text="", color="white", grid=[2, 0], width=15)

        Text(self.box, text="Transfer:", size=24, color="white", grid=[3, 0], align="right")
        Text(self.box, text="Time:", size=24, color="white", grid=[3, 1], align="right")
        Text(self.box, text="Source:", size=24, color="white", grid=[3, 2], align="right")
        Text(self.box, text="Destination:", size=24, color="white", grid=[3, 3], align="right")

        TextBox(self.box, grid=[4, 0])
        TextBox(self.box, grid=[4, 1])
        self.portSrc = CheckBox(self.box, text="Port", grid=[4, 2])
        self.portDst = CheckBox(self.box, text="Port", grid=[4, 3])

        Text(self.box, text="L", size=24, color="white", grid=[5, 0], align="left")
        Text(self.box, text="min:sec", size=24, color="white", grid=[5, 1], align="left")
        self.stbdSrc = CheckBox(self.box, text="Stbd", grid=[5, 2])
        self.stbdDst = CheckBox(self.box, text="Stbd", grid=[5, 3])

        self.volUp = PushButton(self.box, text="^", grid=[6, 0], image="up_arrow.png", pady=5)
        self.timUp = PushButton(self.box, text="^", grid=[6, 1], image="up_arrow.png", pady=5)

        self.volDn = PushButton(self.box, text="v", grid=[7, 0], image="down_arrow.png", pady=5)
        self.timDn = PushButton(self.box, text="v", grid=[7, 1], image="down_arrow.png", pady=5)

        Text(self.box, text="", color="white", grid=[8, 0], width=15)

        Text(self.box, text="Stbd", size=24, align="top", color="green", grid=[9, 0])
        Text(self.box, text="xx.x", size=24, color="white", grid=[9, 1])
        Text(self.box, text="xxx", size=24, color="white", grid=[9, 2])

        Text(self.box, text="%", size=24, color="white", grid=[10, 1])
        Text(self.box, text="L", size=24, color="white", grid=[10, 2])

        self.portSrc.update_command(self.doValve, [self.portSrc])
        self.portDst.update_command(self.doValve, [self.portDst])
        self.stbdSrc.update_command(self.doValve, [self.stbdSrc])
        self.stbdDst.update_command(self.doValve, [self.stbdDst])

        #  self.portSrc.toggle()
        #  self.portDst.toggle()

    def doValve(self, checkbox):

        if checkbox == self.portSrc:
            self.stbdSrc.value = 0
            if checkbox.value == 1:
                self.pid.portSuctionValve.open()
            else:
                self.pid.portSuctionValve.close()
        elif checkbox == self.portDst:
            self.stbdDst.value = 0
            if checkbox.value == 1:
                self.pid.portDischargeValve.open()
            else:
                self.pid.portDischargeValve.close()
        elif checkbox == self.stbdSrc:
            self.portSrc.value = 0
            if checkbox.value == 1:
                self.pid.stbdSuctionValve.open()
            else:
                self.pid.stbdSuctionValve.close()
        else:
            self.portDst.value = 0
            if checkbox.value == 1:
                self.pid.stbdDischargeValve.open()
            else:
                self.pid.stbdDischargeValve.close()

