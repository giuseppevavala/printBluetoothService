# file: l2capclient.py
# desc: Demo L2CAP server for pybluez.
# $Id: l2capserver.py 524 2007-08-15 04:04:52Z albert $

import bluetooth
import uuid
import traceback




def getDictFromString (strInput):
    myList = strInput.split(";")
    myDict = {}
    for el in myList:
        if ('=' in el):
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
        text = text.replace("$" + key, myDict[key])
        
    # Scrive un file.
    out_file = open(fileout,"w")
    out_file.write(text)
    out_file.close()



server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 3

server_sock.bind(("",port))
server_sock.listen(1)

myUuid = "94f39d29-7d6d-437d-973b-fba39e49d4ef"
bluetooth.advertise_service( server_sock, "SampleServerL2CAP",
                   service_id = myUuid,
                   service_classes = [ myUuid ]
                    )

while True:                  
    try:
        client_sock,address = server_sock.accept()
        print("Accepted connection from ",address)
        
        strInput = ''
        data = ''
        try:
            data = client_sock.recv(1)
            strInput = data
            while (data != '&'):
                data = client_sock.recv(1)
                if (data != '&'):
                    strInput = strInput + data
            client_sock.send("Ok chiudi")
            client_sock.recv(10)
        except Exception,e:
            print str(e)
            print 'Connessione interrotta'    
        finally:
            client_sock.close()
            
        ris = getDictFromString (strInput)
        writeToFile (ris, "temp", str(uuid.uuid1()) + ".txt")
    except Exception,e:
        traceback.print_exc()
        print str(e)
        print 'Errore inaspettato'
    
    print 'Stampo'
    print strInput
server_sock.close()