class ProduktItem:
    # Konstruktor: wird aufgerufen, wenn ein neues Item erzeugt wird
    def __init__(
        self, produktname: str, menge: int, kalorien: int, mindestmenge: int
    ) -> None:
        # Produktname speichern
        self.produktname: str = produktname

        # Eigenschaften speichern
        self.menge: int = menge
        self.kalorien: int = kalorien
        self.mindestmenge: int = mindestmenge

    # Prüft, ob die aktuelle Menge unter der Mindestmenge liegt
    def ist_unter_mindestmenge(self) -> bool:
        return self.menge <= self.mindestmenge

    # Menge erhöhen
    def erhoehe_menge(self, menge: int) -> None:
        self.menge += menge

    # Menge verringern (nicht unter 0)
    def verringere_menge(self, menge: int) -> None:
        self.menge -= menge
        if self.menge <= 0:
            self.menge = 0
