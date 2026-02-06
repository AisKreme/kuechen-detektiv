# Funktionalität

# Neue, verschachtelte Dictionary-Variante für add_item
def add_item(inventar, produktname, menge=1, kalorien=1, mindestmenge=0):
    # Produktname vereinheitlichen (Trimmen + klein schreiben)
    schluessel = produktname.strip().lower()

    # Leere Eingabe abfangen
    if not schluessel:
        print("Fehler: Kein Produktname angegeben.")
        return

    # Falls das Produkt noch nicht im Inventar existiert,
    # wird ein neues Dictionary mit Standardwerten angelegt
    if schluessel not in inventar:
        inventar[schluessel] = {
            "Menge": 0,
            "Kalorien": 0,
            "Mindestmenge": 0,
        }

    # Aktuelle Menge aus dem inneren Dictionary holen
    aktuelleMenge = inventar[schluessel].get("Menge", 0)
    # Menge erhöhen
    inventar[schluessel]["Menge"] = aktuelleMenge + int(menge)

    # Aktuelle Kalorien aus dem inneren Dictionary holen
    aktuelleKalorien = inventar[schluessel].get("Kalorien", 0)
    # Kalorien erhöhen
    inventar[schluessel]["Kalorien"] = aktuelleKalorien + int(kalorien)

    # Aktuelle Mindesmenge aus dem inneren Dictionary holen
    aktuelleMindestMenge = inventar[schluessel].get("Mindestmenge", 0)
    # Mindesmenge erhöhen
    inventar[schluessel]["Mindestmenge"] = aktuelleMindestMenge + int(mindestmenge)


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

    # Aktuelle Menge aus dem inneren Dictionary holen
    aktuelleMenge = inventar[schluessel].get("Menge", 0)

    # Menge reduzieren
    neueMenge = aktuelleMenge - int(menge)

    # Menge darf nicht negativ werden
    if neueMenge < 0:
        neueMenge = 0

    # Neue Menge im inneren Dictionary speichern
    inventar[schluessel]["Menge"] = neueMenge

    # Produkt entfernen, wenn Menge 0 ist
    if inventar[schluessel]["Menge"] == 0:
        inventar.pop(schluessel)


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

    print("Kühlschrank-Inventar (Ampel-Status):")

    # Produkte alphabetisch ausgeben
    for produkt in sorted(inventar):
        print(f"\n-> {produkt.title()}:")

        # Inneres Dictionary holen
        produktDaten = inventar[produkt]

        # Werte sicher auslesen
        menge = produktDaten.get("Menge", 0)
        mindestmenge = produktDaten.get("Mindestmenge", 0)

        # Ampel-Logik
        if menge <= mindestmenge:
            statusText = "ROT"
            statusFarbe = rot
        elif menge <= mindestmenge + 1:
            statusText = "GELB"
            statusFarbe = gelb
        else:
            statusText = "GRÜN"
            statusFarbe = gruen

        # Farbigen Status ausgeben
        print(f"  Status: {statusFarbe}{statusText}{reset}")

        # Eigenschaften ausgeben
        for eigenschaft, wert in produktDaten.items():
            print(f"  - {eigenschaft}: {wert}")
