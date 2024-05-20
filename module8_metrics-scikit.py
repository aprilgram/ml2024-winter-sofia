import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of points (N): "))
    
    ground_truth = np.zeros(N, dtype=int)
    predictions = np.zeros(N, dtype=int)
    
    for i in range(N):
        x = int(input(f"Enter ground truth (x) for point {i+1}: "))
        y = int(input(f"Enter predicted class (y) for point {i+1}: "))
        ground_truth[i] = x
        predictions[i] = y
    
    precision = precision_score(ground_truth, predictions)
    recall = recall_score(ground_truth, predictions)
    
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
