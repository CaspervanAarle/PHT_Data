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
dataset_name = "CASP"

### in
CSV_DIR = "C:\\Users\\Casper\\Projects\\MasterScriptie\\custom_projects\\model_training\\PHT_data_generator2\\external\\{}.csv".format(dataset_name)
### out
GOAL_DIR_CENTRAL = os.getcwd() + "\\{}\\".format(dataset_name + "_central")
GOAL_DIR_FEDERATED = os.getcwd() + "\\{}\\".format(dataset_name + "_federated")


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


### oud:
#shutil.copyfile(CSV_DIR , target)
        

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
try:
    os.mkdir(GOAL_DIR_CENTRAL)
except OSError:
    print ("Creation of the directory failed or already exists")   
    
total_df = ds.loc[r_list]
total_df.to_csv(target,  index=False)

### write central (old)
"""
shutil.copyfile(CSV_DIR , target)
"""

### write federated old:
"""
try:
    os.mkdir(GOAL_DIR_FEDERATED)
except OSError:
    print ("Creation of the directory failed or already exists")   
with open(CSV_DIR, 'r', newline='') as in_file:
    csv_reader = csv.reader(in_file, delimiter=',')
    header = []
    for i, row in enumerate(csv_reader):
        if i==0:
            header = row
        else:
            with open(GOAL_DIR_FEDERATED + "{}.csv".format(i), mode='w', newline='') as out_file:
                csv_writer = csv.writer(out_file, delimiter=',')
                csv_writer.writerow(header)
                csv_writer.writerow(row)
            out_file.close()
"""