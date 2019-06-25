# Data Science Lab - SS - 2019

Dataset: https://archive.org/download/archiveteam-twitter-stream-2018-04/archiveteam-twitter-stream-2018-04.tar

1. [filter.py](https://github.com/harshildarji/DataScienceLab/blob/master/filter.py)
<br/>This script will go through all the `JSON` files in `dataset` folder, and will only store the tweet if it matches following criterias:
<br/>- `extended_tweet` is **NOT** null
<br/>- `lang` is `en` (English)
<br/>- Tweet contains word(_s_) defined in `keyWords` list
<br/>It will not store all the details of a particular tweets, but only the features we require for our purpose:
<br/>- Twitter User Desciption
<br/>- Tweet
<br/>All this information will be stored in `csv` format (saved as `all_data.csv`).

2. [label.py](https://github.com/harshildarji/DataScienceLab/blob/master/label.py)
<br/>Since we need to manually annotate all the selected tweets, this script will provide a simple command line interface to help with that.
<br/>This will present the user with a tweet (from `all_data.csv`, line by line), user will input `1` or `0` where:
<br/>- `1`: Tweet is migration relevant
<br/>- `0`: Tweet is **NOT** migration relevant
<br/>Once the user will hit enter, label will be stored in `train_label.csv`.

3. [annotation.ipynb](https://github.com/harshildarji/DataScienceLab/blob/master/annotation.ipynb)
<br/>This notebook **trains** and performs **evaluation** on the first 1500 (_untill now_) **labelled** data.
<br/>Pipeline (_for now_):
<br/>- Import data, and remove rows with null values in any columns
<br/>- Prepare `TF-IDF` and `Doc2Vec` feature extraction techniques
<br/>- Provide appropriate data and labels to both the techniques, train classifiers using retrieved feature vectors and store their results in a `dict`
<br/>- Plot results!
