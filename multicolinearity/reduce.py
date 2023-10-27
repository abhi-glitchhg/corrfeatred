import numpy as np
from collections import defaultdict
import networkx as nx
from networkx.algorithms import clique
import pandas as pd
import random

def reduce_features(corrmatrix, threshhold=0.75,method_='min', random_state=None):


#     """
#     correlation matrix : df.corr
#     threshhold: float
#     method: `min` or `max` default is min 
#     """

    if random_state!=None:
        random_gen = random.Random(random_state)

    inf_ = 3*(corrmatrix.shape[0]) + 10 # adding 10 for no reason, this could be any positive number; but messi is GOAT.
    corr_matrix = corrmatrix > threshhold
    assert method_ in ('min', 'max'), "wrong input parameter"
    method = max if method_ == 'min' else min
    feature_set = []
    del_this = []
    cols = np.array(corr_matrix.columns)
    corr_matrix = corr_matrix.values.astype(bool)
    # if summ >=2 then self loop zero
    for i in range(corr_matrix.shape[0]):
        if corr_matrix[i].sum() >=2:
            corr_matrix[i][i]=0
        else:
            feature_set.append(cols[i])
            del_this.append(i)
    corr_matrix = np.delete(np.delete(corr_matrix, del_this, axis=0), del_this, axis=1)
    cols_new = np.delete(cols, del_this, axis=0)
    G = nx.Graph(corr_matrix)    
    cliques = list(clique.find_cliques(G))
    # print(cliques)
    cliques = sorted(cliques, key=lambda x: len(x), reverse=True)
    mask = np.zeros(len(cliques), dtype=bool)
   
    dict1 = defaultdict(lambda : 0)
    dict2 = defaultdict(list)
    # print("lfg")
    for idx, clq in enumerate(cliques):
            for key in clq:
                dict1[key]+=1 # a node present in how many groups
                dict2[key].append(idx) # node to group mapping
    while not np.all(mask):

        if random_state==None:
            top = method(dict1.items(), key = lambda kv: kv[1])
        else:
            dict_items = list(dict1.items())
            random_gen.shuffle(dict_items)
            top = method(dict_items, key = lambda kv: kv[1])
            del dict_items
        
        if top[1] <=0 : break
        if top[1] >= inf_: break
        feature_set.append(cols_new[top[0]])
       
        assert sum(mask[dict2[top[0]]]) == 0, "sum should be zero here"
       
        mask[dict2[top[0]]] = True
       
        for i in dict2[top[0]]:
            for j in cliques[i]:
                dict1[j]-= 1
        # direct connections with top[0] must be made 0;
       
        for i in np.where(corr_matrix[top[0]])[0]: 
          if method_ == 'min': 
            dict1[i] = 0
          else:
            dict1[i] = inf_ 

        if method_ == 'min': 
          dict1[top[0]] = 0
        else:
          dict1[top[0]] = inf_
        #print(dict1.items())
       
       
    return feature_set
if __name__ == "__main__":
    adjacency_matrix = pd.DataFrame(np.array([
    
                             [1,1,1,0,0,0,1,1,0], #a
                             [1,1,1,0,0,0,0,0,0], #b
                             [1,1,1,1,0,0,0,0,0], #c 
                             [0,0,1,1,1,0,0,0,0], #d 
                             [0,0,0,1,1,1,0,0,0], #e
                             [0,0,0,0,1,1,1,1,1], #f
                             [1,0,0,0,0,1,1,1,1], #g
                             [1,0,0,0,0,1,1,1,1], #h
                             [0,0,0,0,0,1,1,1,1], #i
                             ]))
    
    a = reduce_features(adjacency_matrix,0.75)

    print(f"final feautre set is: {a}")

    b = reduce_features(adjacency_matrix, 0.75, 'max')
    print(b)

    print(reduce_features(adjacency_matrix, 0.75, 'max', 42))

