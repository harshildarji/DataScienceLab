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

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        print(dirName + '/' + fname)
        data = pd.read_json(dirName + '/' + fname, lines = True)
        data = data[data.extended_tweet.notnull()].reset_index()

        for uid, lang in enumerate(data['lang']):
            try:
                if lang == 'en':
                    user_id = str(data['user'][uid]['id'])
                    user_desc = str(str(data['user'][uid]['description']).replace(',', ' ').replace('\n', ' ').encode('UTF-8'))
                    text = str(str(data['extended_tweet'][uid]['full_text'].replace(',', ' ').replace('\n', ' ')).encode('UTF-8'))
                    location = str(data['user'][uid]['location']).replace(',', ' ')

                    line = user_id + ',' + user_desc + ',' + text + ',' + location

                    if isinstance(text, str) and wordRe.search(text):
                        f.write(line + '\n')
                        tweets += 1

            except Exception as e:
                #print(e)
                pass
f.close()
end = time.time()

print('\nNumber of tweets: {}'.format(tweets))
print('Total time: {} h'.format((end - start)/3600))