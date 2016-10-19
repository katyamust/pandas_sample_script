import pandas as pd
import numpy as np

def pandas_to_list(original_df):

    # list of column names
    print('list of column names')
    columns_list = original_df.columns.tolist()
    print(columns_list)

    # dataframe of first 4 columns of original dataframe
    print('dataframe of first 4 columns of original dataframe (first 10 rows)')
    first4_columns_df = original_df[columns_list[0:4]]
    print(first4_columns_df.head(10))

    print('list of first 4 columns of original dataframe')
    x = first4_columns_df.values.tolist()
    print(x)

    print('list of values a named column A')
    y = original_df['A'].values.tolist()
    print(y)

    print('list of last 2 column values')
    ncols = original_df.shape[1]
    two_last_cols_df = original_df[ columns_list[ncols-2 : ncols] ]

    print('dataframe of last 2 columns of original dataframe (first 10 rows)')
    print(two_last_cols_df.head(10))

    print('last 2 columns of original dataframe')
    print(two_last_cols_df.columns.tolist())
    y1 = two_last_cols_df.values.tolist()
    print(y1)

if __name__ == "__main__":

    df = pd.DataFrame(np.random.randint(0,100,size=(100, 9)), columns=list('ABCDEFGHK'))


    pandas_to_list(df)




