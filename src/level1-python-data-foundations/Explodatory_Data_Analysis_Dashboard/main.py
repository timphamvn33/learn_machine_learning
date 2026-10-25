from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_FILE = PROJECT_ROOT / "data" / "students.csv"

def load_data():
    return pd.read_csv(DATA_FILE)

def main():
    df = load_data()

    print("\n raw data: ")
    print(df)

    print("\n colums to list: ")
    print(df.columns.tolist())

    print("\n data type and missing value: ")
    print(df.info())

    print("\nsummary statistic: ")
    print(df.describe())

if __name__ == "__main__":
    main()