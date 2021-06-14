# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:31:11 2021

@author: Casper
"""

import os
import random
import pandas as pd


### dataset name
# name of the csv file in the external folder
# must include header as first row
dataset_name = "placeholder"

### in dir:
CSV_DIR = os.getcwd() + "\\in\\{}.csv".format(dataset_name)
### out dir:
GOAL_DIR_CENTRAL = os.getcwd() + "\\out\\{}\\".format(dataset_name + "_central")
GOAL_DIR_FEDERATED = os.getcwd() + "\\out\\{}\\".format(dataset_name + "_federated")

### random seed for consistent shuffling
RANDOM_SEED = 4

def write_federated(ds):
    """make directory for federated data and write data"""
    try:
        os.mkdir(GOAL_DIR_FEDERATED)
    except OSError:
        print ("Creation of the directory failed or already exists")   
        
    ### write federated:
    r_list = list(range(len(ds.index)))
    random.Random(RANDOM_SEED).shuffle(r_list)
    for i in range(min(len(r_list),1000)):
        locker_df = ds.loc[[r_list[i]]]
        locker_df.to_csv(GOAL_DIR_FEDERATED + "{}.csv".format(i+1),  index=False)

def write_central(ds):
    """make directory for central data and write data"""
    ### make central directory:
    try:
        os.mkdir(GOAL_DIR_CENTRAL)
    except OSError:
        print ("Creation of the directory failed or already exists")   
    target = GOAL_DIR_CENTRAL + "data.csv"
    
    ### write central:
    r_list = list(range(len(ds.index)))
    random.Random(RANDOM_SEED).shuffle(r_list)
    total_df = ds.loc[r_list]
    total_df.to_csv(target,  index=False)
    
    
if __name__ == "__main__" :
    ### read 
    df = pd.read_csv(CSV_DIR, header=0)
    
    ### shuffle
    ds = df.sample(frac=1)
    print(ds)
    
    ### make out directory:
    try:
        OUT_DIR = os.getcwd() + "\\out\\"
        os.mkdir(OUT_DIR)
    except OSError:
        print ("Creation of the directory failed or already exists")   
        
    ### fill with data:
    write_central(ds)
    write_federated(ds)
    
    