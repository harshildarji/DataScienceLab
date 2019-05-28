# Script to provide a simple command line interface to perform manual annotation!

import csv
import sys

train_data = open('train_data.csv', 'a')
train_label = open('train_label.csv', 'a')
with open('all_data.csv') as f:
        data = csv.reader(f)
        for line in data:
                try:
                        print('\n' + line[2][2:-1])
                        label = input('Label [0/1]: ')
                        if not label:
                                sys.exit()
                        train_data.write(','.join(line) + '\n')
                        train_label.write(label + '\n')
                except Exception as e:
                        #print(e)
                        pass
train_data.close()
train_label.close()