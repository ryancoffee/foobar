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

    target=n+5
    initalloc=int(math.log(target)/2+2)*target
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
    i=1
    done=False
    while not done:
        i+=1
        while v[i]==0:
        #if v[i] is 0:
            i+=1
        #print('i = ', i,'v[i] = ', v[i])
        for j in range(i*i,len(v),i): ## for loops are painful
            v[j] = 0
        #print('v = ',v)
        s=''.join(str(val) for val in v[:i] if val > 1 ) 
        #print('s = ',s)
        done = bool(len(s)>target)

    ## getting ready to print out to ascii for plotting ##
    dim = int(math.sqrt(len(v))+1)
    vout = np.zeros(np.power(dim,int(2)),dtype=int)
    vout[:len(v)] = v #int(1) for val in v if val>1
    vout.shape=(dim,dim)
    outname = 'blockprimes.%i.dat' % n
    np.savetxt(outname,vout,fmt='%i')
    return s[n:n+5]

def main():
    if len(sys.argv)<2:
        print('no individuals requested')
        return '-----'
    ids = sys.argv[1:]
    answers = []
    for n in ids:
        id_str = answer(int(n))
        print('re_id(%i) = %s'%(int(n),id_str))
    return

if __name__=='__main__':
    main()
