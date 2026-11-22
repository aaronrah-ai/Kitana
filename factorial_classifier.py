import math
from decimal import Decimal, getcontext

getcontext().prec = 28

class FactorialRadialClassifier:
    """
    A custom Machine Learning classifier using your simulated cube 
    and factorial container logic (File 3) to classify data points.
    """
    def __init__(self, max_dimension=6):
        self.max_dimension = max_dimension
        self.class_centers = {}

    def _compute_convergence_score(self, x_val, center_val):
        x = Decimal(str(x_val))
        a = Decimal(str(center_val))
        radial_distance = abs(x - a)
        
        total_shell_sum = Decimal('0')
        for n in range(1, self.max_dimension + 1):
            raw_cube = radial_distance ** n
            factorial_container = Decimal(math.factorial(n))
            total_shell_sum += raw_cube / factorial_container
            
        return total_shell_sum

    def fit(self, X_train, y_train):
        """Learns the center anchor 'a' for each class label."""
        grouped = {}
        for x, label in zip(X_train, y_train):
            grouped.setdefault(label, []).append(x)
        
        for label, values in grouped.items():
            self.class_centers[label] = sum(values) / len(values)

    def predict(self, X_test):
        """Classifies new points based on tightest factorial shell convergence."""
        predictions = []
        for x in X_test:
            best_label = None
            lowest_expansion = None
            
            for label, center in self.class_centers.items():
                score = self._compute_convergence_score(x, center)
                if lowest_expansion is None or score < lowest_expansion:
                    lowest_expansion = score
                    best_label = label
            predictions.append(best_label)
        return predictions

if __name__ == "__main__":
    # Example Training Data (e.g., classifying low vs. high velocity/load states)
    X_train = [1.8, 2.0, 2.2, 7.5, 7.7, 8.0]
    y_train = ["Low_State", "Low_State", "Low_State", "High_State", "High_State", "High_State"]

    model = FactorialRadialClassifier(max_dimension=8)
    model.fit(X_train, y_train)

    test_samples = [2.015, 7.70]  # Testing your exact half-hypotenuse and final n values
    results = model.predict(test_samples)
    
    for sample, pred in zip(test_samples, results):
        print(f"Input: {sample} -> Predicted Class: {pred}")
