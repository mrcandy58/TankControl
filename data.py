from guizero import Box, Text, TextBox, CheckBox, PushButton


class CreateData:
    def __init__(self, app, pid):
        self.app = app
        self.pid = pid
        self.box = Box(self.app, grid=[0, 1], layout="grid")
        self.box.bg = "grey50"
        self.box.width = "fill"
        self.portSrc = self.portDst = self.stbdSrc = self.stbdDst = None
        self.volume = 0
        self.time = 0

        col = 0
        Box(self.box, grid=[col, 0], width="fill")
        #  Text(self.box, text="", color="white", grid=[col, 0], width="fill")

        col += 1
        Text(self.box, text="Port", size=24, color="red", grid=[col, 0])
        Text(self.box, text="xx.x", size=24, color="white", grid=[col, 1])
        Text(self.box, text="xxx", size=24, color="white", grid=[col, 2])

        col += 1
        Text(self.box, text="%", size=24, color="white", grid=[col, 1])
        Text(self.box, text="L", size=24, color="white", grid=[col, 2])

        col += 1
        Text(self.box, text="", color="white", grid=[col, 0], width="fill")

        col += 1
        Text(self.box, text="Transfer:", size=24, color="white", grid=[col, 0], align="right")
        Text(self.box, text="Time:", size=24, color="white", grid=[col, 1], align="right")
        Text(self.box, text="Source:", size=24, color="white", grid=[col, 2], align="right")
        Text(self.box, text="Destination:", size=24, color="white", grid=[col, 3], align="right")

        col += 1
        TextBox(self.box, grid=[col, 0])
        TextBox(self.box, grid=[col, 1])
        self.portSrc = CheckBox(self.box, text="Port", grid=[col, 2])
        self.portDst = CheckBox(self.box, text="Port", grid=[col, 3])
        self.portSrc.bg = self.portDst.bg = "red"

        col += 1
        Text(self.box, text="L", size=24, color="white", grid=[col, 0], align="left")
        Text(self.box, text="min:sec", size=24, color="white", grid=[col, 1], align="left")
        self.stbdSrc = CheckBox(self.box, text="Stbd", grid=[col, 2])
        self.stbdDst = CheckBox(self.box, text="Stbd", grid=[col, 3])
        self.stbdSrc.bg = self.stbdDst.bg = "green"

        col += 1
        self.volUp = PushButton(self.box, text="^", grid=[col, 0], image="up_arrow.png", pady=5)
        self.timUp = PushButton(self.box, text="^", grid=[col, 1], image="up_arrow.png", pady=5)
        self.volUp.bg = self.timUp.bg = "white"

        col += 1
        self.volDn = PushButton(self.box, text="v", grid=[col, 0], image="down_arrow.png", pady=5)
        self.timDn = PushButton(self.box, text="v", grid=[col, 1], image="down_arrow.png", pady=5)
        self.volDn.bg = self.timDn.bg = "white"

        col += 1
        Text(self.box, text="", color="white", grid=[col, 0], width="fill")

        col += 1
        Text(self.box, text="Stbd", size=24, align="top", color="green", grid=[col, 0])
        Text(self.box, text="xx.x", size=24, color="white", grid=[col, 1])
        Text(self.box, text="xxx", size=24, color="white", grid=[col, 2])

        col += 1
        Text(self.box, text="%", size=24, color="white", grid=[col, 1])
        Text(self.box, text="L", size=24, color="white", grid=[col, 2])

        col += 1
        Text(self.box, text="", color="white", grid=[col, 0], width="fill")

        self.portSrc.update_command(self.doValve, [self.portSrc])
        self.portDst.update_command(self.doValve, [self.portDst])
        self.stbdSrc.update_command(self.doValve, [self.stbdSrc])
        self.stbdDst.update_command(self.doValve, [self.stbdDst])

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

