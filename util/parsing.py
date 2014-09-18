'''
Created on 18/set/2014

@author: giuseppe
'''

def getDictFromString (strInput):
    myList = strInput.split(";")
    myDict = {}
    for el in myList:
        key = el.split ("=")[0];
        value = el.split ("=")[1];
        myDict[key] = value
        
    return myDict


def writeToFile (myDict, filein, fileout):
    # Legge un file.
    in_file = open(filein,"r")
    text = in_file.read()
    in_file.close()
    
    for key in myDict.iterkeys():
        text = text.replace(key, myDict[key])
        
    # Scrive un file.
    out_file = open(fileout,"w")
    out_file.write(text)
    out_file.close()
    

import uuid

strInput = 'totale=1200.00;carta=4023-6004-3125-4876'
ris = getDictFromString (strInput)
writeToFile (ris, "temp", str(uuid.uuid1()) + ".txt")


