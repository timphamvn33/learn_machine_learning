from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_FILE = PROJECT_ROOT / "data" / "students.csv"

def load_data():
    return pd.read_csv(DATA_FILE)

def create_features(df):
    df = df.copy()

    # Feature 1: Convert attendance percentage to proportion.
    df["attendance_rate"] = df["attendance"] / 100

    # Feature 2: Allow model to learn a curved study-hours pattern.
    df["study_hours_squared"] = df["hours_studied"] ** 2

    # Featrure 3: Represent a possible interaction between two features
    
    # Feature 4: Group previous scores into categories.
    df["previous_score_band"] = pd.cut(
        df["previous_score"], 
        bins=[-float("inf"), 60, 75, float("inf")],
        labels=["low", "medium", "high"],
        right=False
    )

    return df

def main():
    df = load_data()

    print("Original data:")
    print(df.head())

    featured_df = create_features(df)

    print("\nData with engineered features:")
    print(featured_df.head())

    print("\nFeature columns:")
    print(featured_df.columns.tolist())

    # convert the categories score band to one-hot columns
    encoded_df = pd.get_dummies(featured_df,
                               columns=["previous_score_band"],
                               dtype=int,
                               )

    print("\nData after one-hot encoding:")
    print(encoded_df.head())

    # save the engineered dataset
    output_file = PROJECT_ROOT / "data" / "engineered_student.csv"
    encoded_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()
