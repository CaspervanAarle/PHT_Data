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
import matplotlib.pyplot as plt
import numpy as np


#GOAL_DIR = "C:\\Users\\Casper\\Projects\\MasterScriptie\\custom_projects\\data\\generated_dataset\\"
MAP_NAME = "linreg"
GOAL_DIR_CENTRAL = os.getcwd() + "\\{}\\".format(MAP_NAME + "_central")
GOAL_DIR_FEDERATED = os.getcwd() + "\\{}\\".format(MAP_NAME + "_federated")
N_FEATURES = 1
N_TARGETS = 1

# create variable values



x_all, y_all, coef = sklearn.datasets.make_regression(n_samples=100, 
                                 n_features=N_FEATURES, 
                                 n_informative=N_FEATURES, 
                                 n_targets=N_TARGETS, 
                                 bias=2, 
                                 effective_rank=None, 
                                 tail_strength=-1, 
                                 noise=1, 
                                 shuffle=True, 
                                 coef=True, 
                                 random_state=9)



"""
x_all, y_all = sklearn.datasets.make_classification(n_samples=50, 
                                     n_features=N_FEATURES, 
                                     n_informative=1, 
                                     n_redundant=0, 
                                     n_repeated=0, 
                                     n_classes=2, 
                                     n_clusters_per_class=1, 
                                     weights=None, 
                                     flip_y=0.01, 
                                     class_sep=0.5, 
                                     hypercube=True, 
                                     shift=1.0, 
                                     scale=4.0, 
                                     shuffle=True, 
                                     random_state=5)

"""
plt.scatter(x_all, y_all)
plt.show()
#print(coef)
# create variable names
variables = []
for x in range(N_FEATURES + N_TARGETS):
    variables.append("var_" + str(x+1))
    
#  save to single csv file:
try:
    os.mkdir(GOAL_DIR_CENTRAL)
except OSError:
    print ("Creation of the directory failed or already exists")    
y_all_s = np.expand_dims(y_all, axis=1)
all_data = np.concatenate((x_all,y_all_s), axis=1)
with open(GOAL_DIR_CENTRAL + 'data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(variables)
    for d in all_data:
        writer.writerow(d)

# save to separate csv files:
try:
    os.mkdir(GOAL_DIR_FEDERATED)
except OSError:
    print ("Creation of the directory failed or already exists")
for i, (x, y) in enumerate(zip(x_all, y_all)):
    datapoint = np.concatenate((x, [y]))
    with open(GOAL_DIR_FEDERATED + str(i+1) + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(variables)
        writer.writerow(datapoint)