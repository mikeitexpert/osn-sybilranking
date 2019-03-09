import os,inspect
import json
basePath = os.path.dirname(
		os.path.abspath(inspect.getfile(inspect.currentframe()))
	)

settingsFilename = basePath + '/settings.json'
with open(settingsFilename, 'r') as settingsFile:
	settings = json.load( settingsFile )
	proxies = settings['proxies']
	twitter_access_token = settings['twitter_access_token']
	insta_username = settings['insta_username']
	insta_password = settings['insta_password']
	
