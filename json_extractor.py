# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:30:52 2018

@author: proj1_wsn
"""
import json
import time
def func(src_file,dest_file):
    ffile= src_file
    with open(ffile, "r") as json_data:
        if(src_file.find("1")!=-1):
            file_output = open(dest_file, "w")
        else:
            file_output = open(dest_file, "a")
        d=json.load(json_data)
        index=0
        flag=0
        if(src_file.find("1")!=-1):
            print("[",file=file_output)
        for line in d:
            strr= json.dumps(line)
            if (('"wpan.dst_pan": "0x00005ce5"' in strr or (strr.find('"wpan.ack_request": "0"')!=-1 and strr.find("wpan.dst_pan")==-1)) and "_ws.malformed" not in strr):
                if(strr.find('"data.len": "12"')!=-1 or (strr.find("Command Frame: Link Status")!=-1 and strr.find('"zbee_nwk.cmd.link.count": "0"')==-1) or (strr.find('"wpan.ack_request": "0"')!=-1 and strr.find("Command Frame: Link Status")==-1 and strr.find('"data.len": "12"')==-1)):
                    #print(flag)
                    if(flag!=0):
                        print(",",file=file_output)
                    flag=1
                    print("{",file=file_output)
                    ed=line["_source"]["layers"]["frame"]["frame.time"]
                    struct_time = time.strptime(line["_source"]["layers"]["frame"]["frame.time"][:21], "%b %d, %Y %H:%M:%S")
                    t = (struct_time[0],struct_time[1],struct_time[2],struct_time[3],struct_time[4],struct_time[5],struct_time[6],struct_time[7],struct_time[8])
                    t = time.mktime(t)
                    print('"Date" :',end='"',file=file_output)
                    print(time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.localtime(t)),end='",',file=file_output)
                    time1=float(ed[13:15])*3600+float(ed[16:18])*60-5*3600-30*60+24*60*60*(float(ed[5])-1.0)
                    time1=time1+float(ed[19:31])
                    level=1
                    if(src_file.find("5")!=-1 or src_file.find("6")!=-1 or src_file.find("7")!=-1):
                        time1=time1+160.6734
                        level=2
                    print('"Time":',time1 ,end=',', file=file_output)
                    print('"File":',level ,end=',', file=file_output)
                    if(strr.find('"wpan.seq_no"')!=-1):
                        print('"Sequence number": "',line["_source"]["layers"]["wpan"]["wpan.seq_no"] ,end='",', file=file_output)
                    if(((strr.find('"data.len": "12"')!=-1 or (strr.find("Command Frame: Link Status")!=-1 and strr.find('"zbee_nwk.cmd.link.count": "0"')==-1))) and (strr.find("wpan.dst_pan")!=-1 and strr.find("wpan.dst16")!=-1 and strr.find("wpan.src16")!=-1 )):
                        print('"Pan_id": "', line["_source"]["layers"]["wpan"]["wpan.dst_pan"] ,end='",', file=file_output)
                        print('"Source": "', line["_source"]["layers"]["wpan"]["wpan.src16"] ,end='",', file=file_output)    
                        print('"Destination": "', line["_source"]["layers"]["wpan"]["wpan.dst16"] ,end='",' , file=file_output)
                        if(strr.find("zbee_aps.counter")!=-1):
                            print('"Counter number": "',line["_source"]["layers"]["zbee_aps"]["zbee_aps.counter"] ,end='",', file=file_output)
                
                if strr.find('"wpan.ack_request": "0"')!=-1 and strr.find("Command Frame: Link Status")==-1 and strr.find('"data.len": "12"')==-1:
                    print('"Data Acknowledged": "',"1",end='"', file=file_output)
                    print("}",end="",file=file_output)
                elif strr.find('"data.len": "12"')!=-1 and strr.find("Command Frame: Link Status")==-1:
                    strx=line["_source"]["layers"]["data"]["data.data"]
                    print('"Data": "', strx[18:20],end='"', file=file_output )
                    print("}",end="",file=file_output)
                elif strr.find("Command Frame: Link Status")!=-1:
                    cnt=int (line["_source"]["layers"]["zbee_nwk"]["Command Frame: Link Status"]['zbee_nwk.cmd.link.count']) 
                    cnt1=cnt
                    while(cnt !=0 ):
                        str1='Link '+ str(cnt1-cnt+1)
                        #if(strr.find(str1)!=-1):
                        print('"',str1,'Address": "' , line["_source"]["layers"]["zbee_nwk"]["Command Frame: Link Status"][str1]["zbee_nwk.cmd.link.address"],end='",', file=file_output)
                        print('"',str1,'incoming cost": "' , line["_source"]["layers"]["zbee_nwk"]["Command Frame: Link Status"][str1]['zbee_nwk.cmd.link.incoming_cost'],end='",', file=file_output)
                        if(cnt==1):
                            print('"',str1,'outgoing cost": "' , line["_source"]["layers"]["zbee_nwk"]["Command Frame: Link Status"][str1]['zbee_nwk.cmd.link.outgoing_cost'], end='"',file=file_output)
                        else:
                            print('"',str1,'outgoing cost": "' , line["_source"]["layers"]["zbee_nwk"]["Command Frame: Link Status"][str1]['zbee_nwk.cmd.link.outgoing_cost'], end='",',file=file_output)    
                        cnt=cnt-1
                    if(cnt1!=0):
                        print("}",end="",file=file_output)
        if(src_file.find("7")==-1):               
            print(",",file=file_output)
        else:
            print("]",file=file_output)
    