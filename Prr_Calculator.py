# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:43:57 2018

@author: Suyash
"""

import numpy as np
def prr(src_file,dest_file):
    ffile= "H:\\Documents\\27-06-18.txt"
    x=7
    listt= []
    with open (ffile , "r") as in_file:
        file_output = open("fout3.csv", "w")
        content=""
        for line in in_file.readlines():
            content += line
        str=content
        strr=content
        def func(str1,str2,v):
            c1=[0]*9
            cnt1=np.array(c1)
            c2=[0]*9
            cnt2=np.array(c2)
            cnt=0
            substr1="7E0"
            substr2="7E ,"
            index=0
            a=0
            b=0
            c=0
            a = [[0]*10002]*8
            arr=np.array(a)
            b=[[0]*10002]*8
            brr=np.array(b)      
            eee=['6193','6B19','8628','3C38','6B54','6A42','F950']
            cs=[2,2,2,1,2,2,2]
            while(index<len(str)):
                index=str.find(substr1,index)
                if index==-1:
                    break
                while(cnt!=52):
                    if(str[index]==' '):
                        index=index+21
                    elif(str[index]=='\n'):
                        index=index+1
                    else:
                        listt.append(str[index])
                        index=index+1
                        cnt=cnt+1
                cnt=0
                str10=listt[24]+listt[25]+listt[26]+listt[27]
                for i in range(0,7):
                    if(eee[i]==str10):
                        xe=i
                        break
                if listt[42]==str1[0] and listt[43]==str1[1]:
                    s=""
                    a = listt[47]
                    b = listt[48]
                    c = listt[49]
                    s=a+b+c
                    num=int(s , 16)
                    arr[xe][num]=arr[xe][num]+1
                    if(listt[47]=='3' and listt[48]=='E' and listt[49]=='9'):
                        cnt=cnt
                    elif arr[xe][num]<=1:
                        cnt1[xe]=cnt1[xe]+1
                    
                elif listt[42]==str2[0] and listt[43]==str2[1]:
                    s=""
                    a = listt[47]
                    b = listt[48]
                    c = listt[49]
                    s=a+b+c
                    num=int(s , 16)
                    brr[xe][num]=brr[xe][num]+1
                    if(listt[47]=='3' and listt[48]=='E' and listt[49]=='9'):
                        cnt=cnt
                    elif brr[xe][num]<=1:
                        cnt2[xe]=cnt2[xe]+1
                    
                listt.clear()
            
            index1=0
            a=0
            b=0
            c=0
            cnt=0
           
                
            while(index1<len(strr)):
                index1=strr.find(substr2,index1)
                #print(flag)
                if index1==-1:
                    break
                elif str[index1+24]=='7':
                    index1=index1+22
                    continue
                while(cnt!=52):
                    if(strr[index1]==' '):
                        index1=index1+21
                    elif(strr[index1]=='\n'):
                        index1=index1+1
                    else:
                        listt.append(strr[index1])
                        index1=index1+1
                        cnt=cnt+1
                #print(listt[0:52])
                cnt=0
                str10=listt[24]+listt[25]+listt[26]+listt[27]
                for i in range(0,7):
                    if(eee[i]==str10):
                        xe=i
                        break
                if listt[42]==str1[0] and listt[43]==str1[1]:
                    s=""
                    a = listt[47]
                    b = listt[48]
                    c = listt[49]
                    s=a+b+c
                    num=int(s , 16)
                    arr[xe][num]=arr[xe][num]+1
                    if(listt[47]=='3' and listt[48]=='E' and listt[49]=='9'):
                        cnt=cnt
                    elif arr[xe][num]<=1:
                        cnt1[xe]=cnt1[xe]+1
                        
                elif listt[42]==str2[0] and listt[43]==str2[1]:
                    s=""
                    a = listt[47]
                    b = listt[48]
                    c = listt[49]
                    s=a+b+c
                    num=int(s , 16)
                    brr[xe][num]=brr[xe][num]+1
                    if(listt[47]=='3' and listt[48]=='E' and listt[49]=='9'):
                        cnt=cnt
                    elif brr[xe][num]<=1:
                        cnt2[xe] = cnt2[xe] + 1
                    
                listt.clear()
            for i in range(0,7):
                print(cs[i],end=",",file=file_output)
                print(x,end=",",file=file_output)
                print(v,end=",",file=file_output)
                print(eee[i],end=",",file=file_output)
                print((cnt1[i]+cnt2[i])/(2000),file=file_output)
        print("Number of Hops,",end="",file=file_output)
        print("Number of Sensors,",end="",file=file_output)
        print("Data Rate,",end="",file=file_output)
        print("Address,",end="",file=file_output)
        print("Packet Reception Ratio",file=file_output)
        func('01','02','50')
        func('05','06','75')
        func('09','0A','100')
        func('0D','0E','250')
        func('11','12','500')
        func('15','16','1000')
        #func('19','18','2000')