import numpy as np
from collections import defaultdict
import pickle as pk
import time
#import psutil
import multiprocessing as mpr

def wf_pickle_n100(pid):
    gens = pop = 100
    anames = ['A', 'a']
    initprobs = np.arange(.1,1,.1)
    
    for p0 in initprobs:
        results = defaultdict(dict)

        pkl = open('./psims/n100' + 'p' + str(int(100*p0)) + '.pkl', 'ab')
        i=0
        p = p0
        while gens > i:
            p = round(np.random.binomial(2*pop, p)/float(2*pop),3)
            i += 1
            results[i] = p
        pk.dump({pid:results}, pkl)
        pkl.close()
    return

def wf_pickle_n1000(pid):
    gens = pop = 1000
    anames = ['A', 'a']
    initprobs = np.arange(.1,1,.1)
    
    for p0 in initprobs:
        results = defaultdict(dict)
        i=0
        pkl = open('./psims/n1000' + 'p' + str(int(100*p0)) + '.pkl', 'ab')
        p = p0
        while gens > i:
            p = round(np.random.binomial(2*pop, p)/float(2*pop), 3)
            i += 1
            results[i] = p 
        pk.dump({pid:results}, pkl)
        pkl.close()
    return



def wf_pickle_n10000(pid):
    gens = pop = 10000
    anames = ['A', 'a']
    initprobs = np.arange(.1,1,.1)
    
    for p0 in initprobs:
        results = defaultdict(dict)
        i = 0
        pkl = open('./psims/n10000' + 'p' + str(int(100*p0)) + '.pkl', 'ab')
        p = p0
        while gens > i:
            p = round(np.random.binomial(2*pop, p)/float(2*pop), 3)
            i += 1
            results[i] = p
        pk.dump({pid:results}, pkl)
        pkl.close()
    return

def wf_pickle_n100000(pid):
    gens = pop = 100000
    anames = ['A', 'a']
    initprobs = np.arange(.1,1,.1)
    
    for p0 in initprobs:
        results = defaultdict(dict)
        i = 0
        pkl = open('./psims/n100000' + 'p' + str(int(100*p0)) + '.pkl', 'ab')
        p = p0
        while gens > i:
            p = round(np.random.binomial(2*pop, p)/float(2*pop), 3)
            i += 1
            results[i] = p
        pk.dump({pid:results}, pkl)
        pkl.close()
    return

if __name__ == '__main__':
    import time

    pool = mpr.Pool(processes=mpr.cpu_count() -1)

    t1 = time.time()
    pool.map(wf_pickle_n100, range(1000))
    t2 = time.time()
   
    print 'first done in', t2-t1

    t3 = time.time()
    pool.map(wf_pickle_n1000, range(1000))
    t4 = time.time()
    
    print 'second done in', t4-t3

    t5=time.time()
    pool.map(wf_pickle_n10000, range(1000))
    t6=time.time()

    print 'third done in', t6-t5

    t7=time.time()
    pool.map(wf_pickle_n100000, range(1000))
    t8=time.time()
    
    print 'last done in', t8-t7
    
    print 'All together:'
    print '1st:', t2-t1, '2nd:',t4-t3, '3rd:', t6-t5, '4th:',t8-t7
