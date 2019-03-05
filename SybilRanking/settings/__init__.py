import os,inspect
import json
basePath = os.path.dirname(
		os.path.abspath(inspect.getfile(inspect.currentframe()))
	)

settingsFilename = basePath + '/settings.json'
with open(settingsFilename, 'r') as settingsFile:
	settings = json.load( settingsFile )
	proxies = settings['proxies']
	access_token = settings['access_token']
