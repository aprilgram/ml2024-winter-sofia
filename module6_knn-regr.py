import numpy as np

class NumberStore:
    def __init__(self):
        self.x_train = None
        self.y_train = None

    def read(self, n):
        self.x_train = np.zeros(n)
        self.y_train = np.zeros(n)
        for i in range(n):
            x = float(input(f"Enter x_{i+1}: "))
            y = float(input(f"Enter y_{i+1}: "))
            self.x_train[i] = x
            self.y_train[i] = y

if __name__ == "__main__":
    numbers = NumberStore()
    n = int(input("Enter N: "))
    k = int(input("Enter k: "))
    numbers.read(n) 
    x = float(input("Enter x: "))
    if k > n:
        print("Error: k > N")
    elif k <= 0:
        print("Error: k <= 0")
    else:
        distances = np.sqrt(np.sum((numbers.x_train.reshape(-1, 1) - np.array([x]))**2, axis=1))
        sorted_idxs = np.argsort(distances)
        nn_idxs = sorted_idxs[:k]
        y_pred = np.mean(numbers.y_train[nn_idxs])
        print("Y=", y_pred)
