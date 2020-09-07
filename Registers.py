#contains all the registers
class Registers():
    def __init__(self):
        self.AC  = [0]*40
        self.MBR = [0]*20
        self.IBR = [0]*20
        self.IR  = [0]*8
        self.MAR = [0]*12
        self.PC  = 0
        self.MQ  = [0]*40