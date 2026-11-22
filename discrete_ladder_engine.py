from decimal import Decimal, getcontext

getcontext().prec = 28

def discrete_summation_mapping(x, mode="linear"):
    """
    Computes f(x) = sum_{k=1}^{x} g(k) where the upper limit n = x.
    Supports 'linear' (g(k)=k), 'square' (g(k)=x), or 'fibonacci' scaling functions.
    """
    x_int = int(x)
    accumulated_sum = Decimal('0')

    if mode == "linear":
        for k in range(1, x_int + 1):
            accumulated_sum += Decimal(k)
    elif mode == "square":
        # Tier 1 & 2: "x sum x, x times" -> x^2
        for _ in range(1, x_int + 1):
            accumulated_sum += Decimal(str(x))
    elif mode == "fibonacci":
        a, b = Decimal('1'), Decimal('1')
        for _ in range(1, x_int + 1):
            accumulated_sum += a
            a, b = b, a + b

    return accumulated_sum

def discrete_ladder_engine(x_val, n_level):
    """
    Executes the escalating scaling level: Sum_{k=1}^{x^(n-1)} x = x^n
    Stacks the base component x iteratively up to the upper boundary x^(n-1).
    """
    x = int(x_val)
    if n_level < 1:
        raise ValueError("Operational level n must be >= 1")

    upper_boundary = x ** (n_level - 1)
    total_value = 0

    # Discrete summation loop adding x to itself x^(n-1) times
    for _ in range(upper_boundary):
        total_value += x

    return upper_boundary, total_value

if __name__ == "__main__":
    x_input = 4
    n_input = 3

    print(f"--- Discrete Geometric Scaling Framework (x={x_input}, n={n_input}) ---")
    
    # 1. Standard discrete summation f(x) where n = x
    sq_sum = discrete_summation_mapping(x_input, mode="square")
    fib_sum = discrete_summation_mapping(x_input, mode="fibonacci")
    print(f"Tier 2 ('x sum x, x times'): {sq_sum}")
    print(f"Discrete Fibonacci Summation (n=x={x_input}): {fib_sum}")

    # 2. Escalating discrete ladder: Sum_{k=1}^{x^(n-1)} x
    boundary, collapsed_val = discrete_ladder_engine(x_input, n_input)
    print(f"Tier 3 Upper Boundary (x^(n-1)): {boundary} iterations")
    print(f"Tier 3 Collapsed Value (x^n): {collapsed_val}")
