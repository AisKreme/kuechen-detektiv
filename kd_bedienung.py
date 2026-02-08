import readchar
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
        print("6: Produkt bearbeiten")
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
        if auswahl not in (1, 2, 3, 4, 5, 6):
            print(
                "Fehler: Bitte eine gültige Option (1, 2, 3, 4, 5, 6 oder ENTER) wählen."
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
    menge = input(f"Wie viele {produkt.capitalize()} sollen {eingabe} werden? ").strip()
    # Menge überprüfen
    if not menge.isdigit():
        print("Bitte eine Zahl eingeben.")
        menge = None

    return produkt, menge


# FUNKTION FÜR KALORIEN & MINDESTMENGE


def eingabe_produkt_zusatz(produkt):
    # Kalorien Abfrage
    kalorien = input(
        f"Wie viele Kalorien sollen {produkt.capitalize()} haben? "
    ).strip()
    if not kalorien.isdigit():
        print("Bitte eine Zahl eingeben.")
        kalorien = None

    # Mindesmenge Abfage eines Produkts
    mindest_menge = input(
        f"Wie viele {produkt.capitalize()} sollen mindestens vorhanden sein? "
    ).strip()

    # Mindesmenge überprüfen
    if not mindest_menge.isdigit():
        print("Bitte eine Zahl eingeben.")
        mindest_menge = None

    return kalorien, mindest_menge


# Neue Funktion: Produkt bearbeiten
def edit_product(inventar: dict) -> None:
    # Produkt auswählen
    produktAlt = input("Welches Produkt soll bearbeitet werden? ").strip().lower()

    if not produktAlt:
        print("Abbruch: Kein Produkt angegeben.")
        return

    if produktAlt not in inventar:
        print("Fehler: Produkt nicht im Inventar vorhanden.")
        return

    produktItem = inventar[produktAlt]

    # Neuen Namen abfragen
    produktNeu = (
        input(f'Neuer Produktname (ENTER für "{produktItem.produktname}"): ')
        .strip()
        .lower()
    )
    if produktNeu:
        produktItem.produktname = produktNeu
        inventar[produktNeu] = produktItem
        inventar.pop(produktAlt)

    # Neue Menge abfragen
    neueMenge = input(
        f"Neue Menge (aktuell {produktItem.menge}, ENTER zum Behalten): "
    ).strip()
    if neueMenge:
        if neueMenge.isdigit():
            menge_int = int(neueMenge)
            # if menge_int <= 0:
            #     inventar.pop(produktItem.produktname)
            #     print("Produkt wurde entfernt, da die Menge <= 0 ist.")
            # else:
            #     produktItem.menge = menge_int
            if menge_int <= 0:
                # Interaktive Auswahl "Behalten" / "Löschen"
                options = ["Behalten", "Löschen"]
                selected = 0
                print("\nMenge ist ≤ 0. Bitte wählen Sie:")
                while True:
                    # Anzeige der Optionen
                    display = ""
                    for i, option in enumerate(options):
                        if i == selected:
                            display += f"[{option}] "
                        else:
                            display += f" {option}  "
                    print("\r" + display, end="", flush=True)

                    key = readchar.readkey()
                    if key == readchar.key.LEFT:
                        selected = (selected - 1) % len(options)
                    elif key == readchar.key.RIGHT:
                        selected = (selected + 1) % len(options)
                    elif key == readchar.key.ENTER:
                        print()  # Neue Zeile nach Auswahl
                        break
                if options[selected] == "Löschen":
                    inventar.pop(produktItem.produktname)
                    print("Produkt wurde entfernt, da Menge ≤ 0 gewählt wurde.")
                    return
                else:
                    # Behalten gewählt: Menge nicht ändern
                    pass
            else:
                produktItem.menge = menge_int
        else:
            print("Ungültige Menge – Wert bleibt unverändert.")

    # Neue Kalorien abfragen
    neueKalorien = input(
        f"Neue Kalorien (aktuell {produktItem.kalorien}, ENTER zum Behalten): "
    ).strip()
    if neueKalorien:
        if neueKalorien.isdigit():
            produktItem.kalorien = int(neueKalorien)
        else:
            print("Ungültige Kalorien – Wert bleibt unverändert.")

    # Neue Mindestmenge abfragen
    neueMindestmenge = input(
        f"Neue Mindestmenge (aktuell {produktItem.mindestmenge}, ENTER zum Behalten): "
    ).strip()
    if neueMindestmenge:
        if neueMindestmenge.isdigit():
            mindest_int = int(neueMindestmenge)
            # if mindest_int <= 0:
            #     print("Ungültige Mindestmenge – Wert bleibt unverändert.")
            if mindest_int <= 0:
                # Interaktive Auswahl "Behalten" / "Löschen"
                options = ["Behalten", "Löschen"]
                selected = 0
                print("\nMindestmenge ist ≤ 0. Bitte wählen Sie:")
                while True:
                    # Anzeige der Optionen
                    display = ""
                    for i, option in enumerate(options):
                        if i == selected:
                            display += f"[{option}] "
                        else:
                            display += f" {option}  "
                    print("\r" + display, end="", flush=True)

                    key = readchar.readkey()
                    if key == readchar.key.LEFT:
                        selected = (selected - 1) % len(options)
                    elif key == readchar.key.RIGHT:
                        selected = (selected + 1) % len(options)
                    elif key == readchar.key.ENTER:
                        print()  # Neue Zeile nach Auswahl
                        break
                if options[selected] == "Löschen":
                    inventar.pop(produktItem.produktname)
                    print("Produkt wurde entfernt, da Mindestmenge ≤ 0 gewählt wurde.")
                    return
                else:
                    # Behalten gewählt: Mindestmenge nicht ändern
                    pass
            else:
                produktItem.mindestmenge = mindest_int
        else:
            print("Ungültige Mindestmenge – Wert bleibt unverändert.")

    # Produkt löschen, falls Menge <= 0
    # if produktItem.menge <= 0:
    #     inventar.pop(produktItem.produktname)
    #     print("Produkt wurde entfernt, da die Menge <= 0 ist.")


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

                # kalorien, mindest_menge = eingabe_produkt_zusatz(produkt)

                # NEUER CODE:
                # Zusatzdaten (Kalorien & Mindestmenge) NUR abfragen,
                # wenn das Produkt noch nicht im Inventar existiert
                if produkt.strip().lower() not in inventar:
                    kalorien, mindest_menge = eingabe_produkt_zusatz(produkt)
                else:
                    kalorien = None
                    mindest_menge = None
                # -------

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

            case 6:
                edit_product(inventar)
            # Default
            case _:
                return
