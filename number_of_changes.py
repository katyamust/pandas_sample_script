import numpy as np
import pandas as pd

def calculate_value_change(serie):

    if serie.unique().__len__() == 1:
        return 0

    serie_shifted = np.roll(serie, -1)

    #total_changed = np.sum( serie[:-1] != serie_shifted[:-1] )
    total_changed = np.count_nonzero(serie[:-1] ^ serie_shifted[:-1])

    return total_changed

if __name__ == "__main__":
    #x = [1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3]
    #x = np.array([1,1,1,10,1,1,1,1,1,1,2,2,2,2,2,2,2,3,1])

    #x = range(1,100)

    #x = pd.Series([1, 1, 1, 1, 1, 1, 1, 1, 1])
    x = pd.Series([1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3])
    n = calculate_value_change(x)
    print('Value changed in this array')
    print(x)
    print(n)

