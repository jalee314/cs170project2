import math
import random

class Problem:

    def __init__(self, algo_choice, num_features):
        self.algo_choice = algo_choice
        self.num_features = num_features

    def algorithm(self, features):
        if self.algo_choice == 1:                           #forward selection
        
            explored_features = set()
            max_accuracy = -1

            for feature in features:
                if feature in explored_features:
                    continue
                

        else:
            explored_features = set()                       #backward elimination
                

    def evaluation_function(self):                          #for number of features we generate, generate a random probability to each feature
        feature_list = []
        for feature in range(self.num_features):
            feature_list.append(random.random())
        return feature_list

