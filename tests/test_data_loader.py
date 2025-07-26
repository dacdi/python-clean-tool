import pandas as pd
from src.data_loader import load_csv


def test_load_valid_csv(tmp_path):
    # Create a temporary CSV file
    d = tmp_path / "data"
    d.mkdir()
    file = d / "test.csv"
    file.write_text("col1,col2\n1,2\n3,4")

    df = load_csv(filepath=str(file), sep=",")

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["col1", "col2"]
