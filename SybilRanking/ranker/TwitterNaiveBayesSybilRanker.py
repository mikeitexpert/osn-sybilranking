# internal imports
from .SybilRankerBase import SybilRankerBase
from ..model import TwitterNaiveBayesSybilRankerFactory

class TwitterNaiveBayesSybilRanker(SybilRankerBase):
	def __init__(self):
		super(TwitterNaiveBayesSybilRanker, self).\
			__init__(
				TwitterNaiveBayesSybilRankerFactory.modelFilename
			)
	