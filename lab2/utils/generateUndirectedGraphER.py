import itertools
import random
from collections import defaultdict

class generateUndirectedGraphER:
    # params
    # n: numero di nosi
    # p: probabilita che un certo nodo venga estratto
    def __init__(self,n,p):
        if p >= 0 and p <= 1:
            self.n = n
            self.p = p
            self.V = set(range(n))
            self.adj_list = defaultdict(set)
            for pairs in itertools.combinations(self.V,2):
                if random.random() < p and pairs[0] != pairs[1]:
                    self.adj_list[pairs[0]].add(pairs[1])
            # print self.V
            # print self.E
        else:
            print ("Error: p must be in [0,1]")

# generateUndirectedGraphER(4,0.3)
