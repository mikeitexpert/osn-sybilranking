import tensorflow as tf
import SybilRanking as sb

def test(argv):
    igdesrf = sb.model.InstaDNNEstimatorSybilRankerFactory()
    igdesrf.validate()
    return True

def test_insta_dnn_estimator_ranker_factory():
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(test)
    return True
