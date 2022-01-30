import pandas as pd


def main():
    pd.set_option('display.max_columns', 8)

    # Read in the data
    general = pd.read_csv('../task/test/general.csv')
    prenatal = pd.read_csv('../task/test/prenatal.csv')
    sports = pd.read_csv('../task/test/sports.csv')

    # Rename for clarity and overlapping columns
    prenatal.rename(columns={"HOSPITAL": "hospital", "Sex": "gender"}, inplace=True)
    sports.rename(columns={"Hospital": "hospital", "Male/female": "gender"}, inplace=True)

    # Merge all the DataFrame
    concat_df = pd.concat([general, prenatal, sports], ignore_index=True)
    concat_df.drop(columns=["Unnamed: 0"], inplace=True)
    print(pd.DataFrame.sample(n=20, random_state=30, self=concat_df))


if __name__ == "__main__":
    main()
