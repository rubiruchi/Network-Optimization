# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:28:50 2018

@author: Suyash
"""
import numpy as np
import time
import json

ffile="H:\\Documents\\datfinal1.json"
with open(ffile, "r") as json_data:
    file_output = open("fout1.csv", "w")
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
            ulist2.append(y)"""
    
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
            listt=[[None]for _ in range(7)]
            minn=[""]*7
            maxx=[""]*7
            f=0
            lo=0
            time1=0.0
            for line in d:
                if(line["Time"]!=time1):
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
                                    packet[k] = packet[k]+1
                                    if(z==line["Sequence number"]):
                                        retry[k] = retry[k] + 1
                                        f=1
                                    y=z
                                    z = line["Sequence number"]
                    #print(y==z)
                    elif(strr.find("Sequence number")!=-1):
                        
                        if(strr.find("Data Acknowledged")!=-1 and y==line["Sequence number"] ):
                            if(k!=-1):
                                #print("HI")
                                ack[k] = ack[k] + 1
                time1=line["Time"]
            for l in range(0,7):
                if(len(listt[l])>1):
                    minn[l]=(listt[l][1])
                    maxx[l]=(listt[l][len(listt[l])-1])
                    #print(i,"  ",j,"  ",minn[l],"  ",maxx[l])
            eee=[50,75,100,250,500,1000,2000]
            for r in range (0,7):
                if(packet[r]>0):
                    print(ulist1[i][7:11],end=",",file=file_output)
                    print(ulist2[j][7:11],end=",",file=file_output)
                    print(eee[r],end=",",file=file_output)
                    print(packet[r],end=",",file=file_output)
                    #print(ack[r],end=",",file=file_output)
                    print(retry[r],file=file_output)
                    lo=lo+ack[r]
            
            