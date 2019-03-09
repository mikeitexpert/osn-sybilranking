import SybilRanking as sb

# report classficition accuracy
sybilRanker = sb.ranker.InstaNaiveBayesSybilRanker()
sybilRanker.validate()

# peform ranking
twitterUserList = [
	'mikeitgeek',
]

print("username,rank")
for username in twitterUserList:
	print ('{},{}'.format(
		username,
		sybilRanker.getRank(username))
	)
