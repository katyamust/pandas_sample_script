import pandas as pd
import string
import random
import numpy as np

def pandas_df_column_str_to_numeric( df, str_column_name ):

    grouped = df.groupby(df[str_column_name])
    df_dict = grouped.groups

    d = dict.fromkeys(df_dict.keys())

    dkeys = d.keys()
    i = 0
    for key in dkeys:
        d[key] = i
        i += 1

    df[str_column_name] = df[str_column_name].map(d)

    # this also works but very slow:
    # df[str_column_name].replace(d, inplace=True)

    return df


if __name__ == "__main__":

    # generate random characters array
    strArr = np.empty((100,9),dtype=str)
    for i in range(0,100):
        strArr[i] = random.choice(string.ascii_letters)

    char = random.choice(string.ascii_letters)

    # sample DataFrame: 9 columns by 100 rows
    df = pd.DataFrame(strArr, columns=list('ABCDEFGHK'))

    # replace string values of column C to numeric values
    df = pandas_df_column_str_to_numeric(df, 'C' )

    print('Success')