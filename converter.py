# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:31:11 2021

@author: Casper
"""

import os
import csv
import shutil
from random import shuffle
import random
import numpy as np
import pandas as pd


### dataset name
# name of the csv file in the external folder
# must include header as first row
dataset_name = "placeholder"

### in
CSV_DIR = os.getcwd() + "\\in\\{}.csv".format(dataset_name)
### out
GOAL_DIR_CENTRAL = os.getcwd() + "\\out\\{}\\".format(dataset_name + "_central")
GOAL_DIR_FEDERATED = os.getcwd() + "\\out\\{}\\".format(dataset_name + "_federated")

try:
    OUT_DIR = os.getcwd() + "\\out\\"
    os.mkdir(OUT_DIR)
except OSError:
    print ("Creation of the directory failed or already exists")   


### write central
try:
    os.mkdir(GOAL_DIR_CENTRAL)
except OSError:
    print ("Creation of the directory failed or already exists")   
target = GOAL_DIR_CENTRAL + "data.csv"

df = pd.read_csv(CSV_DIR, header=0)

### shuffle
ds = df.sample(frac=1)
print(ds)


### write federated
try:
    os.mkdir(GOAL_DIR_FEDERATED)
except OSError:
    print ("Creation of the directory failed or already exists")   
    
r_list = list(range(len(ds.index)))
random.Random(4).shuffle(r_list)
#print(r_list)
for i in range(min(len(r_list),1000)):
    locker_df = ds.loc[[r_list[i]]]
    #print(locker_df)
    locker_df.to_csv(GOAL_DIR_FEDERATED + "{}.csv".format(i+1),  index=False)


### write central    
total_df = ds.loc[r_list]
total_df.to_csv(target,  index=False)
