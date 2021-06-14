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

# name your custom dataset:
dataset_name = "synthetic"


GOAL_DIR_CENTRAL = os.getcwd() + "\\out\\{}\\".format(dataset_name + "_central")
GOAL_DIR_FEDERATED = os.getcwd() + "\\out\\{}\\".format(dataset_name + "_federated")
N_FEATURES = 1
N_TARGETS = 1


def make_dir():
    """generate out directory"""
    OUT_DIR = os.getcwd() + "\\out\\"
    try:
        os.mkdir(OUT_DIR)
    except OSError:
        print ("Creation of the directory failed or already exists")  
    return





def make_reg():
    """generate dataset for regression task"""
    return sklearn.datasets.make_regression(n_samples=100, 
                                     n_features=N_FEATURES, 
                                     n_informative=N_FEATURES, 
                                     n_targets=N_TARGETS, 
                                     bias=2, 
                                     effective_rank=None, 
                                     tail_strength=-1, 
                                     noise=1, 
                                     shuffle=True, 
                                     coef=False, 
                                     random_state=9)



def make_classif():
    """generate dataset for classification task"""
    return sklearn.datasets.make_classification(n_samples=50, 
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

def create_header():
    """creates header for csv file"""
    variables = []
    for x in range(N_FEATURES + N_TARGETS):
        variables.append("var_" + str(x+1))
    return variables


def visualize(x_all, y_all):
    """visualize generated datapoints when n_features=1"""
    if np.array(x_all).shape[1] == 1:
        plt.scatter(x_all, y_all)
        plt.show()
    else:
        print("Unable to visualize input variables containing more than 1 feature")
    
        
def write_central(x_all, y_all, header):
    """save to single csv file:"""
    try:
        os.mkdir(GOAL_DIR_CENTRAL)
    except OSError:
        print ("Creation of the directory failed or already exists")    
    y_all_s = np.expand_dims(y_all, axis=1)
    all_data = np.concatenate((x_all,y_all_s), axis=1)
    with open(GOAL_DIR_CENTRAL + 'data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for d in all_data:
            writer.writerow(d)
        
def write_federated(x_all, y_all, header):
    """save to separate csv files"""
    try:
        os.mkdir(GOAL_DIR_FEDERATED)
    except OSError:
        print ("Creation of the directory failed or already exists")
    for i, (x, y) in enumerate(zip(x_all, y_all)):
        datapoint = np.concatenate((x, [y]))
        with open(GOAL_DIR_FEDERATED + str(i+1) + '.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerow(datapoint)
            
if __name__ == "__main__" :
    make_dir()
    # x_all, y_all = make_reg()
    x, y = make_classif()
    visualize(x, y)
    header = create_header()
    write_central(x, y, header)
    write_federated(x, y, header)
    
    