#!/usr/bin/python3

import math
import sys
import numpy as np

def answer(n):
    # your code here
    if n>100000: # keep things reasonable
        return '-----'

    # first find what the limit needs to be
    # generate the list
    # jump the string by n

    target=n
    initalloc=int(math.log(target+5)/2+2)*(target+5)
    if n==0:
        initalloc += 4
    if n==1:
        initalloc += 6
    if n==2:
        initalloc += 8

    # OK, the string length grows linearly with the target length, 
    # until the primes cross the decades, then the increse linearly, 
    # but with a faster rate. 
    # This helps us decide what the initiallen should be based 
    # on the target len

    v=np.arange(initalloc)
    #i=1
    #done=False
    #while not done:
    for i in range(2,len(v)):
        #i+=1
        #while v[i]==0:
        if v[i]==0:
            continue
        for j in range(i*i,len(v),i): ## for loops are painful
            v[j] = 0

    ## getting ready to print out to ascii for plotting ##
    dim = int(math.sqrt(len(v))+1)
    vout = np.zeros(np.power(dim,int(2)),dtype=int)
    vout[:len(v)] = v 
    vout.shape=(dim,dim)
    outname = 'primes.%i.%ix%i.dat' % (n,dim,dim)
    np.savetxt(outname,vout,fmt='%i')
    y=v[np.where(v>0)]
    for k in range(10,100,10):
        dimx = y[k]
        dimh = len(v)//dimx+1
        vout = np.zeros(dimx*dimh,dtype=int)
        vout[:len(v)] = v
        vout.shape=(dimx,dimh)
        outname = 'primes.%i.%ix%i.dat' % (n,dimx,dimh)
        np.savetxt(outname,vout,fmt='%i')
    return

def main():
    if len(sys.argv)<2:
        print('no individuals requested')
        return '-----'
    nlist = sys.argv[1:]
    for n in nlist: 
        answer(int(n))
    return

if __name__=='__main__':
    main()
