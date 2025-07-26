import argparse
import os
from dotenv import load_dotenv

from src.data_loader import load_csv
from src.logger_config import setup_logging
from src.analyze import analyze_dataframe


def main():
    # 🌱 Lade .env-Datei (sucht automatisch im Projektverzeichnis)
    load_dotenv()

    # 🎛️ Argumente definieren mit Fallback auf Umgebungsvariablen
    parser = argparse.ArgumentParser(description="CSV-Tool mit Logging")

    parser.add_argument(
        "--filepath",
        default=os.getenv("CSV_PATH"),
        help="Pfad zur CSV-Datei (z. B. aus .env)",
    )

    parser.add_argument("--sep", default=",", help="Spaltentrenner (Standard: Komma)")

    parser.add_argument(
        "--loglevel",
        default=os.getenv("LOG_LEVEL", "INFO"),
        help="Logging-Level (DEBUG, INFO, WARNING, ERROR)",
    )

    args = parser.parse_args()

    # 🪵 Logging starten
    setup_logging(level=args.loglevel)

    # 🧪 Datei laden
    try:
        df = load_csv(filepath=args.filepath, sep=args.sep)
        print(df.head())
    except Exception as e:
        print(f"Fehler beim Laden der Datei: {e}")

    try:
        df = load_csv(filepath=args.filepath, sep=args.sep)
        analyze_dataframe(df)
    except Exception as e:
        print(f"Fehler beim Laden oder Analysieren der Datei: {e}")


if __name__ == "__main__":
    main()
