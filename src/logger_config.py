import logging


def setup_logging(level: str = "INFO"):
    """
    Zentrale Logging-Konfiguration für das Projekt.

    Args:
        level (str): Log-Level als Text (z. B. "DEBUG", "INFO", "WARNING").
    """
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Ungültiger Log-Level: {level}")

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
