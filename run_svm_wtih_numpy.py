import numpy as np
import pandas as pd

from sklearn.svm import SVC

import timeit

if __name__ == "__main__":

    nfeatures = 40
    nrows = 1000000

    start = timeit.default_timer()

    # create 2 dimensional numpy array
    x = np.zeros((nrows, nfeatures), dtype=np.int)

    x[-1,-1] = 19

    y = np.zeros(nrows, dtype=np.int)
    y[-315] = 1

    print("SVC classifier")
    model = SVC()
    x_train = x
    y_train = y
    model.fit(x_train,y_train)

    print('Done.{0:f}'.format(timeit.default_timer() - start))
