from sklearn.metrics import cohen_kappa_score
import pandas as pd 
import itertools

dilip = pd.read_csv('dilip.csv')
harshil = pd.read_csv('harshil.csv')
abhishek = pd.read_csv('abhishek.csv')
arsal = pd.read_csv('arsal.csv')

dfs = [harshil, abhishek, dilip, arsal]
_dfs = ['Harshil', 'Abhishek', 'Dilip', 'Arsal']

comb = list(itertools.combinations(dfs, 2))
_comb = list(itertools.combinations(_dfs, 2))

sum_ = 0
for i in range(len(comb)):
    ck = cohen_kappa_score(comb[i][0]['label'], comb[i][1]['label'])
    print('{} - {}: {:.4f}'.format(_comb[i][0], _comb[i][1], ck))
    sum_ += ck

print('-' * 24, '\nMean Cohen\'s kappa: {:.4f}'.format(sum_ / 6))