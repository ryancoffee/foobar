import math
import sys

def answer(n):
    # your code here
    if n>10000: # keep things reasonable
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
    #print('initalloc = ',initalloc)

    # OK, the string length grows linearly with the target length, 
    # until the primes cross the decades, then the increse linearly, 
    # but with a faster rate. 
    # This helps us decide what the initiallen should be based 
    # on the target len

    v=range(initalloc)
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
