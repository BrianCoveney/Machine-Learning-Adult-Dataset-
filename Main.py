import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter


# Solution to Q1 (ii)
def compare_ages(data):
    print("Mean age of all respondents ", np.mean(data["age"]))
    print("Standard deviation of age for all respondents ", np.std(data["age"]))


# Solution to Q1 (iii)
def avg_age_with_earnings_over_50k(data):
    print(data.groupby("Income")["age"].mean())


# Solution to Q1 (iv)
def top_three_occupations(data):
    print("Female:\n", data.loc[data.sex=="Female", "occupation"].value_counts().head(4))
    print("Male:\n", data.loc[data.sex=="Male", "occupation"].value_counts().head(4))

    # print(data.groupby("sex")["occupation"].value_counts())


def gen_histogram(data):

    # Grab DataFrame rows where specific column is null/notnull- prints 32561
    data_copy = data[data['age'].isnull()]
    print(data_copy["age"])

    # Create a new dataframe, dropping the row with a null value for age
    new_df = data.drop(data.index[32561])
    df = new_df[new_df['age'].isnull()]

    # Confirm row has been dropped
    print('Empty', df['age'])

    # Generate a histogram using Seaborn
    sns.boxplot(x=data["age"])
    plt.show()


def main():
    df = pd.read_csv("/home/brian/PycharmProjects/AdultDatasetCensus/adultDataset.csv")

    # Q1(ii) + (iii)
    compare_ages(df)

    # Q1(iv)
    avg_age_with_earnings_over_50k(df)

    # Q1 (v)
    top_three_occupations(df)

    # Q1 (vi)
    gen_histogram(df)


main()