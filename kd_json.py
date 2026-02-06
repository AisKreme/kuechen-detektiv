import json
from pathlib import Path

# Konstante mit Pfad zur JSON-Datei
FILE_PATH = Path(__file__).parent / 'inventory.json'

# Speichern des Dictionary in JSON-Datei
def save_inventory(inventar, pfad=FILE_PATH):
    with pfad.open('w', encoding='utf-8') as datei:
        json.dump(inventar, datei, ensure_ascii=False, indent=2)
    # Rückmeldung über Speicherung
    print('Inventar gespeichert in:', pfad.name)

# Laden des Dictionary aus einer JSON-Datei
def load_inventory(pfad=FILE_PATH):
    # Pfad existiert nicht
    if not pfad.exists():
        print('Datei wurde nicht gefunden.')
        return {}
    
    try:
        # Datei öffnen und Daten laden
        with pfad.open('r', encoding='utf-8') as datei:
            daten = json.load(datei)
        
        # Daten überprüfen
        if not isinstance(daten, dict):
            print('Ungültiges Datenformat. Start mit leerem Inventar.')
            return {}
        
        # korrekte Daten zurückgeben
        print(f'Inventar aus Datei {pfad.name} geladen.')
        return daten
    except (json.JSONDecodeError, UnicodeDecodeError):
        print('JSON beschädigt oder unlesbar. Start mit leerem Inventar.')
        return {}