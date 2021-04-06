# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:39:31 2021

@author: Casper
"""

import sklearn
from sklearn import datasets
import numpy as np
import csv


GOAL_DIR = "C:\\Users\\Casper\\Projects\\MasterScriptie\\custom_projects\\data\\generated_dataset\\"
N_FEATURES = 9
N_TARGETS = 1

x_all, y_all = sklearn.datasets.make_regression(n_samples=100, 
                                 n_features=N_FEATURES, 
                                 n_informative=4, 
                                 n_targets=N_TARGETS, 
                                 bias=1.23, 
                                 effective_rank=None, 
                                 tail_strength=0.5, 
                                 noise=2, 
                                 shuffle=True, 
                                 coef=False, 
                                 random_state=1)


variables = []
for x in range(N_FEATURES + N_TARGETS):
    variables.append("var_" + str(x+1))
    


for i, (x, y) in enumerate(zip(x_all, y_all)):
    datapoint = np.concatenate((x, [y]))
    with open(GOAL_DIR + str(i+1) + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(variables)
        writer.writerow(datapoint)