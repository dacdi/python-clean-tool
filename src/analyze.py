import pandas as pd
import logging


def analyze_dataframe(df: pd.DataFrame) -> None:
    """
    Analyze a DataFrame: log basic statistics and check for missing values.

    Args:
        df (pd.DataFrame): The input DataFrame to analyze.
    """
    logger = logging.getLogger(__name__)

    try:
        logger.info("Starting analysis of DataFrame")

        logger.info("Column names: %s", list(df.columns))
        logger.info("Number of rows: %d", len(df))

        if df.empty:
            logger.warning("The DataFrame is empty")
            return

        # Basic statistics
        logger.info("Calculating column means...")
        means = df.mean(numeric_only=True)
        logger.info("Column means:\n%s", means)

        # Check for missing values
        missing = df.isnull().sum()
        if missing.any():
            logger.warning("Missing values found:\n%s", missing)
        else:
            logger.info("No missing values found")

    except Exception as e:
        logger.error("Error during analysis: %s", e)
        raise

    logger.info("Describe:\n%s", df.describe())
