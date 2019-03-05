import joblib as jl

class SybilRankerBase:
	ranker = None
	def __init__(self, modelFilename):
		self.ranker = jl.load( modelFilename )	
				
	def getRank(self, node_name):
		return self.ranker.getRank(node_name)
	
	def validate(self):
		self.ranker.validate()
		