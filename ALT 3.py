import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv ('drivingtest.csv')
print ("info", df.info())
print ("shape", df.shape)
print (df.describe())

MyPass = 0
MyFail = 0
GenderF = 0
GenderM = 0

with open ('drivingtest.csv' , 'r') as file:
    csv_reader = csv.reader (file)
    print ("Printing rows")
   
    for row in csv_reader:
        if row [6] == "Pass" and int (row [2]) < 18:
            MyPass += 1
            print (row [2], "MyPass")
           
        if row [4] == "none" and row [5] == 0 and int(row[2]) < 18:
            MyFail += 1
            print(row[2], "MyFail")

           
       
    
