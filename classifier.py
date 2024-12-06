import math


class NN:
    def __init__(self):
        self.features = None
        self.labels = None
        self.min_max = None

    def train(self, training_data):
        features = [row[1:] for row in training_data]
        self.labels = [row[0] for row in training_data]
        self.features, self.min_max = self.normalize(features)


    def test(self, test_instance):
        distances = []

        normalized_test = []

        for i in range(len(test_instance)):
            test_val = test_instance[i]
            min_val = self.min_max[i][0]
            max_val = self.min_max[i][1]
            denom = max_val - min_val

            if denom == 0:
                normalized_val = 0
            else:
                normalized_val = (test_val - min_val)/denom

            normalized_test.append(normalized_val)

        for i, train_instance in enumerate(self.features):
            dist = self.euclidean(normalized_test, train_instance)
            distances.append((dist, self.labels[i]))  

        nn = min(distances, key=lambda x: x[0])
        return nn[1]  
    

    def euclidean(self, a, b):
        differences = []
        for i in range(len(a)):
            differences.append((a[i]-b[i])**2)

        return math.sqrt(sum(differences))

    def normalize(self, features):
        n = len(features[0])

        normalized_features = []
        min_max = []

        for i in range(n):
            col = [row[i] for row in features]
            col_min, col_max = min(col), max(col)
            min_max.append((col_min, col_max))
            
            denom = col_max - col_min

            if denom == 0:
                normalized_col = [0.0 for _ in col]
            else:
                normalized_col = [(value - col_min)/denom for value in col]

            for j, value in enumerate(normalized_col):
                if len(normalized_features) <= j:
                    normalized_features.append([]) 
                normalized_features[j].append(value)

        return normalized_features, min_max