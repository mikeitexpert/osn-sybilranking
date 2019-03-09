import SybilRanking as sb

def test_insta_naivebayes_ranker():
	# report classficition accuracy
	sybilRanker = sb.ranker.InstaNaiveBayesSybilRanker()
	sybilRanker.validate()

	# peform ranking
	twitterUserList = [
		'mikeitgeek',
	]

	print("\tusername,rank")
	for username in twitterUserList:
		print ('\t{},{}'.format(
			username,
			sybilRanker.getRank(username))
		)
	return True
