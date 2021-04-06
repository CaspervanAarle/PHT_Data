# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:39:31 2021

@author: Casper
"""

import sklearn
from sklearn import datasets
import numpy as np
import csv
import os


#GOAL_DIR = "C:\\Users\\Casper\\Projects\\MasterScriptie\\custom_projects\\data\\generated_dataset\\"
MAP_NAME = "dataset"
GOAL_DIR2 = os.getcwd() + "\\{}\\".format(MAP_NAME)
N_FEATURES = 9
N_TARGETS = 1

# create variable values
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


# create variable names
variables = []
for x in range(N_FEATURES + N_TARGETS):
    variables.append("var_" + str(x+1))
    

# save to separate csv files:
try:
    os.mkdir(GOAL_DIR2)
except OSError:
    print ("Creation of the directory failed")
for i, (x, y) in enumerate(zip(x_all, y_all)):
    datapoint = np.concatenate((x, [y]))
    with open(GOAL_DIR2 + str(i+1) + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(variables)
        writer.writerow(datapoint)