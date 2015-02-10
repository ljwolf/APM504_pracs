import pickle as pk
import numpy as np
import matplotlib.pyplot as plt

def depickle(fp_pkl): 
    first = True
    samplist = []
    ends = {}
    count = 1
    while fp_pkl:
        try:
            sim = pk.load(fp_pkl)
        except EOFError:
            break
        Afreqs = sim.values()[0].values()
        if first:
            Afreqs_mean = Afreqs
            first = False
        
        #means and sampled values
        Afreqs_mean = [m + (x - m)/float(count) for m,x in zip(Afreqs_mean, Afreqs)]
        nrec = len(sim)
        midfreq = Afreqs[nrec/2]
        endfreq = Afreqs[-1]
        samplist.append((midfreq, endfreq))

        #time to fixation
        Unknown = True
        for i in range(len(Afreqs)):
            if (Afreqs[i] < .01 or Afreqs[i] > .99) and Unknown:
                ends.update({count:i})
                Unknown = False
            if not Unknown:
                break
        count +=1
    return samplist, ends, Afreqs_mean

def meanends(fname, p0):
    sim = open(fname)
    samples, ends, means = depickle(sim)
    plt.figure(figsize=(1.6*5, 5))
    plt.plot(means)
    plt.title('Mean Allele Frequency, $p_0 = ' + p0 + '$')
    plt.xlabel('Generation')
    plt.ylabel('Mean $p_t$')
    print len(ends), ' Simulations Fixed in ', np.mean(ends.values()), 'generations (avg)'


def depickle_sex(fp_pkl):
    res = []
    ends = {}
    count = 1
    while fp_pkl: 
        try:
            sim = pk.load(fp_pkl)
            res.append(sim)
        except EOFError:
            break
        
        #time to fixation
        W_Known = False
        M_Known = False
        for i in range(len(sim)):
            
            #sex and directional fixation. Men and Women can either fix up and down.
            
            #women
            if sim[i][0] < .01 :
                ends.update({count:dict()})
                ends[count].update({'Wdo':i})
                W_Known = True
            if sim[i][0] > .99 :
                ends.update({count:dict()})
                ends[count].update({'Wup':i})
                W_Known = True
            
            #men
            if sim[i][1] < .01 :
                ends.update({count:dict()})
                ends[count].update({'Mdo':i})
                M_Known = True
            if sim[i][1] > .99 :
                ends.update({count:dict()})
                ends[count].update({'Mup':i})
                M_Known = True
            
            #Then, when we know both, we end. 
            if W_Known and M_Known: 
                break
        count += 1
    return res, ends






def ttfix(fp_pkl):
    first = True
    ends = {}
    count = 0 
    while fp_pkl:
        try:
            sim = pk.load(fp_pkl)
        except EOFError:
            break
        Afreqs = sim.values()[0].values()
        Unknown = True
        for i in range(len(Afreqs)):
            if Afreqs[i] < .01 and Unknown:
                ends.update({count: i})
                Unknown = False
            if not Unknown:
                break
        if count not in ends.keys():
            ends.update({count:np.nan})
        count +=1

