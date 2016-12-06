import numpy as np
import pandas as pd

def calculate_value_change(serie):

    if serie.unique().__len__() == 1:
        return 0

    serie_shifted = np.roll(serie, -1)
    total_changed = np.sum(serie != serie_shifted) - 1
    return total_changed

#(a and not b) or (not a and b)


if __name__ == "__main__":

    #x = np.array([1,1,1,10,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3])
    #x = range(1,100)

   # x = pd.Series([1, 1, 1, 1, 1, 1, 1, 1, 1])
    x = pd.Series([1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3])
    n = calculate_value_change(x)
    print('Value changed in this array')
    print(x)
    print(n)
