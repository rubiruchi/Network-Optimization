# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:48:59 2018

@author: proj1_wsn
"""

import numpy as np
import time
import json

ffile="H:\\Documents\\datfinal1.json"
with open(ffile, "r") as json_data:
    file_output = open("output17.json", "w")
    d=json.load(json_data)
    """for line in d:
        print(line)
        break"""
    index=0
    list1=[]
    list2=[]
    #print("[",file=file_output)
    """for line in d:
        strr= json.dumps(line)
        #print("HI")
        if(strr.find("Source")!=-1):
        
            list1.append(line["Source"])
            list2.append(line["Destination"])
    listset1=set(list1)
    listset2=set(list2)
    ulistt1=list(listset1)
    ulistt2=list(listset2)
    ulist1=[]
    ulist2=[]
    for x in ulistt1:
        cnt=0
        for line in d:
            strr= json.dumps(line)
            if(strr.find("Source")!=-1):
                if(line["Source"]==x):
                    cnt=cnt+1
        #print(x,"        ",cnt)
        if(cnt>10):
            ulist1.append(x)
    for y in ulistt2:
        cnt=0
        for line in d:
            strr= json.dumps(line)
            if(strr.find("Source")!=-1):
                if(line["Destination"]==y):
                    cnt=cnt+1
        if(cnt>10):
            ulist2.append(y)
    """
    ulist1=[' 0x00003c38', ' 0x0000c69f', ' 0x0000ffff', ' 0x00008628', ' 0x00000000', ' 0x00006b19', ' 0x00006a42', ' 0x00006b54', ' 0x0000f950', ' 0x00006193']
    ulist2=[' 0x00003c38', ' 0x0000c69f', ' 0x0000ffff', ' 0x00008628', ' 0x00000000', ' 0x00006b19', ' 0x00006a42', ' 0x00006b54', ' 0x0000f950', ' 0x00006193']
    a=len(ulist1)
    b=len(ulist2)
    print(a)
    print(b)
    
    
    for i in range(0,len(ulist1)):
        for j in range(0,len(ulist2)):
            
            packet = np.zeros(7)
            retry = np.zeros(7)
            ack = np.zeros(7)
            z=""
            y=""
            lsi=np.zeros(7)
            ci=np.zeros(7)
            co=np.zeros(7)
            lso=np.zeros(7)
            avgi=np.zeros(7)
            avgo=np.zeros(7)
            listt=[[None]for _ in range(7)]
            minn=[""]*7
            maxx=[""]*7
            f=0
            lo=0
            time1=0.0
            for line in d:
                
                strr= json.dumps(line)
                if(strr.find("Source")!=-1):
                    if(line["Source"]==ulist1[i] and line["Destination"]==ulist2[j]):
                        if(strr.find('"Data"')!=-1):
                            index=strr.find('"Data"')
                            str1=strr[index+10]+strr[index+11]
                            k=-1
                            if(str1=='01' or str1=='02'):
                                k=0  
                            if(str1=='05' or str1=='06'):
                                k=1
                            if(str1=='09' or str1=='0a'):
                                k=2
                            if(str1=='0d' or str1=='0e'):
                                k=3
                            if(str1=='13' or str1=='14'):
                                k=4
                            if(str1=='15' or str1=='16'):
                                k=5
                            if(str1=='19' or str1=='1a'):
                                k=6
                            if(k!=-1):
                                listt[k].append(line["Date"])  
            for l in range(0,7):
                if(len(listt[l])>1):
                    del listt[l][0]
                    listt[l].sort()
                    minn[l]=(listt[l][0])
                    maxx[l]=(listt[l][len(listt[l])-1])
                    #print(ulist1[i],"  ",ulist2[j],"  ",l,"  ",minn[l],"  ",maxx[l])
            
                    for line in d:
                        strr= json.dumps(line)
                        if(strr.find("Link")!=-1):
                            cnt1=0
                            index=0
                            index=strr.find("Address",index)
                            while(index!=-1):
                                cnt1=cnt1+1
                                str8=' Link '+ str(cnt1)+' Address'
                                str9=' Link '+ str(cnt1)+' incoming cost'
                                str10=' Link '+ str(cnt1)+' outgoing cost'    
                                if(line["Source"]==ulist1[i] and line[str8]==ulist2[j]):
                                    if(line["Date"]>=minn[l] and line["Date"]<=maxx[l]):
                                        lsi[l]=lsi[l]+int(line[str9])
                                        lso[l]=lso[l]+int(line[str10])
                                        #print(int(line[str10]))
                                        if(lsi[l]!=0):
                                            ci[l]=ci[l]+1
                                        if(lso[l]!=0):
                                            co[l]=co[l]+1
                                index=index+1
                                index=strr.find("Address",index)
                    if(ci[l]!=0):
                        avgi[l]=lsi[l]/ci[l]
                        avgo[l]=lso[l]/co[l]
                        print(ulist1[i],"  ",ulist2[j],"  ",l,"  ",avgi[l],"    ",avgo[l])
                    