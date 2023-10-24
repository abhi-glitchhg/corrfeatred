import numpy as np
from collections import defaultdict
import networkx as nx
from networkx.algorithms import clique


def reduce_features(corr_matrix, threshhold=0.0):


    """
    correlation matrix : df.corr
    threshhold: float
    method: 
    """

    # if summ >=2 then self loop zero 
    for i in range(corr_matrix.shape[0]):
        if corr_matrix[i].sum() >=2:
            corr_matrix[i][i]=0
    

    G = nx.Graph(corr_matrix)     
     
    cliques = list(clique.find_cliques(G))
    cliques = sorted(cliques, key=lambda x: len(x), reverse=True)
    mask = np.zeros(len(cliques), dtype=bool)
    feature_set = []
     
    dict1 = defaultdict(lambda : 0)
    dict2 = defaultdict(list)
    
    for idx, clq in enumerate(cliques):
            for key in clq:
                dict1[key]+=1
                dict2[key].append(idx)
    while not np.all(mask): 

        # print(dict1, "\n", dict2)

        
        sorted_list = sorted(dict1.items(), key = lambda kv: kv[1], reverse=True)
        # print(sorted_list)
        
        top = sorted_list[0]
        # print(top)
        feature_set.append(top[0])
        mask[dict2[top[0]]] = True
        # print(mask)
        
        for i in dict2[top[0]]:
            for j in cliques[i]:
                dict1[j]-= 1

        # print("iter finished \n\n\n")
    return feature_set





if __name__ == "__main__":
    adjacency_matrix = np.array([
    
                             [1,1,1,0,0,0,1,1,0,0], #a
                             [1,1,1,0,0,0,0,0,0,0], #b
                             [1,1,1,1,0,0,0,0,0,0], #c 
                             [0,0,1,1,1,0,0,0,0,0], #d 
                             [0,0,0,1,1,1,0,0,0,0], #e
                             [0,0,0,0,1,1,1,1,1,0], #f
                             [1,0,0,0,0,1,1,1,1,0], #g
                             [1,0,0,0,0,1,1,1,1,0], #h
                             [0,0,0,0,0,1,1,1,1,0], #i
                             [0,0,0,0,0,0,0,0,0,1]
                             ])
    
    a = reduce_features(adjacency_matrix,0.0)

    print(f"final feautre set is: {a}")


