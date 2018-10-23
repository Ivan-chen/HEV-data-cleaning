# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:10:17 2018
把每辆车的数据都结合到一个csv文件内
@author: Administrator
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
#import time
from data_cleaning import data_cleaning
from mpl_toolkits.mplot3d import Axes3D


#file='SHEVDC_ST1_ET1_64067.txt'
#data_cleaning(file)
carpath='清洗后'
carfiles = os.listdir(carpath) 
for car in carfiles:
    path=carpath+'/'+car+'/'
    files=os.listdir(path)
#    fig=plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
    df=pd.DataFrame()
    max_date=0
    min_date=sys.maxsize
    df_all=pd.DataFrame([])
    for file in files:
        with open(path+file) as f: 
            df_temp=pd.read_csv(f)
            df_all=df_all.append(df_temp)
#        ax.scatter(df_temp['time stamp'][1:],df_temp['current'][:-1], df_temp['max temperature'][1:],c='b',s=0.5,label='temperature1')
#        ax.scatter(df_temp['time stamp'][1:],df_temp['current'][:-1], df_temp['min temperature'][1:],c='r',s=0.5,label='temperature2')
#    plt.savefig(path.rstrip('/')+'_1.jpg',dpi=1000)    
#    plt.show()
    df_all.to_csv('cleaned/'+car+'.csv')
    print(car+'saved')
print('finished')