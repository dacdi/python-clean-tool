# 🧼 Python Clean Tool

Ein kleines Python-Tool zur Analyse von CSV- oder JSON-Dateien.  
Es zeigt den Einsatz von Clean Code, Logging, Tests und Git-Dokumentation.

## 🧰 Features

- Einlesen von CSV-Daten
- Logging & Fehlerbehandlung
- Saubere Funktionsstruktur
- Vorbereitung auf Unit-Tests
- Reproduzierbare Projektstruktur

## 🛠️ Setup

1. Projekt klonen (wenn online) oder lokal öffnen  
2. Virtuelle Umgebung erstellen:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Beispiel ausführen
python src/main.py

python-clean-tool/
│
├── src/          # Quellcode (z. B. data_loader.py)
├── tests/        # Tests (folgt in Woche 3)
├── data/         # Eingabedaten (CSV/JSON)
├── .venv/        # Virtuelles Environment (nicht in Git)
├── .gitignore
├── requirements.txt
└── README.md
