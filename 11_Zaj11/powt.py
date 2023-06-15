class Fox:
    def __init__(self, łapy, uszy, ogon):
        self.łapy = łapy
        self.uszy = uszy
        self.ogon = ogon

    def sound(self, special_sound):
        return f'{special_sound}!!! - Lis ma {self.łapy} łapy {self.uszy} uszów i {self.ogon} ogon!'






fafik = Fox(4, 2, 1)
print(fafik.sound('HAHAH'))

