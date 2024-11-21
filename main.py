from search import Problem

def main():
    print("Welcome to Jason Lee's Feature Selection Algorithm.\n\n")

    num_features = int(input("Please enter total number of features: ")) 

    if(num_features < 1):
        print("Choose a value greater than 0")
        quit()   

    algo = int(input("Type the number of the algorithm you want to run.\n\n\t1) Forward Selection\n\t2) Backward Elimination\n\n"))

    if algo > 2 or algo < 1:
        print("Invalid\n")
        quit()

    problem = Problem(algo, num_features)
    problem.algorithm()

if __name__ == "__main__":
    main()
