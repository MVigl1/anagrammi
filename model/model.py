from functools import lru_cache


class Model:
    def __init__(self):
        _anagrammi = set()

    def calcola_anagrammi(self, word):
        self._anagrammi = set()
        lettere_rimanenti =word
        parziale=""
        self.ricorsione(word, lettere_rimanenti, parziale)
        return self._anagrammi

    def ricorsione(self, word, lettere_rimanenti, parziale):
        if len(lettere_rimanenti) == 0:
            self._anagrammi.add(parziale)
            #print(f"----------------ANAGRAMMA {parziale}")

        else:
            for i in range(len(word)):
                parziale += word[i]
                #print(f"il parziale è {parziale}")
                lettere_rimanenti = word[:i] + word[i+1:]
                #print(f"rimangono queste lettere {lettere_rimanenti}")
                self.ricorsione(lettere_rimanenti, lettere_rimanenti, parziale)
                parziale = parziale[:-1]



if (__name__ == '__main__'):
    model = Model()
    print(model.calcola_anagrammi("dog"))
