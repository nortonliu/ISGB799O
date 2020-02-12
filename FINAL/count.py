import numpy as np 
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_excel('attitudes_all.xlsx',encoding = 'ansi')

count_vectorizer = CountVectorizer(ngram_range=(1, 2),stop_words = 'english')

df = data.copy()
X_text = df['tweet']
count_vectorizer.fit(X_text)
X = count_vectorizer.transform(X_text)
words = count_vectorizer.get_feature_names()
print(type(words))
print(type(X.toarray()))
words_df = pd.DataFrame(X.toarray())
words_df.columns = words
words_df = words_df.T
words_df['row_sum'] = words_df.apply(lambda x: x.sum(), axis = 1)
print(words_df['row_sum'])
words_df['row_sum'].to_csv('word_frequency_only.csv')
print('finish')