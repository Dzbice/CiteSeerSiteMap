import hashlib
import os
import string
import random
import time

start = time.perf_counter()
while True:
    print("Slelect root path for data")
    x = input()
    if not os.path.exists(x):
        print("Invalid path")
        continue
    else: 
        print("Root selected")
        break
for i in range(250000):
    toBeHased=''.join(random.choice(string.ascii_letters+string.digits) for _ in range(20)) 
    hashed = hashlib.sha1(toBeHased.encode('utf-8')) #string needs to be encoded before being hashed with sha1
    stringedhash = hashed.hexdigest() #get the hex value for it
    
    path = os.path.join(x,"/".join(stringedhash[i:i+2] for i in range(0,14,2)),stringedhash,(stringedhash+".pdf")) #create path, the join is for getting 2 digit for the 
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fp = open(path,"w")
    fp.close()
end = time.perf_counter()
print(f"Full time: {end-start:.4f}")
   

