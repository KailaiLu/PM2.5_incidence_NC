# -*- coding: utf-8 -*-
import os
import pandas as pd

def jisuan(jb,sxx):
    if jb == "CHD":
        death = 126.82
        if sxx == "af":
            af = 0.00823
        elif sxx == "afg":
            af = 0.01254
        elif sxx == "afd":
            af = 0.00388
    elif jb == "STR":
        death = 375.83
        if sxx == "af":
            af = 0.00725
        elif sxx == "afg":
            af = 0.01293
        elif sxx == "afd":
            af = 0.0015
    for i in range(1,4):
        df_pop = pd.read_csv("E:/airpollution/pop/re_2025-2060_S" + str(i) + ".csv", low_memory=False)
        path = r"E:/airpollution/C-15"
        # path = "F:/High group/task20_baoyu/Result/ozzx"
        path_list = os.listdir(path)
        path_list.sort(key=lambda x: str(x[:-3]))
        for filename in path_list:
            file = path + "/" + filename
            year = int(filename[-8:-4])
            qj = str(filename[:6])
            df0 = pd.read_csv(file, low_memory=False,usecols= [0])
            df1 = pd.read_csv(file, low_memory=False)
            path2 = "E:/airpollution/future_county/"+str(qj)+"/"+str(year)
            path2_list = os.listdir(path2)
            path2_list.sort(key=lambda x: str(x[:-3]))
            for filename2 in path2_list:
                date = str(filename2[:-4])
                df0[str(date)]=df1[str(date)]*df_pop[str(year)]*af*death/365000000
            df0.to_csv(r"E:/airpollution/风险计算c-15/"+str(qj)+"_S"+str(i)+"_"+str(year)+"_"+str(jb)+"_"+str(sxx)+".csv", encoding="utf_8_sig", index=False, mode='w+')
jisuan("CHD","af")
jisuan("CHD","afg")
jisuan("CHD","afd")
jisuan("STR","af")
jisuan("STR","afg")
jisuan("STR","afd")