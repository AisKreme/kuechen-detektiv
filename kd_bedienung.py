from kd_funktion import add_item, remove_item, show_inventory
from kd_json import load_inventory, save_inventory


# TODO: Bei mehr Funktionen anpassen
def show_menu():
    while True:
        print("--- Wähle bitte die gewünschte Funktion ---")
        print("1: Produkt hinzufügen")
        print("2: Produkt entfernen")
        print("3: Inventar anzeigen")
        print("4: Speichern des Inventars")
        print("5: Laden des Inventars")
        print("ENTER zum Beenden")

        eingabe = input("Deine Auswahl: ")

        # Programm beenden bei leerer Eingabe
        if not eingabe:
            return None
        # Eingabe muss eine Zahl sein
        if not eingabe.isdigit():
            print("Fehler: Bitte eine Zahl eingeben.")
            continue

        # Zahl in Integer umwandeln
        auswahl = int(eingabe)

        # Gültige Menüauswahl prüfen
        if auswahl not in (1, 2, 3, 4, 5):
            print(
                "Fehler: Bitte eine gültige Option (1, 2, 3, 4, 5 oder ENTER) wählen."
            )
            continue

        return auswahl


def eingabe_produkt_menge(eingabe):
    produkt = input("Produktname (oder ENTER zum Beenden): ").strip()

    # Ende bei leerer Eingabe
    if not produkt:
        produkt = None
        return produkt, None

    # Eingabe eines Produkts
    menge = input(f"Wie viele {produkt} sollen {eingabe} werden? ").strip()
    # Menge überprüfen
    if not menge.isdigit():
        print("Bitte eine Zahl eingeben.")
        menge = None

    return produkt, menge


# NEUE FUNKTION FÜR KALORIEN & MINDESTMENGE


def eingabe_produkt_zusatz(produkt):
    # Kalorien Abfrage
    kalorien = input(f"Wie viele Kalorien sollen {produkt} haben? ").strip()
    if not kalorien.isdigit():
        print("Bitte eine Zahl eingeben.")
        kalorien = None

    # Mindesmenge Abfage eines Produkts
    mindest_menge = input(
        f"Wie viele {produkt} sollen mindestens vorhanden sein? "
    ).strip()

    # Mindesmenge überprüfen
    if not mindest_menge.isdigit():
        print("Bitte eine Zahl eingeben.")
        mindest_menge = None

    return kalorien, mindest_menge


# Nutzer die Eingabe von Produkten ermöglichen
def user_input(inventar):
    while True:
        # Bedienungsmenü anzeigen
        funktion = show_menu()

        # Eingabe verarbeiten
        # TODO: An bestehende Funktionen anpassen
        match funktion:
            # Produkt hinzufügen
            case 1:
                produkt, menge = eingabe_produkt_menge("hinzugefügt")
                # Ende bei leerer Eingabe oder keiner Menge
                if produkt == None:
                    break

                kalorien, mindest_menge = eingabe_produkt_zusatz(produkt)

                if menge == None:
                    continue

                # Produkt wird hinzugefügt
                add_item(inventar, produkt, menge, kalorien, mindest_menge)

            # Produkt entfernen
            case 2:
                produkt, menge = eingabe_produkt_menge("entfernt")
                # Ende bei leerer Eingabe
                # Ende bei leerer Eingabe oder keiner Menge
                if produkt == None:
                    break

                if menge == None:
                    continue

                # Produkt entfernen
                remove_item(inventar, produkt, menge)

            # Inventar anzeigen
            case 3:
                show_inventory(inventar)

            # Speichern des Inventars als JSON
            case 4:
                save_inventory(inventar)

            # Laden des Inventars aus JSON
            case 5:
                # inventar = load_inventory()
                # load_inventory gibt ein neues dict zurück
                geladenes_inventar = load_inventory()
                # Inventar leeren
                inventar.clear()
                # Inhalt des neuen dict in Inventar laden
                inventar.update(geladenes_inventar)
                # neues dict löschen
                del geladenes_inventar

            # Default
            case _:
                return
