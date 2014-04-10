import binascii  
import struct  
print(" -----encoder-----")  
frPath = raw_input("Enter source path: ")  
fwPath = raw_input("Enter target path: ")  
keys = [9,4,6,8]  
  
try:  
    fr = file(frPath,'rb')  
    fw = file(fwPath,'wb')  
    for i in range(4):  
        fr.seek(i)  
        s_16 = binascii.b2a_hex(fr.read(1))  
        s_10 = int(s_16,16)  
        s_10NO = s_10 ^ keys[i]  
        s_10NOvalue = struct.pack('B',s_10NO)  
          
        fw.write(s_10NOvalue)  
      
    fw.write(fr.read())  
except IOError:  
    print("----------------------------------------")  
    print("Progress error")  
finally:  
    print("----------------------------------------")  
    print("done successfully")  
    fr.close()  
    fw.close() 