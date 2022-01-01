from guizero import Box, Text, TextBox, CheckBox, PushButton
import os


class CreateData:
    def __init__(self, fs):
        try:
            self.path = os.environ['TANK']
        except KeyError:
            self.path = "."
        self.fs = fs
        self.box = Box(self.fs.app, align="top", width=1024, height=200)
        self.box.bg = "grey20"
        self.portSrc = self.portDst = self.stbdSrc = self.stbdDst = None
        self.delta = 0
        self.count = 0
        self.time = 0           # msec to run pump
        self.togo = 0.0         # L to xfer
        self.tallyP = 0.0       # Last tally on previous check
        self.flowrate = 0.0     # Instantaneous flowrate
        self.K = 1 / 660.0      # Flowmeter factor L/pulse

        col = 0
        b = Box(self.box, align="left", width=100, height=200)
        Text(b, text="", color="white")

        col += 1
        b = Box(self.box, align="left", width=75, height=200)
        Text(b, text="Port", size=24, color="red2", align="top")
        self.portPercent = Text(b, text="xx.x", size=24, color="white", align="top")
        self.portLiters = Text(b, text="xxx", size=24, color="white", align="top")
        self.ESD = PushButton(b, command=self.esd, text="ESD", pady=2)
        self.ESD.text_size = 20
        self.ESD.text_color = "red"

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
        self.volumeStr = TextBox(b1, text="0.0")
        self.volumeStr.when_key_pressed = self.volKey
        self.timeStr = TextBox(b1, text="0:00")
        self.timeStr.when_key_pressed = self.timeKey
        self.volumeStr.text_size = self.timeStr.text_size = 19
        self.volumeStr.text_color = self.timeStr.text_color = "white"
        self.portDst = CheckBox(b2, text="Port", width=w)
        self.portSrc = CheckBox(b2, text="Port", width=w)
        self.portSrc.bg = self.portDst.bg = "red4"
        self.portSrc.text_size = self.portDst.text_size = 20
        self.fs.pid.portSuctionValve.checkbox = self.portSrc
        self.fs.pid.portDischargeValve.checkbox = self.portDst

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
        self.fs.pid.stbdSuctionValve.checkbox = self.stbdSrc
        self.fs.pid.stbdDischargeValve.checkbox = self.stbdDst

        col += 1
        b = Box(self.box, align="left", width=40, height=200)
        self.volUp = PushButton(b, text="^", image=self.path + "/up_arrow.png", pady=5)
        self.volUp.when_left_button_pressed = self.volUpStart
        self.volUp.when_left_button_released = self.volUpEnd
        self.timUp = PushButton(b, text="^", image=self.path + "/up_arrow.png", pady=5)
        self.timUp.when_left_button_pressed = self.timUpStart
        self.timUp.when_left_button_released = self.timUpEnd
        self.volUp.bg = self.timUp.bg = "white"
        Text(b, text="", size=24, color="white")
        Text(b, text="", size=24, color="white")

        col += 1
        b = Box(self.box, align="left", width=40, height=200)
        self.volDn = PushButton(b, text="v", image=self.path + "/down_arrow.png", pady=5)
        self.volDn.when_left_button_pressed = self.volDnStart
        self.volDn.when_left_button_released = self.volDnEnd
        self.timDn = PushButton(b, text="v", image=self.path + "/down_arrow.png", pady=5)
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
        self.stbdPercent = Text(b, text="xx.x", size=24, color="white")
        self.stbdLiters = Text(b, text="xxx", size=24, color="white")
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

        self.updateData()

    def volKey(self, event):
        if event.tk_event.keysym == "Return":
            v = self.volumeStr.value
            print("got", v)
            try:
                self.togo = float(v)
            except ValueError:
                v = 0.0
            self.volumeStr.value = "{:3.1f}".format(self.togo)

    def timeKey(self, event):
        if event.tk_event.keysym == "Return":
            t = self.timeStr.value
            print("got", t)
            try:
                t1, t2 = t.split(":")
                msec = (int(t1) * 60 + int(t2)) * 1000
            except ValueError:
                msec = 0
            self.time = msec
            self.timeStr.value = "{:2d}:{:02d}".format(int(self.time / (60 * 1000)),
                                                        int(self.time % (60 * 1000) / 1000))

    def esd(self):
        print("ESD")
        self.fs.pid.pump.stop()
        self.fs.pid.allValvesClose()

    def updateData(self):
        # Check filter state
        pin = self.fs.io.pins["primary filter"]
        if self.fs.io.pi.read(pin["pin"]):
            self.fs.pid.filter.plugged()
        else:
            self.fs.pid.filter.clear()

        # Calculate number of flow meter pulses
        t = self.fs.io.counter.tally()
        deltaT = t - self.tallyP
        self.tallyP = t

        # Convert pulses in last refresh period to flow rate
        self.flowrate = deltaT * self.K / (self.fs.refresh / 1000) * 60.0  # L/m
        self.fs.canvas.tk.itemconfigure(self.fs.pid.meter.flowRate, text="{:3.1f} L/m".format(self.flowrate))

        # Calculate volume from pulses
        deltaV = deltaT * self.K

        # TODO Remove following if/elif to update tank levels - for testing only
        # TODO Update tank level and percent from N2k
        if self.fs.pid.portSuctionValve.state and self.fs.pid.stbdDischargeValve.state and self.fs.pid.pump.state:
            self.fs.pid.portTank.incLevel(-deltaV)
            self.fs.pid.stbdTank.incLevel(deltaV)
        elif self.fs.pid.stbdSuctionValve.state and self.fs.pid.portDischargeValve.state and self.fs.pid.pump.state:
            self.fs.pid.portTank.incLevel(deltaV)
            self.fs.pid.stbdTank.incLevel(-deltaV)

        # Update tank levels
        self.portPercent.value = "{:0.1f}".format(self.fs.pid.portTank.getPercent())
        self.portLiters.value = "{:4.1f}".format(self.fs.pid.portTank.getLevel())
        self.stbdPercent.value = "{:0.1f}".format(self.fs.pid.stbdTank.getPercent())
        self.stbdLiters.value = "{:4.1f}".format(self.fs.pid.stbdTank.getLevel())

        # Check tank state
        self.fs.pid.portTank.checkLevel()
        self.fs.pid.stbdTank.checkLevel()

        # Update fuel volume and time remaining in xfer
        if self.fs.pid.pump.state:
            self.togo -= deltaV
            if self.togo < 0.0:
                self.togo = 0.0
            self.volumeStr.value = "{:3.1f}".format(self.togo)

            self.time -= self.fs.refresh
            if self.time < 0:
                self.time = 0
            self.timeStr.value = "{:02d}:{:02d}".format(int(self.time / (60 * 1000)),
                                                        int(self.time % (60 * 1000) / 1000))

        # Check if xfer is complete
        if self.togo == 0.0 and self.time == 0 and self.fs.pid.pump.state:
            self.fs.pid.pump.stop()
            self.fs.pid.allValvesClose()
            self.portSrc.value = self.portDst.value = self.stbdSrc.value = self.stbdDst.value = False

    def doValve(self, checkbox):
        if checkbox == self.portSrc:
            self.stbdSrc.value = 0
            if checkbox.value == 1:
                self.fs.pid.portSuctionValve.open()
            else:
                self.fs.pid.portSuctionValve.close()
        elif checkbox == self.portDst:
            self.stbdDst.value = 0
            if checkbox.value == 1:
                self.fs.pid.portDischargeValve.open()
            else:
                self.fs.pid.portDischargeValve.close()
        elif checkbox == self.stbdSrc:
            self.portSrc.value = 0
            if checkbox.value == 1:
                self.fs.pid.stbdSuctionValve.open()
            else:
                self.fs.pid.stbdSuctionValve.close()
        else:
            self.portDst.value = 0
            if checkbox.value == 1:
                self.fs.pid.stbdDischargeValve.open()
            else:
                self.fs.pid.stbdDischargeValve.close()

    def volUpStart(self, event):
        self.delta = 1
        self.count = 1
        self.volUp.after(10, self.doVolUp, [])

    def volUpEnd(self, event):
        self.delta = self.count = 0

    def doVolUp(self):
        if self.count == 0:
            return
        self.togo += self.delta
        if self.togo >= 200.0:
            self.togo = 200.0
            self.volumeStr.value = "{:3.1f}".format(self.togo)
            return
        self.volumeStr.value = "{:3.1f}".format(self.togo)
        self.count += 1
        if self.count == 6:
            self.delta *= 10
        self.volUp.after(500, self.doVolUp)

    def volDnStart(self, event):
        self.delta = -1
        self.count = 1
        self.volDn.after(10, self.doVolDn, [])

    def volDnEnd(self, event):
        self.delta = self.count = 0

    def doVolDn(self):
        if self.count == 0:
            return
        self.togo += self.delta
        if self.togo <= 0.0:
            self.togo = 0.0
            self.volumeStr.value = "{:3.1f}".format(self.togo)
            return
        self.volumeStr.value = "{:3.1f}".format(self.togo)
        self.count += 1
        if self.count == 6:
            self.delta *= 10
        self.volDn.after(500, self.doVolDn)

    def timUpStart(self, event):
        self.delta = 15 * 1000
        self.count = 1
        self.timUp.after(10, self.doTimUp, [])

    def timUpEnd(self, event):
        self.delta = self.count = 0

    def doTimUp(self):
        if self.count == 0:
            return
        self.time += self.delta
        if self.time >= 20 * 60 * 1000:
            self.time = 20 * 60 * 1000
            self.timeStr.value = "{:02d}:{:02d}".format(int(self.time / (60 * 1000)),
                                                        int(self.time % (60 * 1000) / 1000))
            return
        self.timeStr.value = "{:02d}:{:02d}".format(int(self.time / (60 * 1000)),
                                                    int(self.time % (60 * 1000) / 1000))
        self.count += 1
        if self.count == 5:
            self.delta = 1 * 60 * 1000
        if self.count == 9:
            self.delta = 5 * 60 * 1000
        self.timUp.after(500, self.doTimUp)

    def timDnStart(self, event):
        self.delta = -15 * 1000
        self.count = 1
        self.timDn.after(10, self.doTimDn, [])

    def timDnEnd(self, event):
        self.delta = self.count = 0

    def doTimDn(self):
        if self.count == 0:
            return
        self.time += self.delta
        if self.time <= 0:
            self.time = 0
            self.timeStr.value = "{:02d}:{:02d}".format(int(self.time / (60 * 1000)),
                                                        int(self.time % (60 * 1000) / 1000))
            return
        self.timeStr.value = "{:02d}:{:02d}".format(int(self.time / (60 * 1000)),
                                                    int(self.time % (60 * 1000) / 1000))

        self.count += 1
        if self.count == 5:
            self.delta = -1 * 60 * 1000
        if self.count == 9:
            self.delta = -5 * 60 * 1000
        self.timDn.after(500, self.doTimDn)
