from guizero import Box, Text, TextBox, CheckBox, PushButton


class CreateData:
    def __init__(self, app, pid):
        self.app = app
        self.pid = pid
        self.box = Box(self.app, align="top", width=1024, height=200)
        self.box.bg = "grey20"
        self.portSrc = self.portDst = self.stbdSrc = self.stbdDst = None

        col = 0
        b = Box(self.box, align="left", width=100, height=200)
        Text(b, text="", color="white")

        col += 1
        b = Box(self.box, align="left", width=75, height=200)
        Text(b, text="Port", size=24, color="red2", align="top")
        Text(b, text="xx.x", size=24, color="white", align="top")
        Text(b, text="xxx", size=24, color="white", align="top")
        Text(b, text="", size=24, color="white", align="top")

        col += 1
        b = Box(self.box, align="left", width=25, height=200)
        Text(b, text="", size=24, color="white")
        Text(b, text="%", size=24, color="white")
        Text(b, text="L", size=24, color="white")
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=80, height=200)
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=200, height=200)
        Text(b, text="Transfer:", font="courier", size=24, color="white")
        Text(b, text="Time:", font="courier", size=24, color="white")
        Text(b, text="Destination:", font="courier", size=24, color="white")
        Text(b, text="Source:", font="courier", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=100, height=200)
        self.volume = TextBox(b, text="0")
        self.time = TextBox(b, text="0")
        self.volume.text_size = self.time.text_size = 19
        self.portDst = CheckBox(b, text="Port", width=100)
        self.portSrc = CheckBox(b, text="Port", width=100)
        self.portSrc.bg = self.portDst.bg = "red4"
        self.portSrc.text_size = self.portDst.text_size = 20

        col += 1
        b = Box(self.box, align="left", width=120, height=200)
        Text(b, text="L", size=24, color="white")
        Text(b, text="min:sec", size=24, color="white")
        self.stbdDst = CheckBox(b, text="Stbd", width=100)
        self.stbdSrc = CheckBox(b, text="Stbd", width=100)
        self.stbdSrc.bg = self.stbdDst.bg = "green4"
        self.stbdSrc.text_size = self.stbdDst.text_size = 20

        col += 1
        b = Box(self.box, align="left", width=25, height=200)
        self.volUp = PushButton(b, text="^", image="up_arrow.png", pady=5)
        self.timUp = PushButton(b, text="^", image="up_arrow.png", pady=5)
        self.volUp.bg = self.timUp.bg = "white"
        Text(b, text="", size=24, color="white")
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=25, height=200)
        self.volDn = PushButton(b, text="v", image="down_arrow.png", pady=5)
        self.timDn = PushButton(b, text="v", image="down_arrow.png", pady=5)
        self.volDn.bg = self.timDn.bg = "white"
        Text(b, text="", size=24, color="white")
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=55, height=200)
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=75, height=200)
        Text(b, text="Stbd", size=24, color="green")
        Text(b, text="xx.x", size=24, color="white")
        Text(b, text="xxx", size=24, color="white")
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=25, height=200)
        Text(b, text="", size=24, color="white")
        Text(b, text="%", size=24, color="white")
        Text(b, text="L", size=24, color="white")
        Text(b, text="", size=24, color="white")

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

