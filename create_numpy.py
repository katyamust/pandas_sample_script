import numpy as np
import pandas as pd

import timeit

if __name__ == "__main__":

    nfeatures = 40
    nrows = 1000000

    start = timeit.default_timer()

    # create 2 dimensional numpy array
    n = np.zeros((nrows, nfeatures), dtype=np.int)

    n[-1,-1] = 19

    print('Done.{0:f}'.format(timeit.default_timer() - start))
