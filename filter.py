# Dataset: https://archive.org/download/archiveteam-twitter-stream-2018-04/twitter-2018-04-24.tar
# Script to extract only the necessary tweets (and relevant features of it) from the enitre dataset using a list of keywords!

import os
import pandas as pd
import time
import re
import multiprocessing

def clean(_text):
    _cleaned = ' '.join(re.sub(r'(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z\t])|(http\S+)',' ', _text).split())
    return (_cleaned).strip().lower()

def _readJson(_file):
    print(_file)

    keyWords = ['migration', 'immigration', 'immigrants', 'migrants', 'immigrate','migrate']
    wordRe = re.compile('|'.join(keyWords), re.IGNORECASE)

    f = open('new_data.csv', 'a')
    try:
        data = pd.read_json(_file, lines = True)
        data = data[data.extended_tweet.notnull()].reset_index()

        for uid, lang in enumerate(data['lang']):
                if lang == 'en':
                    user_desc = clean(str(data['user'][uid]['description']))
                    text = clean(str(data['extended_tweet'][uid]['full_text']))

                    line = user_desc + ',' + text

                    if wordRe.search(text):
                        f.write(line + '\n')
                            
    except Exception as e:
        #print(e)
        pass

    f.close()

if __name__ == '__main__':
    start = time.time()

    #f.write('user_id,user_desc,tweet,loc\n')
    rootDir = './dataset'

    files = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            files.append(dirName + '/' + fname)
            
    pool = multiprocessing.Pool()
    pool.map(_readJson, files)
    pool.close()

    end = time.time()

    df = pd.read_csv('all_data.csv')
    print('\nNumber of tweets: {}'.format(df.shape[0]))
    print('Total time: {} h'.format((end - start)/3600))