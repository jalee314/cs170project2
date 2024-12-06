import time

class Validator:
    
    def __init__(self, classifier):
        self.classifier = classifier

    def leave_one_out(self, dataset, feature_subset):
        correct = 0
        total = len(dataset)                            #metrics for accuracy

        validaiton_start = time.time()
        

        for i in range(total):
            iteration_start = time.time()
            test = dataset[i]                           #for every data point, take one out for testing and use the other for training
            training = dataset[:i] + dataset[i+1:]

            test_features = [test[j] for j in feature_subset]                          #extract all the test features for all instances
            subset_training = [[row[0]] + [row[j] for j in feature_subset] for row in training]                 #extract the labels and selected features for the instances    

            train_start = time.time()
            self.classifier.train(subset_training)      #train the classifier with the training instances
            train_end = time.time()

            test_start = time.time()
            pred_label = self.classifier.test(test_features)        #test the testing instance
            test_end = time.time()

            actual_label = test[0]  

            if pred_label == actual_label:                          #compare with actual label and increment correct if result was true
                correct +=1
            iteration_end = time.time()

            print(f"Instance {i+1}/{total}")                                                    #trace logic
            print(f"  Train Time: {train_end - train_start:.4f} seconds")
            print(f"  Test Time: {test_end - test_start:.4f} seconds")
            print(f"  Total Step Time: {iteration_end - iteration_start:.4f} seconds")
            print(f"  Predicted: {pred_label}, Actual: {actual_label}\n")
            
        print(f"\nResults: {correct} / {total}")
        print(f"Accuracy: {correct/total * 100:.2f}%")
        

