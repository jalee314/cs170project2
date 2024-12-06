from classifier import NN
from validator import Validator

def import_data(file_path):                         #https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python 
    data = []   
    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(float, line.split()))
            data.append(row)
    return data

small = 'small-test-dataset.txt'
large = 'large-test-dataset.txt'

small_data = import_data(small)
large_data = import_data(large)

classifier = NN()
validator = Validator(classifier)


print("Jason Lee Project Part 2:\n")

choice = int(input("1 for small dataset\n2 for large dataset\n\nChoice: "))

if choice == 1:
    choice = int(input("1 to use all features\n2 to use features {3,5,7}\n\nChoice: "))
    
    if choice == 1:
        features = list(range(1, 11))
        validator.leave_one_out(small_data, features)
    
    elif choice == 2:
        features = [3,5,7]
        validator.leave_one_out(small_data, features)

    else:
        print("Invalid Value")
        quit()

elif choice == 2:
    choice = int(input("1 to use all features\n2 to use features {3,5,7}\n\nChoice: "))
    
    if choice == 1:
        features = list(range(1, 41))
        validator.leave_one_out(large_data, features)
    
    elif choice == 2:
        features = [1,15,27]
        validator.leave_one_out(large_data, features)
    else:
        print("Invalid Value")
        quit()