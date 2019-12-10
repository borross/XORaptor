import os
from random import randrange, seed
from getpass import getuser

def  xor(inputDATA, key, outputFILE):
    keyLEN = len(key)
    return open(outputFILE, 'wb').write(bytearray(((inputDATA[i] ^ key[i % keyLEN]) for i in range(0, len(inputDATA)))))

def fastXor(inputDATA, key, outputFILE):
    from math import ceil
    DataLen = len(inputDATA)

    #key with same length as file
    kkey = (key*int(ceil(float(DataLen)/float(len(key)))))[:DataLen]
    return open(outputFILE, 'wb').write(bytearray(((inputDATA[i] ^ kkey[i]) for i in range(0, DataLen))))

def secure_delete_rand(file, passes=1):
	seed()
	with open(file, "wb") as delfile:
		length = delfile.tell()
		for pas in xrange(passes):
			delfile.seek(0)
			for byte in xrange(length):
				delfile.write(str(randrange(256)))
	os.remove(file)

key = list(bytearray('password'))
ENC = 0
ext = [".pdf", ".xlsx"]
PATH = "C:\\Users\\"+ getuser() +"\\Downloads\\XOR"

for root, subdirs, files in os.walk(PATH):
    new_strs = root.replace('\\','\\\\')
    #print new_strs
    os.chdir(new_strs)

    if ENC:
    	files = [f for f in os.listdir(new_strs) if os.path.isfile(f) and f.endswith(tuple(ext))]
    else:
    	files = [f for f in os.listdir(new_strs) if os.path.isfile(f) and f.endswith('.enc')]    	 	
    
    for item in files:    	
    	data = bytearray(open(item, 'rb').read())
    	if ENC:
    		output = item + ".enc"
    	else:
    		output = item[:-4]
    	print output
    	fastXor(data, key, output)
    	secure_delete_rand(item)
