#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__authors__ = "zc"
__copyright__ = "Copyright 2015, zc"
__license__ = "MIT"
__email__ = "newvalue92@gmail.com"


#!/usr/bin/env python


from itertools import permutations
import pdb
import random
from math import factorial, ceil



class KDDCorpus:
    def __init__(self, path, path2):
        self.path = path
        self.path2 = path2

        # count number of doc
        length = 0
        for d in self:
            length += 1
        self.length = length

    def __iter__(self):
        maxgen = 100
        with open(self.path2) as f:
            for l in f:
                l = l.strip()
                d2 = l.strip().split('/')
                # generate data from each transaction
                k = [d2[0], d2[0] + '/'+ d2[1], \
                     d2[0] + '/' + d2[1] + '/' + d2[2]]
                kd = k + [l] + k[::-1]
                for i in xrange(maxgen):
                    yield kd[1:-1]
                    yield kd[2:-2]
                    yield kd

        with open(self.path) as f:
            for l in f:
                l = l.strip()
                for d in self.gen_data(l):
                    yield d

    def __len__(self):
        return self.length

    def gen_data(self, l):
        d = l.strip().split(';')
        #maxperm = 1000   # number of permutaion because av(numiterm) ~ 5
        n = len(d)
        #maxrepeat = 80
        maxdupplicate = 10;
        maxorder = 100
        if len(d) > 1:
            # yield list of product in order
            for i in xrange(maxorder):
                yield d   #return list of product in order


            # yield some permutaion of all purchase products
            maxperm = maxdupplicate * len(d) * max(n - 3, 1)
            maxperm = min(maxperm, 1000)

            for i in xrange(maxperm):
                random.shuffle(d)
                yield d

class TreeContextCorpus:
    def __init__(self, maxA=20, maxB=30000, maxC=30000, maxD=30000):
        self.maxA = maxA;
        self.maxB = maxB;
        self.maxD = maxD;
        self.maxC = maxC;
    def __iter__(self):
        for a in xrange(1, self.maxA + 1):
            for b1 in xrange(1, self.maxB + 1):
                for b2 in xrange(1, self.maxB + 1):
                    catA = 'A%05d'%a
                    catB1 = 'A%05d/B%05d'%(a,b1)
                    catB2 = 'A%05d/B%05d'%(a,b2)
                    dk= [catA, catB1,catB2, catA]
                    yield dk

        for a in xrange(1, self.maxA + 1):
            for b in xrange(1, self.maxB + 1):
                for c1 in range(1, self.maxC + 1):
                    for c2 in range(1, self.maxC + 1):
                        catA = 'A%05d'%a
                        catB = 'A%05d/B%05d'%(a,b)
                        catC1 = '%s/C%05d'%(catB,c1)
                        catC2 = '%s/C%05d'%(catB,c2)
                        dk= [catA, catB, catC1 ,catB, catA];
                        yield dk

        for a in xrange(1, self.maxA + 1):
            for b in xrange(1, self.maxB + 1):
                for c in xrange(1, self.maxC + 1):
                    for d1 in xrange(1, self.maxD + 1):
                        for d2 in xrange(1, self.maxD + 1):
                            catA = 'A%05d'%a
                            catB = 'A%05d/B%05d'%(a,b)
                            catC = '%s/C%05d'%(catB,c)
                            catD1 = '%s/D%05d'%(catC,d1)
                            catD2 = '%s/D%05d'%(catC,d2)
                            dk= [catA, catB, catC, catD1, catD2, catC, catB, catA];
                            #for l in xrange(10):
                            yield dk



def main():
    data = KDDCorpus('./dat2', './data2')
    data = TreeContextCorpus(3, 3, 3, 3)
    for d in data:
        print d

if __name__ == '__main__':
    main()
