# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 14:34:24 2021

@author: hwz62
"""

import matplotlib.pyplot as plt

histbins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# histogram of Harvard scores
fig = plt.hist(harvardRaw, bins = 10)
plt.axvline(x=0.632, color='r', linestyle='dashed', linewidth=2)

x = clinicians[clinicians.reviewer==1].harvardscore
y = clinicians[clinicians.reviewer==2].harvardscore
plt.hist(x, histbins, alpha=0.5, label='Positive')
plt.hist(y, histbins, alpha=0.5, label='Negative')
plt.legend(loc='upper right')
plt.axvline(x=0.632, color='r', linestyle='dashed', linewidth=2)
plt.title('PheKB Scores on Reviewed Cases')
plt.show()

# Spread of scores with RA+ v RA- (two hists on top of each other)