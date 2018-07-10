# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:18:56 2018
@author: proj1_wsn
"""

import csv
import json
ffile= "H:\\Documents\\initialtextfile.json"
with open(ffile, "r") as json_data:
    d=json.load(json_data)
    mycsv = csv.writer(open('OutPut.csv', 'wb'))
    #mycsv.writerow(['Hops', 'Sensors', 'Time', 'Prr'])
    for line in d:
        strr=json.dumps(line)
        hops=strr[0]
        #hops=line["Number of Hops"]
        #sensors=line["Number of Sensors"]
        #time=line["Time inn milli-seconds"]
        #prr=line["Packet Reception Ratio"]
        mycsv.writerow([hops])
