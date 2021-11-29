from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return len(self._ostokset)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self._ostokset:
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        onjo = 0
        for place, haku in enumerate(self._ostokset):
            if ostos.tuotteen_nimi() == haku.tuotteen_nimi():
                self._ostokset[place].muuta_lukumaaraa(1)
                onjo = 1
        if onjo == 0:
            self._ostokset.append(ostos)
        

    def poista_tuote(self, poistettava: Tuote):
        ostos = Ostos(poistettava)
        for place, haku in enumerate(self._ostokset):
            if ostos.tuotteen_nimi() == haku.tuotteen_nimi():
                if(self._ostokset[place].lukumaara() > 1):
                    self._ostokset[place].muuta_lukumaaraa(-1)
                else:
                    self._ostokset.pop(place)

    def tyhjenna(self):
        self._ostokset.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
