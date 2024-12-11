from search import Problem

def import_data(file_path):                         #https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python 
    data = []   
    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(float, line.split()))
            data.append(row)
    return data

def main():

    small = 'small-test-dataset.txt'
    large = 'large-test-dataset.txt'
    titanic = 'titanic clean.txt'
    small_data = import_data(small)
    large_data = import_data(large)
    titanic_data = import_data(titanic)

    print("Welcome to Jason Lee's Feature Selection Algorithm.\n\n")

    choice = int(input("Choose your dataset: \n1) Small dataset\n2) Large dataset\n3) Titanic dataset\n"))

    if choice == 1:
        num_features = len(small_data[0]) - 1

        algo = int(input("\nChoose your algorithm:\n1) Forward Selection\n2) Backward Elimination\n"))
        if algo > 2 or algo < 1:
            print("Invalid\n")
            quit()
        problem = Problem(algo, num_features, small_data)
        problem.algorithm()

        quit()

    elif choice == 2:
        num_features = len(large_data[0]) - 1

        algo = int(input("\nChoose your algorithm:\n1) Forward Selection\n2) Backward Elimination\n"))
        if algo > 2 or algo < 1:
            print("Invalid\n")
            quit()
        problem = Problem(algo, num_features, large_data)
        problem.algorithm()

        quit()

    elif choice == 3:
        num_features = len(titanic_data[0]) - 1

        algo = int(input("\nChoose your algorithm:\n1) Forward Selection\n2) Backward Elimination\n"))
        if algo > 2 or algo < 1:
            print("Invalid\n")
            quit()
        problem = Problem(algo, num_features, titanic_data)
        problem.algorithm()

        quit()

    else:
        print("Invalid\n")
        quit()

if __name__ == "__main__":
    main()
