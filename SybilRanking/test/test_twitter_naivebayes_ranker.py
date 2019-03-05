import SybilRanking as sb

# report classficition accuracy
sybilRanker = sb.ranker.TwitterNaiveBayesSybilRanker()
sybilRanker.validate()

# peform ranking
twitterUserList = [
	'WeAreMessi', 
	'twitterdev',
	'RepJoeBarton',
	'HoustonPokeMap',
]

print("username,rank")
for username in twitterUserList:
	print ('{},{}'.format(
		username, 
		sybilRanker.getRank(username))
	)
	