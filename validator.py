class Validator:
    
    def __init__(self, classifier):
        self.classifier = classifier

    def leave_one_out(self, dataset, feature_subset):
        correct = 0
        total = len(dataset)                            #metrics for accuracy

        for i in range(total):
            test = dataset[i]                           #for every data point, take one out for testing and use the other for training
            training = dataset[:i] + dataset[i+1:]

            test_features = [test[j] for j in feature_subset]                          #extract all the test features for all instances
            subset_training = [[row[0]] + [row[j] for j in feature_subset] for row in training]                 #extract the labels and selected features for the instances    

            self.classifier.train(subset_training)      #train the classifier with the training instances

            pred_label = self.classifier.test(test_features)        #test the testing instance
            actual_label = test[0]  

            if pred_label == actual_label:                          #compare with actual label and increment correct if result was true
                correct +=1
        return correct/total
        

