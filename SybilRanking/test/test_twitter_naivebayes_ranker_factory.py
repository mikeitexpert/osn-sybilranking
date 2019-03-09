import SybilRanking as sb
def test_twitter_naivebayes_ranker_factory():
    tnbrf = sb.model.TwitterNaiveBayesSybilRankerFactory()
    tnbrf.validate()
    return True
    
