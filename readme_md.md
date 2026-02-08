# Küchen-Detektiv

Dies ist ein kleines Python-Projekt, um ein Inventar im Kühlschrank zu verwalten.

## Installation und Setup

### Voraussetzungen
- Python 3.10 oder höher
- pip (für virtuelle Environments)

### 1. Repository klonen
```bash
git clone <repo-url>
cd <repo-verzeichnis>
```

### 2. Virtuelles Environment erstellen

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 4. Projekt starten
```bash
python kd_main.py
```

## Hinweise
- Das virtuelle Environment stellt sicher, dass Pakete wie `readchar` sauber installiert werden, ohne das System-Python zu verändern.
- Wenn das Projekt auf ein anderes System geklont wird, einfach die Schritte 2-4 wiederholen.

## Pakete
- `readchar` → für die interaktive Auswahl in der Konsole über Pfeiltasten.

## Troubleshooting
- Fehler `ModuleNotFoundError: No module named 'readchar'`:
  - Stelle sicher, dass das virtuelle Environment aktiviert ist.
  - Prüfe mit `pip list`, ob `readchar` installiert ist.
  - Unter Homebrew-Python auf macOS darf man **nicht systemweit** pip benutzen. Deshalb unbedingt ein venv verwenden.
  - Windows: Wenn Powershell den Befehl `Activate.ps1` blockiert, kann es sein, dass die Ausführung von Skripten eingeschränkt ist. Führe ggf. aus:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

