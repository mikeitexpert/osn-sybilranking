# standard
import inspect, os
import requests

# third party
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.model_selection import cross_val_score
import joblib as jl

#internal
import SybilRanking.settings

class TwitterNaiveBayesSybilRankerFactory:
	basePath = os.path.dirname(
			os.path.abspath(inspect.getfile(inspect.currentframe()))
		)
	modelFilename = basePath + \
		'/modelfiles/TwitterNaiveBayesSybilRanker.joblib'
	trainDataFilename = basePath + \
		'/traindata/twitter_train_data.csv'

	def __init__(self):
		# Importing dataset
		print(pd.__path__)
		self.data = pd.read_csv( self.trainDataFilename, sep=",", encoding='latin1')
		data = self.data
		data.fillna('', inplace=True)

		data = pd.read_csv( self.trainDataFilename,
			sep=",", encoding='latin1' )

		data = data.drop(
				['id', 'id_str', 'url', 'default_profile',
				'default_profile_image', 'screen_name',
				'location', 'has_extended_profile', 'status',
				'lang', 'description', 'created_at', 'name'], 1)

		X = data.drop('bot', 1)
		Y = data['bot']

		# create model
		self.gnb = BernoulliNB()

		# Train classifier
		self.gnb.fit(X, Y)

		# save model
		jl.dump(self, self.modelFilename)

	def validate(self):
		# Importing dataset
		# data = pd.read_csv( self.basePath + self.trainDataFilename, sep=",", encoding='latin1')
		data = self.data
		data = data.drop(['id', 'id_str', 'url', 'default_profile',
				 'default_profile_image', 'screen_name', 'location',
		         'has_extended_profile', 'status', 'lang',
		         'description', 'created_at', 'name'], 1)

		X = data.drop('bot', 1)
		Y = data['bot']
		bScores = cross_val_score(self.gnb, X, Y, cv=10)
		print('\tcrossvalidated accuracy after NaiveBayesSybilRanker: {}'\
			.format(bScores.mean()))

	def getRank(self, nodeName):
		proxies = SybilRanking.settings.proxies
		access_token = SybilRanking.settings.twitter_access_token

		search_headers = {
		    'Authorization': 'Bearer {}'.format(access_token)
		}
		keymap = {
			"favorites_count": "favourites_count",
			"listedcount": "listed_count"
		}
		search_params = {
		    'screen_name': nodeName
		}
		base_url = 'https://api.twitter.com/'
		search_url = '{}1.1/users/show.json'.format(base_url)
		search_resp = requests.get(search_url,
				headers=search_headers,
				params=search_params,
				proxies = proxies)
		tweet_data = search_resp.json()
		oneRow = []
		userInfoKey =  """
			id,id_str,screen_name,location,description,url,followers_count,
			friends_count,listedcount,created_at,favourites_count,verified,
			statuses_count,lang,status,default_profile,default_profile_image,
			has_extended_profile,name,bot
		""".replace('\t', '').replace('\n', '')
		userInfoKey = userInfoKey.split(',')

		dropList = ['id', 'id_str', 'url', 'default_profile',
			'default_profile_image', 'screen_name',
			'location', 'has_extended_profile',
			'status', 'lang', 'description',
			'created_at', 'name', 'bot']
		oneRow = []
		for key in userInfoKey:
			if key in dropList:
				continue
			try:
				oneRow.append( tweet_data[key] )
			except KeyError:
				try:
					oneRow.append( tweet_data[keymap[key]] )
				except KeyError:
					print("bad key: '{}'".format(key))
			if key == 'screen_name':
				oneRow[-1] = (oneRow[-1])
			elif key == 'id_str':
				oneRow[-1] = float(oneRow[-1])

		detectedClass = self.gnb.predict( [oneRow] )
		print("\tdetectedClass = ", detectedClass)
		predict_proba = self.gnb.predict_proba([oneRow])
		print("\tpredict_proba = ", predict_proba)
		return predict_proba[0][0]*100
