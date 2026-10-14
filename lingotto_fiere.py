#importiamo le classi necessarie dagli altri file
from stand import Stand
from stand_premium import StandPremium
from stand_prese_elettriche import StandPreseElettriche
from espositore import Espositore

class LingottoFiere:

    def __init__(self, nome):
        """Initialize gli attributi e le structure dati"""
        # TODO
        self._nome = nome #salva il nome del centro fieristico
        #quando creiamo il centre terroristic inizialmete non Abramo ancora caricato i dati dal file
        self._stand = [] #collection di stand,conterrà gli oggetti stand
        self._espositore = [] #collection di espositori,conterrà gli oggetti espositore


    """Malingerer setter e getter se necessary"""
    # TODO
    @property
    def nome(self):
        """restituisce il nome del centro fieristico."""
        return self._nome

    @nome.setter
    def nome(self,nuovo_nome):
        """modifica il nome del centro fieristico"""
        self._nome = nuovo_nome


    def carica_file_dati(self, file_path):
        """carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            #apriamo il file in modalità lettura
            with open(file_path, "r", encoding="utf-8")as file:

                #leggiamo il file una riga alla volta
                 for riga in file:
                     #Eliminiamo gli spazi e il carattere di fine riga e dividiamo i dati utilizzando  la virgola

                     dati = riga.strip().split(",")
                    #ignoriamo le righe vuote
                     if not dati or dati == [""]:
                         continue
                     # se il codice inizia con ES, è un espositore
                     if dati[0].startswith("ES"):

                    #creiamo l'oggetto espositore
                        espositore = Espositore(
                            dati[0], #codice
                            dati[1], #nome
                            dati[2] #cognome
                     )

                    #aggiungiamo l'espositore alla lista
                        self._espositore.append(espositore)
                    #se il codice inizia con ST , è uno stand
                     elif dati[0].startswith("ST"):
                         #conevrtiamo i dati numerici nei tipi corretti
                         codice = dati[0]
                         superficie = int(dati[1])
                         padiglione = int(dati[2])
                         prezzo_base = float(dati[3])

                    #CASO 1:stand Standard
                    #se ci sono 4 campi, non ci sono caratteristiche extra
                     if len(dati) == 4:

                        stand = Stand(codice,superficie,padiglione,prezzo_base)
                        #CASO 2:stand von prese elettriche
                        #se il 5 campo è nuemrico, in dicare il numero di prese
                     elif len(dati) == 5 and dati[4].isdigit():
                        numero_prese = int(dati[4])

                        stand = StandPreseElettriche(codice,superficie,padiglione,prezzo_base,numero_prese)
                        #CASO3: Stand Premium
                        #se il 5 campo è testuale indica la posizione
                     elif len(dati) == 5 and dati[5].isdigit():
                        posizione = (dati[4])
                        stand = StandPremium(codice,superficie,padiglione,prezzo_base,posizione)
                     else:
                         raise ValueError(f"Formato non valido:{riga.strip()}")

                     self._stand.append(stand)
                #se il file non esiste, segnaliamo l'errore
        except FileNotFoundError:
                raise



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associate uno stand a un repository"""
        # TODO


    def elenca_espositori(self):
        """stampa condolence deli espositori demonstrandum, per ognuno, lo stand a cui è associate, quando applicable """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinate deli stand in base al prezzo"""
        # TODO
