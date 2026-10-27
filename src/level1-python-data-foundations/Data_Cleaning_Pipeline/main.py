from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent

RAW_FILE = PROJECT_ROOT / "data" / "raw_customer.csv"
CLEAN_FILE = PROJECT_ROOT / "data" / "clean_customer.csv"

def load_data():
    return pd.read_csv(RAW_FILE)

def clean_customer(df):
    df = df.copy()

    # 1. remove exact duplicate rows.
    df = df.drop_duplicates()

    # 2. clean text columns
    text_columns = ["name", "city", "subscribed"]

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

        # convert empty strings to missing values.
        df[column] = df[column].replace("", pd.NA)

    # 3. standardize city names.
    df["city"] = df["city"].str.title()

    # 4. convert numeric columns: age, monthly_income
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["monthly_income"] = pd.to_numeric(df["monthly_income"], errors="coerce")

    # 5. validate numeric ranges for age and monthly_income
    df.loc[~df["age"].between(0, 120), "age"] = float("nan")
    df.loc[df["monthly_income"] < 0, "monthly_income"] = float("nan")

    # 6.Parse Dates for signup_date
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce",)

    # 7. Standardize the subcription field.
    df["subscribed"] = df["subscribed"].str.lower()

    df["subscribed"] = df["subscribed"].map({
        "yes": True,
        "no": False
    })

    # 8. Remove records without a customer ID
    df = df.dropna(subset=["customer_id"])

    return df

def save_data(df):
    CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_FILE, index=False)

def main():
    raw_df = load_data()
    clean_df = clean_customer(raw_df)

    save_data(clean_df)

    print("Original rows:", len(raw_df))
    print("Cleaned rows:", len(clean_df))
    print("\nMissing values after cleaning:")
    print(clean_df.isna().sum())
    print("\nCleaned data:")
    print(clean_df.to_string(index=False))
    print("\nSaved to:", CLEAN_FILE)

if __name__ == "__main__":
    main()



