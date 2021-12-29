import os


class fsIO:
    def __init__(self, fs):
        self.fs = fs
        self.bus = 1        # I2C bus
        self.addr = 0x10    # Relay board I2C address

        self.pins = {
            "port suction":     {"direction": "output", "bus": "i2c", "pin": 1},
            "stbd suction":     {"direction": "output", "bus": "i2c", "pin": 2},
            "port discharge":   {"direction": "output", "bus": "i2c", "pin": 3},
            "stbd discharge":   {"direction": "output", "bus": "i2c", "pin": 4},
            "xfer pump":        {"direction": "output", "bus": "gp",  "pin": "IO26"},

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
                io.system("i2cset -y {:d} 0x{:02x} 0x{:02x} 0xFF".format(self.bus, self.addr, p["pin"]))
                print("i2c pin {:d} ON".format(p["pin"]))
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
                io.system("i2cset -y {:d} 0x{:02x} 0x{:02x} 0x00".format(self.bus, self.addr, p["pin"]))
                print("i2c pin {:d} OFF".format(p["pin"]))
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
