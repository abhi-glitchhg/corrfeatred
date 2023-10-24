import numpy as np
from collections import defaultdict
import networkx as nx
from networkx.algorithms import clique


def reduce_features(corr_matrix, threshhold):


    """
    correlation matrix : df.corr
    threshhold: float
    method: 
    """

    corr_matrix_ = np.triu(corr_matrix)
    for i in range(corr_matrix_.shape[0]):
        corr_matrix_[i][i] = 0

    G = nx.Graph(corr_matrix)

    cliques = clique.find_cliques(G)
    



if __name__ == "__main__":
    adjacency_matrix = np.array([
    
                             [1,1,1,0,0,0,1,1,0], #a
                             [1,1,1,0,0,0,0,0,0], #b
                             [1,1,1,1,0,0,0,0,0], #c 
                             [0,0,1,1,1,0,0,0,0], #d 
                             [0,0,0,1,1,1,0,0,0], #e
                             [0,0,0,0,1,1,1,1,1], #f
                             [1,0,0,0,0,1,1,1,1], #g
                             [1,0,0,0,0,1,1,1,1], #h
                             [0,0,0,0,0,1,1,1,1], #i
                             ])



