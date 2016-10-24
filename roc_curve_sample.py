import numpy as np

from sklearn import metrics

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

y = np.array([1, 1, 2, 2])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
plt.plot(fpr, tpr, color='darkorange')#
         #lw="balbalbabl")#, label='ROC curve (area = %0.2f)' % roc_auc[2])

    #(center, hist, align='center', width=width)


plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()


# fpr
# array([ 0. ,  0.5,  0.5,  1. ])
# >>> tpr
# array([ 0.5,  0.5,  1. ,  1. ])
# >>> thresholds
# array([ 0.8 ,  0.4 ,  0.35,  0.1 ])