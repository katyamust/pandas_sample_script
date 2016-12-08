import numpy as np
import pandas as pd

import timeit

def calculate_value_changes(serie):

    if serie.unique().__len__() == 1:
        return 0

    serie_shifted = np.roll(serie, -1)

    #total_changed = np.sum( serie[:-1] != serie_shifted[:-1] )
    total_changed = np.count_nonzero(serie[:-1] ^ serie_shifted[:-1])

    return total_changed


"""
Fast function calculating number changes in array

Improvement to previous function:

1.
pandas.Series used as input( usually input comes pandas series type as slice from pandas.DataFrame )
then converted to numpy series as working with numpy series is up t 10 times faster.

2. If input is in floats array it is converted int as xor works only with int,
otherwise we would have to do boolean comparison that is slow

"""
def calculate_value_chagnes_fast(fserie):

    serie = fserie.astype(int)

    if serie.unique().__len__() == 1:
        return 0

    serie_shifted_values = np.roll(serie.values, -1)

    num_series = serie.values[:-1] ^ serie_shifted_values[:-1]
    #total_changed = num_series.nonzero()[0].size
    total_changed = np.count_nonzero(num_series)

    return total_changed


if __name__ == "__main__":
    #x = [1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3]
    #x = np.array([1,1,1,10,1,1,1,1,1,1,2,2,2,2,2,2,2,3,1])

    #x = range(1,100)

    #x = pd.Series([1, 1, 1, 1, 1, 1, 1, 1, 1])

    start = timeit.default_timer()
    x = pd.Series([1, 1, 1, 10.4, 1.3, 1.5, 1.0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3])
    n = calculate_value_changes(x)
    print('Done.{0:f}'.format(timeit.default_timer() - start))

    start = timeit.default_timer()
    x1 = pd.Series([1, 1, 1, 1, 1, 1, 1, 1, 1])
    x1 = pd.Series([1, 1, 1, 10.4, 1.3, 1.5, 1.0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3])
    n = calculate_value_chagnes_fast(x1)
    print('Done.{0:f}'.format(timeit.default_timer() - start))

    print('Value changed in this array')
    print(x)
    print(n)

