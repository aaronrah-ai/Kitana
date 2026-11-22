# Kitana

# Discrete Geometric Scaling & Factorial Convergence Engine

A Python mathematics and machine learning prototype engine built on discrete summation boundaries, Golden Ratio (\(\phi\)) right-triangle geometry, and factorial-bounded hypercube convergence. 

Designed as an alternative to continuous differential calculus, this repository models non-linear scaling, acoustic/kinematic ratios, and radial classification using high-precision discrete arithmetic steps.

---

## 📐 Core Mathematical Architecture

This framework replaces continuous limits (\(dx \to 0\)) with three core discrete engines:

1. **Discrete Summation Ladder (`discrete_ladder_engine.py`)**
   * Redefines polynomial growth (\(x^n\)) as an escalating discrete summation loop bounded by \(x^{n-1}\):
     \[\sum_{k=1}^{x^{n-1}} x = x^n\]
   * Supports linear, square ("\(x\) sum \(x\), \(x\) times"), and Fibonacci sequence step-packet generation using 28-digit `Decimal` precision.

2. **Pythagoras–\(\phi\) Geometric Scaling (`consolidated_pages.py`)**
   * Maps right-triangle hypotenuse ratios (\(\sqrt{1.25}\) and \(\frac{\sqrt{65/4}}{2} \approx 2.0156\)) to the Golden Ratio (\(\phi = 0.5 + \sqrt{1.25} \approx 1.61803\)) and Kepler triangle identities (\(1 + \phi = \phi^2\)).
   * Resolves trigonometric domain constraints (\(\tan^{-1}\) vs. \(\cos^{-1}\)) and links radial ratios to logarithmic order-of-magnitude scaling.

3. **Simulated Cube & Factorial Container (`simulated_cube_container.py`)**
   * Models radial expansion \((x - a)^n\) around an anchor point \(a\) across \(n\) dimensions, using matching factorials (\(n!\)) as structural containers to dampen explosive growth and force convergence:
     \[S_n = \frac{(x - a)^n}{n!}\]

---

## 🧠 Machine Learning Applications

The discrete kernels in this repository can be deployed directly into custom ML pipelines:

* **Factorial Radial Classifier:** Uses `simulated_cube_container` logic as a radial basis function (RBF) kernel to classify data points by measuring tightest factorial shell convergence around learned class centers—naturally suppressing outliers without manual normalization.
* **Discrete Polynomial Feature Generator:** Expands flat tabular inputs into non-linear, integer-stepped feature matrices via `discrete_summation_mapping` (`square` and `fibonacci` modes) for transparent regression modeling.
* **\(\phi\)-Harmonic Activation & Scaling:** Applies Golden Ratio triangle proportions and trigonometric phase conversions to periodic, acoustic, and biomechanical datasets.

---

## 🚀 Quickstart & Usage

### Prerequisites
* Python 3.8+ (uses standard library `math` and `decimal` modules—no external dependencies required for the core engines).

### Running the Engines

```bash
# 1. Run the Discrete Summation & Escalating Ladder Engine
python discrete_ladder_engine.py

# 2. Run the Consolidated Pythagoras-Phi & Kepler Triangle Solver
python consolidated_pages.py

# 3. Run the Simulated Cube & Factorial Convergence Engine
python simulated_cube_container.py
```

### Example: Factorial Radial Classifier

```python
from factorial_classifier import FactorialRadialClassifier

X_train = [1.8, 2.0, 2.2, 7.5, 7.7, 8.0]
y_train = ["Low_State", "Low_State", "Low_State", "High_State", "High_State", "High_State"]

model = FactorialRadialClassifier(max_dimension=8)
model.fit(X_train, y_train)

predictions = model.predict([2.015, 7.70])
print(predictions)  # Output: ['Low_State', 'High_State']
```

---

## 📂 Repository Structure

```text
├── discrete_ladder_engine.py      # Discrete summation mapping & x^(n-1) boundary loops
├── consolidated_pages.py          # Pythagoras-Phi geometry, Kepler triangle & trig solver
├── simulated_cube_container.py    # Radial (x - a)^n / n! convergence engine
├── factorial_classifier.py        # Supervised ML classifier built on factorial shells
└── README.md                      # Documentation & mathematical overview
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
