from atm_card import ATMCard

class Customer:
    def __init__(self, id, custpin, custbalance):
        self.id = id
        self.custpin = 1234
        self.custbalance = 10000

    def cek_id(self):
        return self.id
    
    def cek_pin(self):
        return self.custpin
    
    def cek_saldo(self):
        return self.custbalance

    def debet(self, nominal_debet):
        self.custbalance -= nominal_debet
        return self.custbalance
    
    def simpan(self, nominal_simpan):
        self.custbalance += nominal_simpan
        return self.custbalance
    
    def ubahPin(self, pinBaru):
        self.custpin = pinBaru
        return self.custpin