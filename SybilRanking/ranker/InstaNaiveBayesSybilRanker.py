# internal imports
from .SybilRankerBase import SybilRankerBase
from ..model import InstaNaiveBayesSybilRankerFactory

class InstaNaiveBayesSybilRanker(SybilRankerBase):
	def __init__(self):
		super(InstaNaiveBayesSybilRanker, self).\
			__init__(
				InstaNaiveBayesSybilRankerFactory.modelFilename
			)
