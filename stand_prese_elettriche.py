from stand import Stand
# sovrapprezzo pari al 7% per ogni presa extra, ovvero: prezzo finale = prezzo base × (1 + 0.07 × numero_prese)
class StandPreseElettriche(Stand):
    def __init__(self,codice,superficie,padiglione,prezzo_base,numero_prese):
        super().__init(self,codice,superficie,padiglione,prezzo_base)
        self.__numero_prese = numero_prese

    def calcola_prezzo(self):
        return self._prezzo_base * (1 + 0.07 * self.__numero_prese)

    def __str__(self):
        return super().__str__() + f" - Prese aggiuntive:{self.__numero_prese}"