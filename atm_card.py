class ATMCard:
    def __init__(self, defaultpin, defaultbalance):
        self.defaultpin = defaultpin
        self.defaultbalance = defaultbalance
    
    def pinawal(self):
        return self.defaultpin
    
    def saldoawal(self):
        return self.defaultbalance