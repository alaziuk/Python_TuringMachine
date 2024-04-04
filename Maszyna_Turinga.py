from abc import ABC, abstractmethod, abstractproperty
from ntpath import join

#odwrócenie liter wyrazu w tekście

class Abstrakcyjna_MaszynaTuringa(ABC):

    def __init__(self):
        pass
    
    @abstractproperty
    def ListaStanow(self):
        pass

    @abstractproperty
    def Przejscia(self):
        pass

    @abstractmethod
    def Krok(self, znak):
        pass

    @abstractmethod
    def Maszyna(self, Tasma):
        pass

    @abstractmethod
    def CzyStanPoczątkowy(self, stan):
        pass

    @abstractmethod
    def CzyStanKoncowy(self, stan):
        pass

class MaszynaTuringa(Abstrakcyjna_MaszynaTuringa):
    def __init__(self, plik):
        self.ListaStanow(plik)
        stany = list(self.stany.keys())
        self.stanPoczatkowy = stany[0]
        self.stan_tymczasowy = self.stanPoczatkowy
        self.glowica = 0                               

    def ListaStanow(self,plik):
        self.plik = open(plik,'r')
        self.tasma = self.plik.readline()
        self.tasma = list(self.tasma)
        tekst = self.plik.readline()
        self.alfabet = []
        self.stany = dict()
        i = 0
        j = 0
        tekst = tekst.replace("\n","")
        while tekst:
            self.alfabet.append(tekst[0])
            x = self.alfabet[j]
            tekst = tekst.replace(x,"")
            j = j + 1
        tekst = 1
        t1, t2, t3, t4 = 0,0,0,0
        koniec = 0
        indeks = 0
        stan_stanu = 1
        nazwa_stanu = ";"
        while tekst:
            if koniec == 1:
                break
            tekst = self.plik.readline()
            for k in range(len(self.alfabet)):
                    if tekst[0] == self.alfabet[k]:
                        zgodnosc = True
                        break
                    else:
                        zgodnosc = False
                    if tekst[0] == ":":
                        koniec = 1
                        tekst = tekst.replace(":","\n")
                        tekst = "\n"
                        break
            if zgodnosc == False:
                indeks += 1
            if stan_stanu != indeks:
                stan_stanu = indeks
                self.stany[nazwa_stanu] = stany
                nazwa_stanu = ";"
            while tekst[0] != '\n':    
                if zgodnosc:
                    tekst = list(tekst)
                    t1 = tekst[0]
                    tekst.pop(0)
                    tekst.pop(0)
                    t2 = tekst[0]
                    tekst.pop(0)
                    tekst.pop(0)
                    t3 = tekst[0]
                    tekst.pop(0)
                    tekst.pop(0)
                    t4 = tekst[0:len(tekst)]
                    t4 = "".join(t4)
                    t4 = t4.replace("\n","")
                    for x in range(len(tekst)-1):
                        tekst.pop(0)
                    stany.append([t1,t2,t3,t4])
                else:
                    nazwa_stanu = nazwa_stanu.replace(";","")
                    nazwa_stanu += tekst[0]
                    tekst = tekst.replace(nazwa_stanu[i],"")
                    i = i + 1
                    stany = [] 
            i = 0

    def Przejscia(self, stan_aktualny, znak):
        self.tasma[self.glowica] = self.stany[stan_aktualny][self.Numer(stan_aktualny, znak)][1]
        przemieszczenie_glowicy = self.stany[stan_aktualny][self.Numer(stan_aktualny, znak)][2]
        if przemieszczenie_glowicy =='p':
            self.glowica = self.glowica + 1
        elif przemieszczenie_glowicy =='l': 
            self.glowica = self.glowica - 1
        else:
            self.glowica = self.glowica

    def CzyStanPoczątkowy(self, stan):
        return stan == self.stanPoczatkowy

    def CzyStanKoncowy(self, stan):
        return stan == 'koniec'

    def Numer(self, stan, przejscie):
        for i in range(0, len(self.stany[stan])):
            if self.stany[stan][i][0] == przejscie:
                return i

    def Krok(self, znak):
        stan_aktualny = self.stan_tymczasowy
        stan_nastepny = self.stany[stan_aktualny][self.Numer(stan_aktualny, znak)][3]
        self.Przejscia(stan_aktualny,znak)
        self.stan_tymczasowy = stan_nastepny

    def Maszyna(self):
        print(self.tasma, self.glowica)
        while True:
            if (self.CzyStanKoncowy(self.stan_tymczasowy)):
                break
            self.Krok(self.tasma[self.glowica])
            print(self.tasma, self.glowica)


if __name__ == "__main__":
    maszyna = MaszynaTuringa("C:/Users/adaml/OneDrive/Dokumenty/MaszynaTuringa/instrukcja.txt")
    maszyna.Maszyna()
    # Na ten moment instrukcja jest napisana tak, aby odwracała słowo "kot" oraz "ale"
    # Wyjaśnienie działanie instrukcji dla prowadzącego:
    # pierwsza linijka: tasma
    # druga linijka: alfabet (nie może zawierać nazw stanu)
    # trzecia i kolejne linijki: instrukcja:
    # np s1
    # Jest to nazwa stanu
    # np. a b p s2
    # Jest to instrukcja dla maszyny. Jeżeli znak na taśmie to a, to zamienia znak na b, przesuwa się o jeden w prawo i zmienia stan na stan2.
    # Ważne jest, aby na końcu dodać znak ":", który oznacza koniec instrukcji.
    # Wyoknał: Adam Łaziuk oraz Arkadiusz Pajewski
