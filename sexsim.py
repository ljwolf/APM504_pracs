from collections import defaultdict
import pickle as pk
import time
#import psutil
import multiprocessing as mpr
import numpy as np

def sexsim(fpct, p0, gens):
    pop = 2 * gens
    mpct = fpct
    i=0
    while gens > i:
        i +=1
        fpct = round(np.random.binomial(int(fpct * pop), fpct) / (fpct * pop), 3)
        mpct = round(np.random.binomial(int(fpct * pop), fpct) / (fpct * pop), 3)
        results[i] = (fpct, mpct)
    return results

def sexsim_ps(fpct, pop, gens):
    mpct = round(1 - fpct, 2)
    plist = np.arange(.1,1,.1)
    for p0 in plist:
        p_f = p0
        p_m = p0
        mpct = 1 - fpct
        i = 0
        pkl = open('./sexsims/' + str(int(fpct*100)) + 'p' + str(int(100*p0)) + '.pkl', 'ab')
        results = []
        while gens > i:
            i +=1
            p_f = round(np.random.binomial(int(fpct * pop), p_f) / (fpct * pop), 3)
            p_m = round(np.random.binomial(int(mpct * pop), p_m) / (mpct * pop), 3)
            results.append((p_f, p_m))
        pk.dump(results, pkl)
        pkl.close()
