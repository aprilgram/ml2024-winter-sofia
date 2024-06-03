import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    N = int(input("Enter N: "))

    train_X = []
    train_Y = []
    for _ in range(N):
        x = float(input("Enter x: "))
        y = int(input("Enter y: "))
        train_X.append([x])
        train_Y.append(y)

    train_X = np.array(train_X)
    train_Y = np.array(train_Y)

    M = int(input("Enter M: "))

    test_X = []
    test_Y = []
    for _ in range(M):
        x = float(input("Enter x: "))
        y = int(input("Enter y: "))
        test_X.append([x])
        test_Y.append(y)

    test_X = np.array(test_X)
    test_Y = np.array(test_Y)

    best_k = 1
    best_accuracy = 0.0

    for k in range(1, 11):
        if k > N:
            continue
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(train_X, train_Y)
        predictions = knn.predict(test_X)
        accuracy = accuracy_score(test_Y, predictions)
        print(f"k={k}, Accuracy={accuracy}")

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k

    print(f"Best k:{best_k}, Test accuracy: {best_accuracy:.4f}")

if __name__ == "__main__":
    main()
