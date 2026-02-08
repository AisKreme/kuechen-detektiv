# Import
from produktitem import ProduktItem


# Neue, verschachtelte Dictionary-Variante für add_item
def add_item(
    inventar: dict,
    produktname: str,
    menge: int = 1,
    kalorien: int = 0,
    mindestmenge: int = 0,
) -> None:
    # Produktname vereinheitlichen (Trimmen + klein schreiben)
    schluessel: str = produktname.strip().lower()

    # Leere Eingabe abfangen
    if not schluessel:
        print("Fehler: Kein Produktname angegeben.")
        return

    # NEUER CODE
    # Menge prüfen und umwandeln
    try:
        menge = int(menge)
    except ValueError:
        print("Fehler: Menge muss eine Zahl sein.")
        return

    # Produkt nur EINMAL anlegen
    if schluessel not in inventar:
        try:
            kalorien = int(kalorien)
            mindestmenge = int(mindestmenge)
        except ValueError:
            print("Fehler: Kalorien und Mindestmenge müssen Zahlen sein.")
            return

        inventar[schluessel] = ProduktItem(
            produktname=schluessel,
            menge=0,
            kalorien=kalorien,
            mindestmenge=mindestmenge,
        )

    # Menge IMMER zur bestehenden Menge addieren
    inventar[schluessel].erhoehe_menge(menge)

    # ALTER CODE

    ## Falls das Produkt noch nicht im Inventar existiert,
    ## wird ein neues Dictionary mit Standardwerten angelegt
    # if schluessel not in inventar:
    #     inventar[schluessel] = {
    #         "Menge": 0,
    #         "Kalorien": 0,
    #         "Mindestmenge": 0,
    #     }

    ## Aktuelle Menge aus dem inneren Dictionary holen
    # aktuelleMenge = inventar[schluessel].get("Menge", 0)
    # # Menge erhöhen
    # # inventar[schluessel]["Menge"] = aktuelleMenge + int(menge)

    # # Aktuelle Kalorien aus dem inneren Dictionary holen
    # aktuelleKalorien = inventar[schluessel].get("Kalorien", 0)
    # # Kalorien erhöhen
    # inventar[schluessel]["Kalorien"] = aktuelleKalorien + int(kalorien)

    # # Aktuelle Mindesmenge aus dem inneren Dictionary holen
    # aktuelleMindestMenge = inventar[schluessel].get("Mindestmenge", 0)
    # # Mindesmenge erhöhen
    # inventar[schluessel]["Mindestmenge"] = aktuelleMindestMenge + int(mindestmenge)


def remove_item(inventar, produktname, menge=1):
    # Produktname vereinheitlichen (Trimmen + klein schreiben)
    schluessel = produktname.strip().lower()

    # Leere Eingabe abfangen
    if not schluessel:
        print("Fehler: Kein Produktname angegeben.")
        return

    # Prüfen, ob das Produkt überhaupt im Inventar existiert
    if schluessel not in inventar:
        print("Fehler: Produkt nicht im Inventar vorhanden.")
        return

    try:
        menge = int(menge)
    except ValueError:
        print("Fehler: Menge muss eine Zahl sein.")
        return
    # Neu durch Klassen Implementierung
    inventar[schluessel].verringere_menge(menge)

    # Aktuelle Menge aus dem inneren Dictionary holen
    # aktuelleMenge = inventar[schluessel].get("Menge", 0)

    # Menge reduzieren
    # neueMenge = aktuelleMenge - int(menge)

    # Menge darf nicht negativ werden
    # if neueMenge < 0:
    #     neueMenge = 0

    # Neue Menge im inneren Dictionary speichern
    # inventar[schluessel]["Menge"] = neueMenge

    # Produkt entfernen, wenn Menge 0 ist
    # if inventar[schluessel]["Menge"] == 0:
    #     inventar.pop(schluessel)


def show_inventory(inventar):
    # ANSI-Farbcodes für das Terminal
    rot = "\033[91m"
    gelb = "\033[93m"
    gruen = "\033[92m"
    reset = "\033[0m"

    # Prüfen, ob das Inventar leer ist
    if not inventar:
        print("Dein Kühlschrank ist leer.")
        return

    print("Kühlschrank-Inventar:")

    # Produkte alphabetisch ausgeben
    for produkt in sorted(inventar):
        print(f"\n-> {produkt.title()}:")

        produktItem = inventar[produkt]

        # menge = produktItem.menge
        # mindestmenge = produktItem.mindestmenge

        # # Inneres Dictionary holen
        # produktDaten = inventar[produkt]

        # # Werte sicher auslesen
        # menge = produktDaten.get("Menge", 0)
        # mindestmenge = produktDaten.get("Mindestmenge", 0)

        # Ampel-Logik - ALT
        # if menge <= mindestmenge:

        # Ampel-Logik über Methode aus der Klasse
        if produktItem.ist_unter_mindestmenge():
            statusText = "ROT"
            statusFarbe = rot
        # elif menge <= mindestmenge + 1:
        elif produktItem.menge <= produktItem.mindestmenge + 1:
            statusText = "GELB"
            statusFarbe = gelb
        else:
            statusText = "GRÜN"
            statusFarbe = gruen

        # Farbigen Status ausgeben
        print(f"  Status: {statusFarbe}{statusText}{reset}")

        # NEUE AUSGABE
        print(f"  - Menge: {produktItem.menge}")
        print(f"  - Kalorien: {produktItem.kalorien}")
        print(f"  - Mindestmenge: {produktItem.mindestmenge}")

        # ALTE AUSGABE mit For-Loop
        # # Eigenschaften ausgeben
        # for eigenschaft, wert in produktDaten.items():
        #     print(f"  - {eigenschaft}: {wert}")
