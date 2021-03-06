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
import random

from sklearn.preprocessing import KBinsDiscretizer

# name your custom dataset:
dataset_name = "synthetic_class3"


GOAL_DIR_CENTRAL = os.getcwd() + "\\out\\{}\\".format(dataset_name + "_central")
GOAL_DIR_FEDERATED = os.getcwd() + "\\out\\{}\\".format(dataset_name + "_federated")
N_FEATURES = 1
N_TARGETS = 1

SCALE = [random.Random().randint(1,1000) for _ in range(N_FEATURES)]


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
                                     noise=4, 
                                     shuffle=True, 
                                     coef=False, 
                                     random_state=10)



def make_classif():
    """generate dataset for classification task"""
    return sklearn.datasets.make_classification(n_samples=100, 
                                         n_features=N_FEATURES, 
                                         n_informative=N_FEATURES, 
                                         n_redundant=0, 
                                         n_repeated=0, 
                                         n_classes=2, 
                                         n_clusters_per_class=1, 
                                         weights=None, 
                                         flip_y=0.01, 
                                         class_sep=0.5, 
                                         hypercube=True, 
                                         shift=None, 
                                         scale=SCALE, 
                                         shuffle=True, 
                                         random_state=800)

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
            
def scale(x, scale_vec):
    return x*scale_vec
            
if __name__ == "__main__" :
    make_dir()
    #x, y = make_reg()
    x, y = make_classif()
    
    scale_vec = [pow(10, random.randint(-2, 2)) for i in range(N_FEATURES)]
    
    x = scale(x, scale_vec)
    print(x)
    visualize(x, y)
    header = create_header()
    
    binner = KBinsDiscretizer(n_bins=5, encode='ordinal')
    x = binner.fit_transform(x)
    print(x)
    
    visualize(x, y)
    write_central(x, y, header)
    write_federated(x, y, header)
    
    