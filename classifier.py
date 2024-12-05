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

    def normalize(self, features):
        n = len(features[0])

        normalized_features = []

        for i in range(n):
            col = [row[i] for row in features]
            col_min, col_max = min(col), max(col)
            
            denom = col_max - col_min

            if denom == 0:
                normalized_col = [0.0 for _ in col]
            else:
                normalized_col = [(value - col_min)/denom for value in col]

            for j, value in enumerate(normalized_col):
                if len(normalized_features) <= j:
                    normalized_features.append([]) 
                normalized_features[j].append(value)

        return normalized_features