import math
import random

class Problem:

    def __init__(self, algo_choice, num_features):
        self.algo_choice = algo_choice
        self.num_features = num_features
        self.accuracy_dict = {}

    def algorithm(self):
        if self.algo_choice == 1:                                               #forward selection

            explored_features = set()
            best_subset = set()
            max_accuracy = -1

            no_feature_accuracy = self.evaluation_function(0)
            max_accuracy = no_feature_accuracy

            print(f"Using no features and \"random\" evaluation, I get an accuracy of{no_feature_accuracy:.2f}%\n")

            
                

    def evaluation_function(self, num_features, subset=None):                   #for number of features we generate, generate a random probability to each
        if subset is None:
            subset = tuple()                                                    #base case for empty set
        if subset not in self.accuracy_dict:
            accuracy = random.random() * 100
            self.accuracy_dict[subset] = accuracy
        return self.accuracy_dict[num_features]


