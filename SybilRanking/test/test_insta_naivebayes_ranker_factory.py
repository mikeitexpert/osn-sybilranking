import SybilRanking as sb

def test_insta_naivebayes_ranker_factory():
    tnbrf = sb.model.InstaNaiveBayesSybilRankerFactory()
    tnbrf.validate()
    return True
