# Dataset: https://archive.org/download/archiveteam-twitter-stream-2018-04/twitter-2018-04-24.tar
# Script to extract only the necessary tweets (and relevant features of it) from the enitre dataset using a list of keywords!

import os
import pandas as pd
import time
import re
 
keyWords = ['migration', 'immigration', 'immigrants', 'migrants', 'immigrate','migrate']
wordRe = re.compile('|'.join(keyWords), re.IGNORECASE)

start = time.time()

f = open('all_data.csv', 'a')
f.write('user_id,user_desc,tweet,loc\n')
rootDir = './dataset'
tweets = 0

def clean(_text):
    _cleaned = ' '.join(re.sub(r'(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z\t])|(http\S+)',' ', _text).split())
    return (_cleaned).strip().lower()

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        print(dirName + '/' + fname)
        try:
            data = pd.read_json(dirName + '/' + fname, lines = True)
            data = data[data.extended_tweet.notnull()].reset_index()

            for uid, lang in enumerate(data['lang']):
                try:
                    if lang == 'en':
                        user_id = str(data['user'][uid]['id'])
                        user_desc = clean(str(data['user'][uid]['description']))
                        text = clean(str(data['extended_tweet'][uid]['full_text']))
                        location = str(data['user'][uid]['location']).replace(',', ' ')

                        line = user_id + ',' + user_desc + ',' + text + ',' + location

                        if wordRe.search(text):
                            f.write(line + '\n')
                            tweets += 1

                except Exception as e:
                    #print(e)
                    pass
        except Exception as e:
            #print(e)
            pass

f.close()
end = time.time()

print('\nNumber of tweets: {}'.format(tweets))
print('Total time: {} m'.format((end - start)/60))