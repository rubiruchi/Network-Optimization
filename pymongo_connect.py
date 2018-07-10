# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:04:11 2018

@author: proj1_wsn
"""

import pymongo
import numpy as np
import datetime
import json
import pprint
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['fine']
collection = db['test']
posts = db.posts
ffile="H:\Documents\suyash ps work\dataset\mergef.json"

with open(ffile, 'r') as json_data:
    file_output = open("H:\Documents\suyash ps work\dataset\datfinal5.json", "w")
    d = json.load(json_data)
    for line in d:
        posts.insert_one(line)
        
    flag=0
    for post in posts.find().sort("Time"):
        if(flag==0):
            print("[",file=file_output)
            flag=flag+1
        else:
            print(",",end="",file=file_output)
        pprint.pprint(post,file_output)
    print("]",file=file_output)