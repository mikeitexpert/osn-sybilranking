from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import os
import inspect
import joblib as jl
import tensorflow as tf
import pandas as pd
# import iris_data
# import insta_data
# print("iris_data = ", iris_data.__path__)
from sklearn.model_selection import train_test_split

class InstaDNNEstimatorSybilRankerFactory:
    basePath = os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe()))
           )
    trainDataFilename = basePath + \
        '/traindata/insta_igaudit_train_data.csv'
    hiddenUnits = [10, 10]
    batchSize = 100
    trainSteps = 1000
    noClasses = 2
    modelDir = basePath + '/modelfiles/dnn_estimator'

    def __init__(self):
        # Importing dataset
        print(pd.__path__)
        print("self.trainDataFilename = ", self.trainDataFilename)
        self.data = pd.read_csv( self.trainDataFilename, sep=",",
                                    encoding='latin1')
        # data = self.data
        # data.fillna('', inplace=True)
        #
        # data = pd.read_csv( self.trainDataFilename,
        #     sep=",", encoding='latin1' )

        self.X, self.Y = InstaDNNEstimatorSybilRankerFactory.load_data()

        # prepare feature columns
        my_feature_columns = []
        for key in self.X.keys():
            my_feature_columns.append(tf.feature_column.numeric_column(key=key))

        # Build 2 hidden layer DNN with 10, 10 units respectively.
        self.dnn = tf.estimator.DNNClassifier(
            feature_columns=my_feature_columns,
            model_dir = InstaDNNEstimatorSybilRankerFactory.modelDir,
            hidden_units = InstaDNNEstimatorSybilRankerFactory.hiddenUnits,
            n_classes = InstaDNNEstimatorSybilRankerFactory.noClasses)

        # Train the Model.
        batch_size = InstaDNNEstimatorSybilRankerFactory.batchSize
        train_steps = InstaDNNEstimatorSybilRankerFactory.trainSteps
        self.dnn.train(
            input_fn = lambda:InstaDNNEstimatorSybilRankerFactory.train_input_fn(
                self.X, self.Y, batch_size),
                    steps=train_steps)

    def validate(self):
        train_x, train_y, test_x, test_y = \
            InstaDNNEstimatorSybilRankerFactory.load_data(split = True)
        my_feature_columns = []
        for key in train_x.keys():
            my_feature_columns.append(tf.feature_column.numeric_column(key=key))

        # Build 2 hidden layer DNN with 10, 10 units respectively.
        classifier = tf.estimator.DNNClassifier(
            feature_columns=my_feature_columns,
            # Two hidden layers of 10 nodes each.
            hidden_units=[10, 10],
            # The model must choose between 3 classes.
            n_classes=2)

        # Train the Model.
        batch_size = InstaDNNEstimatorSybilRankerFactory.batchSize
        train_steps = InstaDNNEstimatorSybilRankerFactory.trainSteps
        classifier.train(
            input_fn=lambda:InstaDNNEstimatorSybilRankerFactory.train_input_fn(
                train_x, train_y,
                batch_size),
            steps=train_steps)

        # Evaluate the model.
        eval_result = classifier.evaluate(
            input_fn=lambda:\
                InstaDNNEstimatorSybilRankerFactory.eval_input_fn(test_x, test_y,
                                                    batch_size))

        print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # def getRank(self, nodeName):
    #     args = dict(
    #             username = nodeName,
    #             usernames = [],
    #             login_user= SybilRanking.settings.insta_username,
    #             login_pass= SybilRanking.settings.insta_password)
    #
    #     scraper = InstagramScraper(**args)
    #     scraper.login()
    #     userData = scraper.scrapeUser( username = nodeName)



    @staticmethod
    def train_input_fn(features, labels, batch_size):
        """An input function for training"""
        # Convert the inputs to a Dataset.
        dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

        # Shuffle, repeat, and batch the examples.
        dataset = dataset.shuffle(1000).repeat().batch(batch_size)

        # Return the dataset.
        return dataset

    @staticmethod
    def eval_input_fn(features, labels, batch_size):
        """An input function for evaluation or prediction"""
        features=dict(features)
        if labels is None:
            # No labels, use only features.
            inputs = features
        else:
            inputs = (features, labels)

        # Convert the inputs to a Dataset.
        dataset = tf.data.Dataset.from_tensor_slices(inputs)

        # Batch the examples
        assert batch_size is not None, "batch_size must not be None"
        dataset = dataset.batch(batch_size)

        # Return the dataset.
        return dataset


    @staticmethod
    def load_data(y_name='bot', split = False, test_size=.10, random_state=42):
        """
        Returns the dataset
                as (train_x, train_y), (test_x, test_y).
            OR
                as (X, Y).
        """
        data = pd.read_csv(
            InstaDNNEstimatorSybilRankerFactory.trainDataFilename,
            sep=",", encoding='latin1')
        data = data.drop(['timestamp', 'username', 'user_id'], 1)
        X = data.drop('bot', 1)
        Y = data['bot']
        if split:
            train_x, test_x, train_y, test_y = train_test_split(
                                X, Y,
                                test_size = test_size,
                                random_state = random_state)
            return train_x, train_y, test_x, test_y
        else:
            return (X, Y)
