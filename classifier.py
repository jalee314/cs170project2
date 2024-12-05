import math


class KNN:
    def __init__(self):
        self.features = None
        self.labels = None

    def train(self, training_data):
        features = [row[1:] for row in training_data]
        self.labels = [row[0] for row in training_data]
        self.features = self.normalize(features)


    def test(self, test_instance):
        pass
    

    def euclidean(self, a, b):
       pass

    def normalize(self, a, b):
        pass