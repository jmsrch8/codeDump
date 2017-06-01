#! /bin/python3
#MAIN BMC Managment App
#Cullen Humphries
#wednesday, may 17, 2017
#Manipulates data from CSVs
#===========================================================#

import csv
import Entry
import os
import time
from datetime import datetime
import subprocess

_sheet = []

def main():
    with open('bmc_05172017.csv') as csvfile:
        reader = csv.reader(csvfile, dialect='excel',quotechar='|')
        header = False
        for i in reader:
            if header == False:
                header = i
            else:
                line = i
                e = Entry.EntryData(line)
                _sheet.append(e)
    getlist()
    

#=============================================================#
    
def getlist():
    i=0
    print("Hostname\tSerialNumber\tIPAddress\tStatus")
    while(True):
        if i <= len(_sheet)-1:
            line = _sheet[i].getAll()
      #      print(line[0] + " " +line[1] + " " +line[2] + " " +line[3] + " " +line[4] + " " +line[5] + " " +
      #            line[6] + " " +line[7] + " " +line[8] + " " +line[9] + " " +line[10] + " " +
      #            line[11] + " " +line[12] + " " +line[13] + " " +line[14] + " " +line[15] + " " +
      #            line[16] + " " +line[17 + " " +line[18] + " " + line[19])
            if checkAlive(line[9], line[15]) == True:
                _sheet[i].setReachable(True)
            line = _sheet[i].getAll()
            print(line[9] + "\t" + line[10] + "\t" + line[15] + "\t" + line[11] + "\t" + str(line[19]))
            i = i + 1
        else:
            break
#=============================================================#

def checkAlive(hstName, ipAdd):
    state = False
    p = subprocess.Popen('ping -n 1' + hstName, stdout=subprocess.PIPE).communicate()[0]
    if ('TTL=' in p):
        state = True
        logging('ping ' + hstName + " is sucessful")
    else:
        logging('ping ' + hstName + " has failed")

    if ipAdd != None:
        p = subprocess.Popen('ping -n 1' + ipAdd, stdout=subprocess.PIPE).communicate()[0]
        if ('TTL=' in p):
            state = True
            logging('ping ' + ipAdd + " is sucessful")
        else:
            logging('ping ' + ipAdd + " has failed")
    else:
        logging(hstName + " has no IP address in BMC")
    p.wait()
    return state


def logging(message):
    with open('log.txt', 'a') as _file:
        t = time.time()
        _file.write(str(t) + '  \t:::\t  ' + message + '\n')
        _file.close()

    
    
main()
input("press \'enter\' to exit...")
