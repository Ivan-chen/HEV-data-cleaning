#数据清洗，目前的设定为100辆电动车，最少运行时间为10min，中间允许有两个断点（没有检测到数据）


#import numpy as np
#import os
#import matplotlib.pyplot as plt
import time
import pandas as pd
import os
#plt.figure()

#files = os.listdir(path) 
#file='SHEVDC_ST1_ET1_65045.txt'

def data_cleaning(file):
    path='乘用车_BEV/'
    with open(path+file) as f:
    #    with open('乘用车_BEV/SHEVDC_ST1_ET1_61474.txt') as f:
        
        
        local=file.rstrip(".txt")
        df=pd.read_table(f,sep=',')
    #    data = (f.read().splitlines())
    #    for i in range(len(data)):
    #        data[i]=data[i].split(",")
    #    data_in=np.array(data)
        run_time=(df['数据采集时间'])
        
        time_stamp=run_time.apply(lambda x:time.mktime(time.strptime(x,'%Y-%m-%d %H:%M:%S')) )
        time_stamp=time_stamp.astype('int64')
        tem_high=(df['单体最高温度'])
        tem_low=(df['单体最低温度'])
        SOC=(df['电池剩余电量(SOC)'])
        voltage_high=(df['单体最高电压'])
        voltage_low=(df['单体最低电压'])
        voltage_all=(df['电池总电压'])
        current=(df['高压电池电流'])
        data_usable=pd.concat([time_stamp,run_time,tem_high,tem_low,SOC,voltage_high,voltage_low,voltage_all,current],axis=1)
        data_usable=data_usable.drop(tem_high[tem_high==0].index,axis = 0)
    
        data_usable=data_usable.dropna(axis=0,how='any')
        
        data_usable.columns=['time stamp','date','max temperature','min temperature','SOC','max V','min V','overall V','current']
    #    data_usable.to_csv('乘用车_BEV/SHEVDC_ST1_ET1_61474'+'.csv')
#        data_usable.set_index(["time stamp"], inplace=True)
        
        count=0
        file_num=0
        min_series=30#20s*min_series 有效数据最少的连续观测点
        margin=62#允许两个观测数据之间相差margin 秒
        for i in range(len(data_usable)-1):
            count+=1
            if((data_usable['time stamp'].iloc[i+1]-data_usable['time stamp'].iloc[i])>margin):
                if(count>min_series):
                    if( not os.path.exists('清洗后/'+local)):
                        os.makedirs('清洗后/'+local)
                    data_usable.iloc[i-count+1:(i+1)].to_csv('清洗后/'+local+'/'+local+'__'+str(file_num)+'.csv')
                    print(local+'__'+str(file_num)+'.csv saved sum='+str(count))
                    file_num+=1
                count=0   
        
    
        
    
#    for t in range(len(timestamp)):
#        timestamp[t]=1
#    data_in[data_in=='']=0.0#填充元素
#    tem_high=(data_in[1:,14]).astype(np.float64)
#    for i in range(1,tem_high.shape[0]-1):
#        if(tem_high[i]==0):
#            tem_high[i]=(tem_high[i+1]+tem_high[i-1])/2
#            
#    x=tem_high.reshape(1,tem_high.shape[0])
    
#    x=np.array(tem_high)
#    plt.plot(tem_high[0:331]