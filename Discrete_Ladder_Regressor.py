from decimal import Decimal, getcontext

getcontext().prec = 28

class DiscreteLadderRegressor:
    """
    Supervised ML Regressor powered by File 1's Discrete Summation Mapping
    and Escalating Ladder Engine (Sum_{k=1}^{x^(n-1)} x = x^n).
    """
    def __init__(self, max_level=3, regularization=1e-4):
        self.max_level = max_level
        self.regularization = regularization
        self.weights = []

    def _discrete_summation_features(self, x_val):
        """Generates discrete step-packet features for a single input x."""
        x_int = max(1, int(round(abs(x_val))))
        
        # 1. Linear Summation: sum_{k=1}^x k
        linear_sum = sum(Decimal(k) for k in range(1, x_int + 1))
        
        # 2. Square Summation: "x sum x, x times" -> x^2
        square_sum = sum(Decimal(str(x_int)) for _ in range(1, x_int + 1))
        
        # 3. Fibonacci Summation: sum of first x Fibonacci steps
        fib_sum = Decimal('0')
        a, b = Decimal('1'), Decimal('1')
        for _ in range(1, x_int + 1):
            fib_sum += a
            a, b = b, a + b

        # 4. Escalating Ladder Level: Sum_{k=1}^{x^(n-1)} x
        # Capped boundary to keep execution fast for larger integers
        safe_x = min(x_int, 12)
        upper_boundary = safe_x ** (self.max_level - 1)
        ladder_val = sum(safe_x for _ in range(upper_boundary))

        return [
            1.0,  # Bias intercept
            float(x_val),
            float(linear_sum),
            float(square_sum),
            float(fib_sum),
            float(ladder_val)
        ]

    def _solve_linear_system(self, A, b):
        """Solves A * w = b using Gaussian elimination."""
        n = len(b)
        M = [row[:] + [b[i]] for i, row in enumerate(A)]

        for col in range(n):
            pivot = max(range(col, n), key=lambda r: abs(M[r][col]))
            M[col], M[pivot] = M[pivot], M[col]
            for row in range(col + 1, n):
                factor = M[row][col] / M[col][col]
                for c in range(col, n + 1):
                    M[row][c] -= factor * M[col][c]

        w = [0.0] * n
        for i in range(n - 1, -1, -1):
            s = sum(M[i][j] * w[j] for j in range(i + 1, n))
            w[i] = (M[i][n] - s) / M[i][i]
        return w

    def fit(self, X_train, y_train):
        """Builds the discrete feature matrix and learns optimal ladder weights."""
        Phi_matrix = [self._discrete_summation_features(x) for x in X_train]
        num_features = len(Phi_matrix[0])

        # Compute normal equations: (Phi^T * Phi + lambda*I) * w = Phi^T * y
        ATA = [[0.0] * num_features for _ in range(num_features)]
        ATy = [0.0] * num_features

        for row, y in zip(Phi_matrix, y_train):
            for i in range(num_features):
                ATy[i] += row[i] * y
                for j in range(num_features):
                    ATA[i][j] += row[i] * row[j]

        for i in range(num_features):
            ATA[i][i] += self.regularization

        self.weights = self._solve_linear_system(ATA, ATy)

    def predict(self, X_test):
        """Predicts continuous target values using learned discrete weights."""
        predictions = []
        for x in X_test:
            features = self._discrete_summation_features(x)
            pred = sum(w * f for w, f in zip(self.weights, features))
            predictions.append(pred)
        return predictions


if __name__ == "__main__":
    # Example: Predicting non-linear load/output scaling from integer steps
    X_train = [1, 2, 3, 4, 5, 6]
    y_train = [2.5, 11.0, 34.5, 82.0, 165.5, 298.0]

    model = DiscreteLadderRegressor(max_level=3)
    model.fit(X_train, y_train)

    test_inputs = [4, 7]
    preds = model.predict(test_inputs)
    for x, y_hat in zip(test_inputs, preds):
        print(f"Input x={x} -> Predicted Output: {y_hat:.2f}")
