import json
from pathlib import Path

from produktitem import ProduktItem

# Konstante mit Pfad zur JSON-Datei
FILE_PATH = Path(__file__).parent / "inventory.json"


# Speichern des Dictionary in JSON-Datei
def save_inventory(inventory: dict, path=FILE_PATH) -> None:
    jsonDaten: dict = {}

    for produktname, produktItem in inventory.items():
        jsonDaten[produktname] = {
            "Menge": produktItem.menge,
            "Kalorien": produktItem.kalorien,
            "Mindestmenge": produktItem.mindestmenge,
        }

    with path.open("w", encoding="utf-8") as file:
        json.dump(jsonDaten, file, ensure_ascii=False, indent=2)
    # Rückmeldung über Speicherung
    print("Inventar gespeichert in:", path.name)


# Laden des Dictionary aus einer JSON-Datei
def load_inventory(path=FILE_PATH) -> dict:
    inventar: dict = {}

    # Pfad existiert nicht
    if not path.exists():
        print("Datei wurde nicht gefunden.")
        return inventar

    try:
        # Datei öffnen und Daten laden
        with path.open("r", encoding="utf-8") as file:
            daten = json.load(file)

        # Daten überprüfen
        if not isinstance(daten, dict):
            print("Ungültiges Datenformat. Start mit leerem Inventar.")
            return inventar

        for produktname, produktDaten in daten.items():
            if not isinstance(produktDaten, dict):
                continue

            inventar[produktname] = ProduktItem(
                produktname=produktname,
                menge=int(produktDaten.get("Menge", 0)),
                kalorien=int(produktDaten.get("Kalorien", 0)),
                mindestmenge=int(produktDaten.get("Mindestmenge", 0)),
            )

        # korrekte Daten zurückgeben
        print(f"Inventar aus Datei {path.name} geladen.")
        return inventar
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError):
        print("JSON beschädigt oder unlesbar. Start mit leerem Inventar.")
        return {}
