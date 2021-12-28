class fsIO:
    def __init__(self, fs):
        self.fs = fs

        self.pins = {
            "port suction":     {"direction": "output", "bus": "i2c", "pin": "1"},
            "stbd suction":     {"direction": "output", "bus": "i2c", "pin": "2"},
            "port discharge":   {"direction": "output", "bus": "i2c", "pin": "3"},
            "stbd discharge":   {"direction": "output", "bus": "i2c", "pin": "4"},
            "xfer pump":        {"direction": "output", "bus": "gp",  "pin": "11"},

            "primary filter":   {"direction": "input", "bus": "gp", "pin": "12"},

            "fuel flow":        {"direction": "freq", "bus": "gp", "pin": "13"}
        }

    def ioOn(self, name):
        if name in self.pins:
            p = self.pins[name]
            if p["direction"] != "output":
                print("Cannot perform output on %s", name)
                return False

            if p["bus"] == "i2c":
                print("i2c pin {:s} ON".format(p["pin"]))
            elif p["bus"] == "gp":
                print("gpio pin {:s} ON".format(p["pin"]))
            else:
                print("Unknown bus {:s} for {:s}".format(p["bus"], name))
                return False

            return True

    def ioOff(self, name):
        if name in self.pins:
            p = self.pins[name]
            if p["direction"] != "output":
                print("Cannot perform output on {:s}".format(name))
                return False

            if p["bus"] == "i2c":
                print("i2c pin {:s} OFF".format(p["pin"]))
            elif p["bus"] == "gp":
                print("gpio pin {:s} OFF".format(p["pin"]))
            else:
                print("Unknown bus {:s} for {:s}".format(p["bus"], name))
                return False

            return True

    def valveOpen(self, name):
        if self.ioOn(name):
            print("Opened {:s}".format(name))

    def valveClose(self, name):
        if self.ioOff(name):
            print("Closed {:s}".format(name))

    def pumpStart(self, name):
        if self.ioOn(name):
            print("Started {:s}".format(name))

    def pumpStop(self, name):
        if self.ioOff(name):
            print("Stopped {:s}".format(name))
