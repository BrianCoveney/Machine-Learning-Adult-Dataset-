import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter


# Solution to Q1 (ii)
def compare_ages(dataframe):
    print("Mean age of all respondents ", np.mean(dataframe["age"]))
    print("Standard deviation of age for all respondents ", np.std(dataframe["age"]))


# Solution to Q1 (iii)
def avg_age_with_earnings_over_50k(data):
    print(data.groupby("Income")["age"].mean())


# Solution to Q1 (iv)
def top_three_occupations(dataframe):
    print("Female:\n", dataframe.loc[dataframe.sex == "Female", "occupation"].value_counts().head(4))
    print("Male:\n", dataframe.loc[dataframe.sex == "Male", "occupation"].value_counts().head(4))

    # print(data.groupby("sex")["occupation"].value_counts())


# Solution to Q1 (v), (vi) and (vii)
def analyse_age_col(dataframe):
    # Grab DataFrame rows where specific column is null/notnull- prints 32561
    data_copy = dataframe[dataframe['age'].isnull()]
    print(data_copy["age"])

    # Create a new dataframe, dropping the row with a null value for age
    df_null_age_dropped = dataframe.drop(dataframe.index[32561])

    # Confirm row has been dropped
    df_age_dropped_proof = df_null_age_dropped[df_null_age_dropped['age'].isnull()]
    print('Empty', df_age_dropped_proof['age'])

    # Generate a histogram
    # sns.distplot(df_null_age_dropped['age'])

    # Generate a boxpolt to identify outliers
    # sns.boxplot(x=df_null_age_dropped["age"])

    df_outliers_removed = df_null_age_dropped[df_null_age_dropped.age<100]
    sns.distplot(df_outliers_removed['age'])
    #plt.show()


def analyse_features(dataframe):
    # df_str_replaced = data.replace({'Income' : {'<=50K' : 0, '>50K' : 1}})

    df_str_replaced = dataframe.replace('<=50K', 1).replace('>50K', 2)

    # Create a scatter plot
    sns.lmplot(x='education-num', y='Income', hue='sex', data=df_str_replaced, x_estimator=np.mean)
    plt.show()


def main():
    df = pd.read_csv("/home/brian/PycharmProjects/AdultDatasetCensus/adultDataset.csv")

    # Q1(ii) + (iii)
    compare_ages(df)

    # Q1(iv)
    avg_age_with_earnings_over_50k(df)

    # Q1 (v)
    top_three_occupations(df)

    # Q1 (vi), (vi) and (vii)
    analyse_age_col(df)

    # Q1 (viii)
    analyse_features(df)


main()
