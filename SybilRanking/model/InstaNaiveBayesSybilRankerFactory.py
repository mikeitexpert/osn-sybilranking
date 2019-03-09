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
from SybilRanking.scraper import InstagramScraper

class InstaNaiveBayesSybilRankerFactory:
	basePath = os.path.dirname(
			os.path.abspath(inspect.getfile(inspect.currentframe()))
		)
	modelFilename = basePath + \
		'/modelfiles/InstaNaiveBayesSybilRanker.joblib'
	trainDataFilename = basePath + \
		'/traindata/insta_train_data.csv'

	def __init__(self):
		# Importing dataset
		print(pd.__path__)
		self.data = pd.read_csv( self.trainDataFilename, sep=",",
									encoding='latin1')
		data = self.data
		data.fillna('', inplace=True)

		data = pd.read_csv( self.trainDataFilename,
			sep=",", encoding='latin1' )

		data = data.drop(
				['username'], 1)

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
		data = self.data
		data = data.drop(['username'], 1)

		X = data.drop('bot', 1)
		Y = data['bot']
		bScores = cross_val_score(self.gnb, X, Y, cv=10)
		print('crossvalidated accuracy after NaiveBayesSybilRanker: {}'\
			.format(bScores.mean()))

	def getRank(self, nodeName):
		args = dict(
				username = nodeName,
				usernames = [],
				login_user= SybilRanking.settings.insta_username,
				login_pass= SybilRanking.settings.insta_password)

		scraper = InstagramScraper(**args)
		scraper.login()
		userData = scraper.scrapeUser( username = nodeName)
		userData.pop(0)
		detectedClass = self.gnb.predict( [userData] )
		print("detectedClass = ", detectedClass)
		predict_proba = self.gnb.predict_proba( [userData] )
		print("predict_proba = ", predict_proba)
		return predict_proba[0][0]*100
