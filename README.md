
[![Publish to PyPI](https://github.com/abhi-glitchhg/corrfeatred/actions/workflows/publish.yml/badge.svg)](https://github.com/abhi-glitchhg/corrfeatred/actions/workflows/publish.yml) [![Tests](https://github.com/abhi-glitchhg/corrfeatred/actions/workflows/test.yml/badge.svg)](https://github.com/abhi-glitchhg/corrfeatred/actions/workflows/test.yml)

# corrfeatred

select features using correlation matrix 

## Installation 

```bash
pip install corrfeatred
```


## Usage 

```python


from corrfeatred import reduce_features

correlation_matrix = #correlation matrix
feature_set = reduce_features(correlation_matrix, threshold=0.8, policy='min')


# if you want another set of features for same correlation matrix, then use random seed to change the output.

different_feature_set = reduce_features(correlation_matrix, threshold=0.8, policy='min', random_seed = 42)
```


## Idea and workflow

Currently there is only one function which takes correlation matrix and thresholds as input and then constructs a graph. 


We create a graph where each node is represents a feature, and edge represents collinearity between the features. Then maximal cliques present in the graph are calculated. 


Each clique represents a cluster of features that are correlated with each other, and hence only one feature from this cluster is enough to represent whole cluster in the final feature sets. Hence, we can have multiple policies about how we want to choose the features (minimum number of features, maximum number of features etc).

Our goal is to have at max one feature from each clique.

And finally the feature set we get from this function will all have pairwise correlation less than the threshhold. 

![workflow](https://github.com/abhi-glitchhg/corrfeatred/assets/72816663/731c0be4-75a0-4355-b4aa-7682d7759d38)





 






