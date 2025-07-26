# tests/test_analyze.py
import pandas as pd
import pytest
from src.analyze import analyze_dataframe


def test_analyze_valid_dataframe():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [None, 1, 1]})
    # no error should occur
    analyze_dataframe(df)  # just make sure it runs


def test_analyze_empty_dataframe():
    df = pd.DataFrame()
    analyze_dataframe(df)  # should log a warning, but not fail


def test_analyze_invalid_input():
    with pytest.raises(AttributeError):  # because .columns will fail
        analyze_dataframe(None)
