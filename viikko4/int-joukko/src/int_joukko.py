class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = []
        self.alkioiden_lukumaara = 0

    def kuuluu(self, n):

        if n in self.lukujono:
                return True
        return False

    def lisaa(self, n):

        if not self.kuuluu(n):
            self.lukujono.append(n)
            self.alkioiden_lukumaara += 1

            return True

        return False

    def poista(self, n):

        if n in self.lukujono:
            
            self.lukujono.pop((self.lukujono.index(n)))
            self.alkioiden_lukumaara -= 1
            return True

        return False

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):  
        return self.lukujono

    @staticmethod
    def yhdiste(a, b):

        for i in b.lukujono:
            a.lisaa(i)

        return a

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()

        for i in a.lukujono:
            if i in b.lukujono:
                y.lisaa(i)

        return y

    @staticmethod
    def erotus(a, b):

        for i in b.lukujono:
            a.poista(i)

        return a

    def __str__(self):
        tuotos = ""
        if self.alkioiden_lukumaara > 0:
            for i in range(0, self.alkioiden_lukumaara - 1):
                tuotos += str(self.lukujono[i]) + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lukumaara - 1])
        return "{"+tuotos+"}"
