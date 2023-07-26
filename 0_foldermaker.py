# this scripts makes the folders named (project id) in designated directory
import os
import csv

root = "/image/image_project"
src = "/X/idlist.csv"
local_dir = os.getcwd()

# read csv
with open(src.removeprefix('/'),'r',encoding='UTF-8') as file:
    csvr = csv.reader(file)
    csvr = list(csvr)

# make root
os.makedirs(local_dir + root, exist_ok=True)

# make each folder
for i in range(5,len(csvr)):
    os.makedirs(local_dir + root + '/' + csvr[i][1], exist_ok=True)