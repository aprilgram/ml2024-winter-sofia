import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the value of k: "))
    
    if k > N:
        print("Error: k should be less than or equal to N.")
        return
    
    X = np.zeros(N)
    Y = np.zeros(N)
    
    print("Enter the values for (x, y) points:")
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        X[i] = x
        Y[i] = y
    
    variance = np.var(Y)
    print(f"Variance of labels in the training dataset: {variance:.2f}")

    x_pred = float(input("Enter the value of X for prediction: "))
    
    X = X.reshape(-1, 1)
    
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X, Y)
    
    y_pred = knn_regressor.predict([[x_pred]])
    
    print(f"Result of k-NN Regression for input X: {y_pred[0]:.2f}")

if __name__ == "__main__":
    main()
