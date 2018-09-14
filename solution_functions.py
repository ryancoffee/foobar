#import numpy as np
import math
import sys



def get5(n,s):

    return s[n:n+5]

    

def checklen(v,targetlen):

    #s=''.join(str(i) for i in v[np.where(v>1)])
    s=''.join(str(i) for i in v if i > 1 ) #[np.where(v>1)])

    return(len(s)>targetlen,s)



def fillstring(initiallen,targetlen):

    #Will need likely less than 10k elements

    # each prime will quickly grow to many digits each

    # primes will climb somehow like linear



    v=range(initiallen)

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



    #eliminating non-primes, stride, don't roll subvectors

    # Eratosthenes method for elimination

    # dont roll, set to 0 and then select >1 at the end

    while not done:

#    while i<initiallen:

        i+=1

        while v[i]==0:

            i+=1

        #y=v[i*i::i] ### 
        #y[np.where(y>0)]=0
        for j in range(i*i,len(v),i): ## for loops are painful
            v[j] = 0

        done,s = checklen(v[:i],targetlen)

        #print(done,s)

    return s



    

def answer(n):

    # your code here

    

    # first find what the limit needs to be

    # generate the list

    # jump the string by n

    

    # OK, the string length grows linearly with the target length, 

    # until the primes cross the decades, then the increse linearly, 

    # but with a faster rate. 

    # This helps us decide what the initiallen should be based 

    # on the target len



    if n>10000: # keep things reasonable

        return '-----'

    target=n+5

    initalloc=int(math.log10(target)+2)*target

    s=fillstring(initalloc,target)

    #print('finished with string = ',s)

    id_str = get5(n,s)


    return id_str

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
