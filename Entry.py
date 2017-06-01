#! /bin/python3
#CLASS Entry
#Cullen Humphries
#wednesday, may 17, 2017
#Entry class sotres data on bmc entrys extracted from a csv
#===========================================================#

class EntryData:

    def __init__(self,_in): #send an array of inputs _in[] 19 in length
        self._all = _in
        self._region = _in[0]
        self._company = _in[1]
        self._site = _in[2]
        self._t1 = _in[3]
        self._t2 = _in[4]
        self._t3 = _in[5]
        self._model = _in[6]
        self._version = _in[7]
        self._manufacturer = _in[8]
        self._name = _in[9]
        self._serialNumber = _in[10]
        self._status = _in[11]
        self._urgency = _in[12]
        self._supportedBy = _in[13]
        self._managedBy = _in[14]
        self._primaryIP = _in[15]
        self._supported = _in[16]
        self._managedCI = _in[17]
        self._contract =  _in[18]
        self._reachable = False # _in[19]
        self._all.append(self._reachable)
        
        

    def getAll(self):
        return self._all

    def setReachable(self,boo):
        self._reachable = boo
    
    
