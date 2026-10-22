from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_FILE = PROJECT_ROOT / "data" / "expenses.csv"

def load_expenses():
    # load expenses data from expenses.csv file
    df = pd.read_csv(DATA_FILE)

    # can use only the specific columns
    # df = pd.read_csv(DATA_FILE, usecols=["category", "amount"])

    # print("\n print first 5 rows \n", df.head())
    # print("\n print first 3 rows \n", df.head(3))
    # print("\n print last 3 rows \n", df.tail(3))
    # print("\n dataset dimesion \n", df.shape)
    # print("\n print column names \n", df.columns)
    # print("\n data type missing values \n", df.info())
    # print("numerical statistic \n", df.describe())

    # mean = df["amount"].mean()
    # mean_string = f"{mean:.2f}"
    # print("\n get the min \n ", df["amount"].min())
    # print("\n get the max \n", df["amount"].max())
    # print("\n get the mean\n", df["amount"].mean())
    # print("\n get sum\n", sum)
    # print("\n get mean rounded\n", mean_string)

    # print("\n get amount spent more than 50 \n", df[df["amount"] > 50])

    # -----------------------------part 2: clean the data
    # datasets are rarely perfect. they may contain missing values, duplicates transactions, inconsistent category names,
    # invalid amounts, or dates in wrong format

    # invalid date/time errors=coerce will return NaT to invalid dates
    dates = pd.to_datetime(df["date"], errors="coerce")
    print(dates)

    # invalid numerical values
    amount = pd.to_numeric(df["amount"], errors="coerce")
    print(amount)

    # return a boolean dataframe showing which cells are missing
    print(df.isna())
    print(df.isna().sum())

    #  fill the missing value with the unknown
    df["description"] = (df["description"].fillna("Unknown"))

    # find the duplicate
    print(df.duplicated())
    print(df.duplicated().sum())

    # remove the duplicate
    df = df.drop_duplicates()

    # remove the trailing white space
    df["category"]= df["category"].str.strip()

    return df

def main():
    # -----------------------------part 1: statistic the data
    expenses = load_expenses()

    # result = expenses[(expenses["category"] == "Dining") & (expenses["amount"] > 30)]
    # print("\n get expenses in dining and amount more than 30\n")
    # print(result)

    # count transaction by category
    # print(expenses["category"].value_counts())

    # # group by category and sort by the amount
    # print(expenses.groupby("category")["amount"].sum().sort_values(ascending=False))

    # # You can also calculate several statistics at once: 
    # summary = expenses.groupby("category").agg(
    # total_spending=("amount", "sum"),
    # average_transaction=("amount", "mean"),
    # transaction_count=("amount", "count"),)
    # print(summary)

    print(expenses)




if __name__ == "__main__":
    main()