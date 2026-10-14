class Espositore:

    def __init__(self, codice_E,nome, cognome):
        self._codice_E = codice_E
        self._nome = nome
        self._cognome = cognome

    def __str__(self):
        return f"{self._codice}: {self._nome} {self._cognome}"
