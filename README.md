# corrfeatred



reduce features using correlation matrix 

## Installation 

```bash
pip install corrfeatred
```


## Usage 

```python


from corrfeatred import reduce_features

correlation_matrix = #correlation matrix
feature_set = reduce_features(correlation_matrix, threshhold=0.8, policy='min')


# if you want another set of features for same correlation matrix, then use random seed to change the output.

different_feature_set = reduce_features(correlation_matrix, threshhold=0.8, policy='min', random_seed = 42)
```


## Workflow

Currently there is only one function which takes correlation matrix and threshholds as input and then constructs a graph. 

There after we find maximal cliques in the graph and our goal is to have at max one feature from each clique.


![workflow](https://github.com/abhi-glitchhg/corrfeatred/assets/72816663/b67118f6-f7dd-4123-8adc-23045b7b63f7)




