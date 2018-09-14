#!/usr/bin/python

import numpy as np

def get5(n,s):
    return s[n:n+5]

def checklen(v,targetlen):
    s=''.join(str(i) for i in v[np.where(v>1)])
    return(len(s)>targetlen,s)

def fillstring(initiallen,targetlen):
    v=np.arange(initiallen)
    i=1
    done=False
    #y[np.where(y%i==0)]=0
    #better to instead vectorize with list and stepsize
    #use stride not mod to sub-array v
    #y=v[i*i::i]
    #use the shallow copy in python
    #y[np.where(y>0)]=0

    #done,s = checklen(v[:i+1],targetlen)
    #print(done,s)
    while not done:
#    while i<initiallen:
        i+=1
        while v[i]==0:
            i+=1
        y=v[i*i::i]
        y[np.where(y>0)]=0
        done,s = checklen(v[:i],targetlen)
        #print(done,s)
    return s


#def answer(n):

# OK, the string length grows linearly with the target length, until the primes cross the decades, then the increse linearly, but with a faster rate. 
# This helps us decide what the initiallen should be based on the target len
n=10000
target=n+5
initalloc=int(np.log10(target)+2)*target
s=fillstring(initalloc,target)
print('finished with string = ',s)
print('re_id = ',get5(n,s))

    
