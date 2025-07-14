import pandas as pd
import logging

# Modul-spezifischer Logger (folgt zentraler Konfiguration)
logger = logging.getLogger(__name__)

def load_csv(filepath: str, sep: str = ",") -> pd.DataFrame:
    """
    Load a CSV file and return its contents as a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file.
        sep (str): Column separator (default: ',')

    Returns:
        pd.DataFrame: Loaded data.

    Raises:
        FileNotFoundError: If the file is not found.
        pd.errors.ParserError: If the file cannot be parsed as CSV.
    """
    try:
        df = pd.read_csv(filepath, sep=sep)
        logger.info(f"✅ Datei geladen: '{filepath}' ({df.shape[0]} Zeilen, {df.shape[1]} Spalten)")
        return df
    except FileNotFoundError:
        logger.error(f"❌ Datei nicht gefunden: '{filepath}'")
        raise
    except pd.errors.ParserError:
        logger.error(f"❌ Parsing-Fehler in Datei: '{filepath}'")
        raise
