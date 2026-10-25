
import matplotlib.pyplot as plt
import seaborn as sns

from main import load_data


def plot_exam_score_distribution(df):
    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="exam_score",
        bins=8,
        kde=True,
    )

    plt.title("Distribution of Exam Scores")
    plt.xlabel("Exam Score")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.show()


def plot_study_hours_vs_score(df):
    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="hours_studied",
        y="exam_score",
    )

    plt.title("Study Hours vs Exam Score")
    plt.xlabel("Hours Studied")
    plt.ylabel("Exam Score")
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df):
    numeric_df = df.drop(columns=["student_id"])

    correlation = numeric_df.corr()

    plt.figure(figsize=(9, 6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        fmt=".2f",
    )

    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def main():
    df = load_data()

    plot_exam_score_distribution(df)
    plot_study_hours_vs_score(df)
    plot_correlation_heatmap(df)


if __name__ == "__main__":
    main()
