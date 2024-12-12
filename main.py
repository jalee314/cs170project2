from search import Problem
import matplotlib.pyplot as plt


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


    elif choice == 2:
        num_features = len(large_data[0]) - 1

        algo = int(input("\nChoose your algorithm:\n1) Forward Selection\n2) Backward Elimination\n"))
        if algo > 2 or algo < 1:
            print("Invalid\n")
            quit()
        problem = Problem(algo, num_features, large_data)
        problem.algorithm()

        

    elif choice == 3:
        num_features = len(titanic_data[0]) - 1

        algo = int(input("\nChoose your algorithm:\n1) Forward Selection\n2) Backward Elimination\n"))
        if algo > 2 or algo < 1:
            print("Invalid\n")
            quit()
        problem = Problem(algo, num_features, titanic_data)
        problem.algorithm()


    else:
        print("Invalid\n")
        quit()

    def plot_scatter(data, feature_x, feature_y, title, save_path=None):                                    #function made with assistance of chatgpt
        
        labels = [row[0] for row in data]  
        x = [row[feature_x] for row in data]
        y = [row[feature_y] for row in data]

          
        plt.figure(figsize=(8, 6))
        for label in set(labels): 
            plt.scatter(
                [x[i] for i in range(len(labels)) if labels[i] == label],
                [y[i] for i in range(len(labels)) if labels[i] == label],
                label=f"Label {int(label)}",
                alpha=0.7
            )
        
        plt.xlabel(f"Feature {feature_x}")
        plt.ylabel(f"Feature {feature_y}")
        plt.title(title)
        plt.legend()
        
        if save_path:
            plt.savefig(save_path)
        plt.show()

    
    plot_scatter(small_data, feature_x=3, feature_y=5, title="Small Dataset: Features 3 and 5")

    plot_scatter(small_data, feature_x=2, feature_y=10, title="Small Dataset: Features 2 and 10")

    plot_scatter(large_data, feature_x=1, feature_y=27, title="Large Dataset: Features 1 and 27")

    plot_scatter(large_data, feature_x=3, feature_y=34, title="Large Dataset: Features 3 and 34")

if __name__ == "__main__":
    main()
