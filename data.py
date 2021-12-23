from guizero import Box, Text, TextBox, CheckBox, PushButton


class CreateData:
    def __init__(self, app, pid):
        self.app = app
        self.pid = pid
        self.box = Box(self.app, align="top", width=1024, height=200)
        self.box.bg = "grey20"
        self.portSrc = self.portDst = self.stbdSrc = self.stbdDst = None
        self.delta = 0
        self.count = 0

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
        b = Box(self.box, align="left", width=50, height=200)
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=225, height=200)
        Text(b, text="Transfer:", size=24, color="white")
        Text(b, text="Time:", size=24, color="white")
        Text(b, text="Destination:", size=24, color="white")
        Text(b, text="Source:", size=24, color="white")

        col += 1
        w = 110
        b = Box(self.box, align="left", width=w, height=200)
        b1 = Box(b, align="top", width=w, height=75)
        b2 = Box(b, align="top", width=w, height=100)
        self.volume = TextBox(b1, text="0")
        self.time = TextBox(b1, text="0:0")
        self.volume.text_size = self.time.text_size = 19
        self.volume.text_color = self.time.text_color = "white"
        self.portDst = CheckBox(b2, text="Port", width=w)
        self.portSrc = CheckBox(b2, text="Port", width=w)
        self.portSrc.bg = self.portDst.bg = "red4"
        self.portSrc.text_size = self.portDst.text_size = 20

        col += 1
        b = Box(self.box, align="left", width=w, height=200)
        b1 = Box(b, align="top", width=w, height=75)
        b2 = Box(b, align="top", width=w, height=100)
        Text(b1, text="L", size=24, color="white")
        Text(b1, text="m:s", size=24, color="white")
        self.stbdDst = CheckBox(b2, text="Stbd", width=w)
        self.stbdSrc = CheckBox(b2, text="Stbd", width=w)
        self.stbdSrc.bg = self.stbdDst.bg = "green4"
        self.stbdSrc.text_size = self.stbdDst.text_size = 20

        col += 1
        b = Box(self.box, align="left", width=40, height=200)
        self.volUp = PushButton(b, text="^", image="up_arrow.png", pady=5)
        self.volUp.when_left_button_pressed = self.volUpStart
        self.volUp.when_left_button_released = self.volUpEnd
        self.timUp = PushButton(b, text="^", image="up_arrow.png", pady=5)
        self.timUp.when_left_button_pressed = self.timUpStart
        self.timUp.when_left_button_released = self.timUpEnd
        self.volUp.bg = self.timUp.bg = "white"
        Text(b, text="", size=24, color="white")
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=40, height=200)
        self.volDn = PushButton(b, text="v", image="down_arrow.png", pady=5)
        self.volDn.when_left_button_pressed = self.volDnStart
        self.volDn.when_left_button_released = self.volDnEnd
        self.timDn = PushButton(b, text="v", image="down_arrow.png", pady=5)
        self.timDn.when_left_button_pressed = self.timDnStart
        self.timDn.when_left_button_released = self.timDnEnd
        self.volDn.bg = self.timDn.bg = "white"
        Text(b, text="", size=24, color="white")
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=30, height=200)
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

    def volUpStart(self, event):
        print("Vol up start")
        self.delta = 1
        self.count = 1
        self.volUp.after(10, self.doVolUp, [])

    def volUpEnd(self, event):
        print("Vol up end")
        self.delta = self.count = 0

    def doVolUp(self):
        print("In VolUp")
        if self.count == 0:
            return
        v = int(self.volume.value) + self.delta
        if v >= 200:
            v = 200
            self.volume.value = v
            return
        self.volume.value = v
        self.count += 1
        if self.count == 6:
            self.delta *= 10
        self.volUp.after(500, self.doVolUp)

    def volDnStart(self, event):
        print("Vol dn start")
        self.delta = -1
        self.count = 1
        self.volDn.after(10, self.doVolDn, [])

    def volDnEnd(self, event):
        print("Vol dn end")
        self.delta = self.count = 0

    def doVolDn(self):
        print("In VolDn")
        if self.count == 0:
            return
        v = int(self.volume.value) + self.delta
        if v <= 0:
            v = 0
            self.volume.value = v
            return
        self.volume.value = v
        self.count += 1
        if self.count == 6:
            self.delta *= 10
        self.volDn.after(500, self.doVolDn)

    def timUpStart(self, event):
        self.delta = 15
        self.count = 1
        self.timUp.after(10, self.doTimUp, [])

    def timUpEnd(self, event):
        self.delta = self.count = 0

    def doTimUp(self):
        if self.count == 0:
            return
        tm = self.time.value.split(":")
        t = int(tm[0]) * 60 + int(tm[1]) + self.delta
        if t >= 1200:
            t = 1200
            self.time.value = "{:02d}:{:02d}".format(int(t / 60), t % 60)
            return
        self.time.value = "{:02d}:{:02d}".format(int(t / 60), t % 60)
        self.count += 1
        if self.count == 5:
            self.delta = 1 * 60
        if self.count == 9:
            self.delta = 5 * 60
        self.timUp.after(500, self.doTimUp)

    def timDnStart(self, event):
        self.delta = -15
        self.count = 1
        self.timDn.after(10, self.doTimDn, [])

    def timDnEnd(self, event):
        self.delta = self.count = 0

    def doTimDn(self):
        if self.count == 0:
            return
        tm = self.time.value.split(":")
        t = int(tm[0]) * 60 + int(tm[1]) + self.delta
        if t <= 0:
            t = 0
            self.time.value = "{:02d}:{:02d}".format(int(t / 60), t % 60)
            return
        self.time.value = "{:02d}:{:02d}".format(int(t / 60), t % 60)

        self.count += 1
        if self.count == 5:
            self.delta = -1 * 60
        if self.count == 9:
            self.delta = -5 * 60
        self.timDn.after(500, self.doTimDn)

