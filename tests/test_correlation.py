from corrfeatred import reduce_features
import numpy as np
import pandas as pd
def test_hello():
    print("welcome to corrfeatreds test suit")
    assert True


def test_correlation():
    for i in (4,8,10,12,16,22,100,500):
        rand_array = np.random.uniform(0,1,i*i).reshape(i,i)
        corr_arr = np.tril(rand_array) + np.triu(rand_array.T,1)
        assert (corr_arr!=corr_arr.T).sum().sum() == 0
        for j in range(i):
            corr_arr[j][j] = 1
        
        corr_matrix = pd.DataFrame(corr_arr,columns=[str(k) for k in range(i)], index=[str(k) for k in range(i)])
        for threshhold in (0.6,0.8,.99):
            print(i,threshhold)
            feats_min = reduce_features(corr_matrix, threshhold=threshhold, policy= 'min')
            feats_max = reduce_features(corr_matrix, threshhold=threshhold, policy='max')

            assert (corr_matrix[feats_max].loc[feats_max]>threshhold).sum().sum() == len(feats_max)
            assert (corr_matrix[feats_min].loc[feats_min]>threshhold).sum().sum() == len(feats_min)



