
import numpy as np
from collections import defaultdict
import networkx as nx
from networkx.algorithms import clique
import random

def reduce_features(correlation_matrix, threshhold=0.75,policy='min', random_seed=None):


#     """
#     correlation_matrix : df.corr
#     threshhold: float
#     method: whether we want minimum number of features or maximum number of features. NOTE: this is bit unstable and sometimes `min` policy has more features than `max`, this depends on how graph develops. 
#     random_seed: random state, use this to get different set of features for same correlation matrix.  
#     """

    if random_seed!=None:
        random_gen = random.Random(random_seed)
    corrmatrix = correlation_matrix.abs().copy()
    inf_ = 4*(corrmatrix.shape[0]) + 10 # adding 10 for no reason, this could be any positive number;
    corr_matrix = corrmatrix > threshhold
    assert policy in ('min', 'max'), "wrong input parameter"
    method = max if policy == 'min' else min
    feature_set = []
    del_this = [] # to track features which are not correlated with any other feature. this will reduce the graph calculations
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
    
    cliques = sorted(cliques, key=lambda x: len(x), reverse=True)
    mask = np.zeros(len(cliques), dtype=bool)
   
    node_to_clique_count = defaultdict(lambda : 0) # this dictionary keeps updated as we select features.
    node_to_clique_list = defaultdict(list) # this dictionary is not updated  

    for idx, clq in enumerate(cliques):
            for key in clq:
                node_to_clique_count[key]+=1 # a node present in how many groups
                node_to_clique_list[key].append(idx) # node to group mapping
    while not np.all(mask):

        if random_seed==None:
            top = method(node_to_clique_count.items(), key = lambda kv: kv[1])
        else:
            dict_items = list(node_to_clique_count.items())
            random_gen.shuffle(dict_items)
            top = method(dict_items, key = lambda kv: kv[1])
            del dict_items
        
        if top[1] <=0 : break 
        if top[1] >= inf_//2: break
        feature_set.append(cols_new[top[0]])
       
       
        mask[node_to_clique_list[top[0]]] = True
        
        for i in np.where(corr_matrix[top[0]])[0]: 
          if policy == 'min': 
            node_to_clique_count[i] = 0
          else:
            node_to_clique_count[i] = inf_ 

        if policy == 'min': 
          node_to_clique_count[top[0]] = 0
        else:
          node_to_clique_count[top[0]] = inf_
        
       
    del corrmatrix
    return feature_set

