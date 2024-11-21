import math
import random

class Problem:

    def __init__(self, algo_choice, num_features):
        self.algo_choice = algo_choice
        self.num_features = num_features
        self.accuracy_dict = {}

    def algorithm(self):
        if self.algo_choice == 1:                                                                                        #forward selection
            features = set(range(1, self.num_features + 1))                                                              #add a set thats essentially just an enumerated list of featuers
            explored_features = set()
            best_subset = set()
            max_accuracy = -1

            no_feature_accuracy = self.evaluation_function(0)                                                           #evaluate default rate 
            max_accuracy = no_feature_accuracy

            print(f"Using no features and \"random\" evaluation, I get an accuracy of {no_feature_accuracy:.2f}%\n")

            while len(explored_features) < self.num_features:                                                           #will keep looping until all features are searched/break is called 
                best_feature = None                                                                                     
                for feature in features - explored_features:                                                            # {1,2,3,4} - {2,3} = {1,4}
                    if feature not in explored_features:                                                                
                        curr_set = explored_features | {feature}                                                        # {2,3} -> {1,2,3}, {2,3,4} (logic explores all subsets throughout all iterations)
                        accuracy = self.evaluation_function(len(curr_set), tuple(curr_set))
                        print(f"\tUsing feature(s) {curr_set} accuracy is {accuracy:.2f}%")
                        if accuracy > max_accuracy:
                            max_accuracy = accuracy
                            best_feature = feature 
                            best_subset = curr_set
                        elif accuracy < max_accuracy:
                            print("Warning, Accuracy has decreased!")
                if best_feature is not None:
                    explored_features.add(best_feature)
                    print(f"Feature set {best_subset} was best, accuracy is {max_accuracy:.2f}%\n")
                else:
                    break                                                                                                 #if no improvement found then we have found the local optimum, break out of search

            if len(best_subset) == 0:
                print(f"Finished search!! The best feature subset is nothing, which has an accuracy of {max_accuracy:.2f}%\n")
            else:
                print(f"Finished search!! The best feature subset is {best_subset}, which has an accuracy of {max_accuracy:.2f}%\n")

            
                

    def evaluation_function(self, num_features, subset=None):                                                             #for number of features we generate, generate a random probability to each
        if num_features == 0:
            subset = tuple()                                                                                              #edge case for empty set
        if subset not in self.accuracy_dict:
            accuracy = random.uniform(.2, 1) * 100                                                                        #don't really want to deal with accuracies in like the 0.89% range
            self.accuracy_dict[subset] = accuracy
        return self.accuracy_dict[subset]


