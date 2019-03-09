import SybilRanking as sb

def test_twitter_naivebayes_ranker():
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

	print("\tusername,rank")
	for username in twitterUserList:
		print ('\t{},{}'.format(
			username,
			sybilRanker.getRank(username))
		)
	return True
