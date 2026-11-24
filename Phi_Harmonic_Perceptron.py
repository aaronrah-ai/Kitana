import math

class PhiHarmonicPerceptron:
    """
    Custom Neural Perceptron powered by File 2's Pythagoras-Phi Geometry,
    Kepler Triangle Scaling, and Inverse Tangent/Cosine Phase Mapping.
    """
    def __init__(self, learning_rate=0.05, epochs=150):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0.0

        # Core Geometric Constants from File 2
        self.phi = 0.5 + math.sqrt(1.25)                 # ≈ 1.618034
        self.phi_sq = self.phi ** 2                      # ≈ 2.618034
        self.half_hyp2 = math.sqrt(65.0 / 4.0) / 2.0     # ≈ 2.015564
        self.kepler_scale = self.phi_sq / (4.5 * self.half_hyp2)  # ≈ 0.288644

    def _phi_harmonic_activation(self, z):
        """
        Maps raw weighted sum 'z' through File 2's trigonometric and
        Kepler-Phi scaling ratios to output a probability in [0, 1].
        """
        # Scale input by Kepler constant and extract tangent phase angle
        scaled_signal = z * self.kepler_scale * self.half_hyp2
        theta_rad = math.atan(scaled_signal)  # Bounded cleanly in (-pi/2, pi/2)
        
        # Apply Golden Ratio harmonic wave modulation
        harmonic_response = math.sin(theta_rad * self.phi)
        
        # Normalize response from [-1, 1] into [0, 1] probability space
        return 0.5 * (harmonic_response + 1.0)

    def fit(self, X_train, y_train):
        """Trains the Phi-Harmonic Perceptron via gradient updates."""
        num_features = len(X_train[0])
        self.weights = [0.1] * num_features
        self.bias = 0.0

        for _ in range(self.epochs):
            for features, target in zip(X_train, y_train):
                z = sum(w * x for w, x in zip(self.weights, features)) + self.bias
                pred = self._phi_harmonic_activation(z)
                error = target - pred

                # Update weights scaled by the Golden Ratio step
                for i in range(num_features):
                    self.weights[i] += self.learning_rate * error * features[i]
                self.bias += self.learning_rate * error

    def predict_proba(self, X_test):
        """Returns continuous Phi-harmonic activation scores."""
        probs = []
        for features in X_test:
            z = sum(w * x for w, x in zip(self.weights, features)) + self.bias
            probs.append(self._phi_harmonic_activation(z))
        return probs

    def predict(self, X_test, threshold=0.5):
        """Returns binary class predictions (0 or 1)."""
        return [1 if p >= threshold else 0 for p in self.predict_proba(X_test)]


if __name__ == "__main__":
    # Example: Classifying wave/kinematic states [frequency_ratio, amplitude_ratio]
    X_train = [
        [0.5, 1.118],   # Golden triangle legs -> Class 0
        [0.6, 1.200],   # Class 0
        [2.0, 4.500],   # Second triangle ratios -> Class 1
        [2.015, 4.290]  # Scaled convergence state -> Class 1
    ]
    y_train = [0, 0, 1, 1]

    perceptron = PhiHarmonicPerceptron(learning_rate=0.08, epochs=200)
    perceptron.fit(X_train, y_train)

    test_samples = [[0.55, 1.15], [2.02, 4.40]]
    preds = perceptron.predict(test_samples)
    probs = perceptron.predict_proba(test_samples)

    for sample, p, label in zip(test_samples, probs, preds):
        print(f"Input {sample} -> Harmonic Score: {p:.3f} | Predicted Class: {label}")
