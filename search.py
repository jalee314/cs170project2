import random
from validator import Validator
from classifier import NN

class Problem:

    def __init__(self, algo_choice, num_features, dataset):
        self.algo_choice = algo_choice
        self.num_features = num_features
        self.accuracy_dict = {}
        self.dataset = dataset
        self.validator = Validator(NN())                                                                                                    
        

    def algorithm(self):
        if self.algo_choice == 1:                                                                                                            #forward selection
            features = set(range(1, self.num_features + 1))                                                                                  #add a set thats essentially just an enumerated list of featuers
            explored_features = set()                       
            best_subset = set()
            global_accuracy = -1                                                                                                             #changed to global and local accuracy since I'm not stopping my search anymore
            

            no_feature_accuracy = self.evaluation_function(0)                                                                                #evaluate default rate 
            global_accuracy = no_feature_accuracy
            print("\nForward Selection:")

            print(f"\nUsing no features and \"random\" evaluation, I get an accuracy of {global_accuracy:.2f}%\n")

            while len(explored_features) < self.num_features:                                                                                #will keep looping until all features are searched/break is called 
                feature_to_add = None                                                                                   
                local_accuracy = 0 
                local_max_set = set()

                for feature in features - explored_features:                                                                                 # {1,2,3,4} - {2,3} = {1,4}                                                             
                        curr_set = explored_features | {feature}                                                                             # {2,3} -> {1,2,3}, {2,3,4} (logic explores all subsets throughout all iterations)
                        accuracy = self.evaluation_function(len(curr_set), tuple(curr_set))
                        print(f"\tUsing feature(s) {curr_set} accuracy is {accuracy:.2f}%")
                        
                        if accuracy > local_accuracy:
                            local_accuracy = accuracy
                            feature_to_add = feature
                            local_max_set = curr_set.copy()
                
                if feature_to_add is not None:
                    explored_features.add(feature_to_add)
                    
                    if local_accuracy > global_accuracy:                                                                                    # new global maxima found
                        global_accuracy = local_accuracy
                        best_subset = explored_features.copy()
                        print(f"\nFeature set {best_subset} was best, accuracy is {global_accuracy:.2f}%\n")
                    else:
                        print(f"\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)\nFeature set {local_max_set} was best, accuracy is {local_accuracy:.2f}%\n")
                                                                                                                                            

            if len(best_subset) == 0:
                print(f"\nFinished search!! The best feature subset is nothing, which has an accuracy of {global_accuracy:.2f}%\n")
            else:
                print(f"\nFinished search!! The best feature subset is {best_subset}, which has an accuracy of {global_accuracy:.2f}%\n")

        else:                                                                                                                               #backward elimination 
            features = set(range(1, self.num_features + 1))
            best_subset = features.copy()
            global_accuracy = -1
            local_max_set = features.copy()

            all_feature_accuracy = self.evaluation_function(len(best_subset), tuple(best_subset))
            global_accuracy = all_feature_accuracy
            
            print("\nBackward Elimination:")
            print(f"\nUsing all features {best_subset} and leave one out validation, I get an accuracy of {global_accuracy:.2f}%\n")

            while len(features) > 0:
                worst_feature = None
                local_accuracy = -1
                
                for feature in features:
                    curr_set = features - {feature}                                                                                         #{1,2,3,4} -> {2,3,4}, {1,3,4}, {1,2,3}
                    accuracy = self.evaluation_function(len(curr_set), tuple(curr_set))
                    if len(curr_set) > 0:
                        print(f"\tUsing feature(s) {curr_set} accuracy is {accuracy:.2f}%")
                    else:
                        print(f"\tUsing no features, accuracy is {accuracy:.2f}%")

                    if accuracy > local_accuracy:                                                                                           #check for new local maxima
                        local_accuracy = accuracy
                        worst_feature = feature 
                        local_max_set = curr_set
                    
                    if accuracy > global_accuracy:                                                                                         #then check for global maxima                                     
                        global_accuracy = accuracy  
                        best_subset = curr_set

                if worst_feature is not None:                                                                                                       
                    features.remove(worst_feature)                                                                                          #continue search from subsets without that featture
                    print(f"\nFeature set {local_max_set} was best, accuracy is {local_accuracy:.2f}%\n")
                else:
                    print("\nWarning, Accuracy has decreased in all possible subsets when removing feature!\n")
                
            if len(best_subset) == 0:
                print(f"\nFinished search!! The best feature subset is nothing, which has an accuracy of {global_accuracy:.2f}%\n")
            else:
                print(f"\nFinished search!! The best feature subset is {best_subset}, which has an accuracy of {global_accuracy:.2f}%\n")

    def evaluation_function(self, num_features, subset=None):                                                                              
        if num_features == 0:
            subset = tuple()
            accuracy = 50.0                                                                                                                 #just set default rate to 50                           
            self.accuracy_dict[subset] = accuracy                                                                                           
            return self.accuracy_dict[subset]                                                                                               #edge case for empty set
        
        if subset not in self.accuracy_dict:
            feature_subset = list(subset)                                                                                     
            accuracy = self.validator.leave_one_out(self.dataset, feature_subset) * 100                                                     #actually have value returned vfrom validation
            self.accuracy_dict[subset] = accuracy
            return self.accuracy_dict[subset]


