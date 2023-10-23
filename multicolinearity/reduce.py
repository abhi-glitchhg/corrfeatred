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

    
    

    G = nx.Graph(corr_matrix)

    cliques = clique.find_cliques(G)
    # thnk about some algo to do stuff.


