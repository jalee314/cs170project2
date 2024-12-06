import math


class NN:
    def __init__(self):
        self.features = None
        self.labels = None
        self.min_max = None                                                     #save min_max from training to use in test

    def train(self, training_data):
        features = [row[1:] for row in training_data]                           
        self.labels = [row[0] for row in training_data]
        self.features, self.min_max = self.normalize(features)


    def test(self, test_instance):
        distances = []

        normalized_test = []

        normalized_test, _ = self.normalize([test_instance], self.min_max)      
        normalized_test = normalized_test[0]                                #set equal to first row of features

    
        for i, train_instance in enumerate(self.features):
            dist = self.euclidean(normalized_test, train_instance)
            distances.append((dist, self.labels[i]))                        #calculate and store distances

            for i, train_instance in enumerate(self.features):
                dist = self.euclidean(normalized_test, train_instance)
                distances.append((dist, self.labels[i]))  

            nn = min(distances, key=lambda x: x[0])                         #assign nearest neighbor to point with the minimum distance from it
            return nn[1]  
        

    def euclidean(self, a, b):
        differences = []
        for i in range(len(a)):
            differences.append((a[i]-b[i])**2)

        return math.sqrt(sum(differences))

    def normalize(self, features, min_max=None):
        n = len(features[0])
        normalized_features = []

        if min_max is None:                                 #calculate min max based on training features
            min_max = []
            for i in range(n):
                col = [row[i] for row in features]
                col_min, col_max = min(col), max(col)
                min_max.append((col_min, col_max))

        for i in range(n):                                  
            col = [row[i] for row in features]
            col_min, col_max = min_max[i]
            denom = col_max - col_min

            if denom == 0:
                normalized_col = [0.0 for _ in col]
            else:
                normalized_col = [(value - col_min) / denom for value in col]

            for j, value in enumerate(normalized_col):
                if len(normalized_features) <= j:               
                    normalized_features.append([])          #create a new row if no space exists
                normalized_features[j].append(value)

        return normalized_features, min_max