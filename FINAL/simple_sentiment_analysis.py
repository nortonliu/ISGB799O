import pandas as pd 
from textblob import TextBlob
#import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

file_list = ['full_records_beyond_burger.txt','full_records_impossible_burger.txt','full_records_impossible_whopper.txt']
output_name = ['attitudes_beyond_burger.csv','attitudes_impossible_burger.csv','attitudes_impossible_whopper.csv']

for n in range(len(file_list)):
	reviews = pd.read_table('D:/Fordham Fall Homework Assignment/Web Analytics/group project due_10_Dec/'+file_list[n], sep = '::',
	 names = ['user_name', 'location', 'id_str', 'followers_count', 'friends_count', 'favourites_count', 'time_zone', 'tweet'])

	df = reviews.copy()

	df['tweet'] = df['tweet'].fillna('999')
	missing = df[(df.tweet == '999')].index.tolist()
	df = df.drop(missing)
	print(df['tweet'].isnull().value_counts())

	attitudes1 = list()
	attitudes2 = list()

	for tweet in df['tweet']:
		testimonial = TextBlob(str(tweet))
		attitude1 = testimonial.sentiment.polarity
		attitudes1.append(attitude1)
	df['textblob'] = attitudes1

	sid = SentimentIntensityAnalyzer()
	for tweet in df['tweet']:
		attitude2 = sid.polarity_scores(tweet)['compound']
		attitudes2.append(attitude2)
	df['nltk_vader'] = attitudes2

	print(df.head())
	print(df.tail())

	df.to_csv(output_name[n],mode='w')