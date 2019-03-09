import traceback as tb

from .test_twitter_naivebayes_ranker_factory import test_twitter_naivebayes_ranker_factory
from .test_twitter_naivebayes_ranker import test_twitter_naivebayes_ranker
from .test_insta_naivebayes_ranker_factory import test_insta_naivebayes_ranker_factory
from .test_insta_naivebayes_ranker import test_insta_naivebayes_ranker

def doAllTest():
    allTests = [
            (test_twitter_naivebayes_ranker_factory,
                'test_twitter_naivebayes_ranker_factory'),
            (test_twitter_naivebayes_ranker,
                 'test_twitter_naivebayes_ranker'),
            (test_insta_naivebayes_ranker_factory,
                 'test_insta_naivebayes_ranker_factory'),
            (test_insta_naivebayes_ranker,
                 'test_insta_naivebayes_ranker')

    ]
    for test, testDesc in allTests:
        doTest(test, testDesc)
def doTest(testFunc, testDesc):
    try:
        result = testFunc()
    except Exception as e:
        print("\t Test Failed: ", e)
        tb.print_exc()
        result = False
    print("Testing {}: Result: {}".format(
        testDesc,
        result)
          )
