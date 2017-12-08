import pandas as pd
import numpy as np


if __name__ == "__main__":

    df1 = pd.DataFrame(np.random.randint(0,100,size=(100, 9)), columns=list('ABCDEFGHK'))
    df2 = pd.DataFrame(np.random.randint(222,22222,size=(100, 9)), columns=list('ABCDEFGHK'))
    #df2 = df1.copy()

    print("df1")
    print(df1.shape)
    print(df1.head())

    print("df2")
    print(df2.shape)
    print(df2.tail())

    """
    Compare 2 dataframes
    """
    print("Equals: ", df1.equals(df2))

    """
    Merge 2 dataframes
    """
    merged_df = df1.merge(df2, how='left', indicator=True)
    print("merged_df")
    print(merged_df.shape)

    #merged_df.drop(columns = ["_merge"], inplace=True)
    print(merged_df.head())
    #print(merged_df.tail())

    # only data from  both dataframes
    both_df = merged_df[merged_df['_merge'] == 'both']
    print("both_df")
    print(both_df.shape)
    print(both_df.head())

    # only data from left dataframe
    left_df = merged_df[merged_df['_merge'] == 'left_only']
    print("left_df")
    print(left_df.shape)
    print(left_df.head())
