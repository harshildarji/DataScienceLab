import pandas as pd 
import sys

data = pd.read_csv('all_data.csv')

train_data = open('train_data.csv', 'a')
train_label = open('train_label.csv', 'a')

written = open('labeled', 'r')
_labeled = list(map(int, written.read().split()))

def _close():
    with open('labeled', 'w') as f:
        f.write(' '.join(list(map(str, _labeled))))
    f.close()
    train_data.close()
    train_label.close()

for _id, t in enumerate(data['tweet']):
    if _id not in _labeled:
        print('\n' + t)
        label = input('Label [0/1]: ')

        if not label: 
            _close()
            sys.exit()

        train_data.write(','.join([str(data['desc'][_id]), t]) + '\n')
        train_label.write(label + '\n')
        _labeled.append(_id)

_close()