import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter


# Solution to Q1 (ii) + (iii)
def compare_ages(data):
    print("Mean age of all respondents ", np.mean(data["age"]))
    print("Standard deviation of age for all respondents ", np.std(data["age"]))


# Solution to Q1 (iv)
def avg_age_with_earnings_over_50k(data):
    print(data.groupby("Income")["age"].mean())


# Solution to Q1 (v)
def top_three_occupations(data):
    print("Female:\n", data.loc[data.sex=="Female", "occupation"].value_counts().head(4))
    print("Male:\n", data.loc[data.sex=="Male", "occupation"].value_counts().head(4))

    # print(data.groupby("sex")["occupation"].value_counts())


def main():
    df = pd.read_csv("/home/brian/PycharmProjects/AdultDatasetCensus/adultDataset.csv")

    # Q1(ii) + (iii)
    compare_ages(df)

    # Q1(iv)
    avg_age_with_earnings_over_50k(df)

    # Q1 (v)
    top_three_occupations(df)


main()