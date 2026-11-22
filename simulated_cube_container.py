import math
from decimal import Decimal, getcontext

# Set high precision for exact decimal outputs
getcontext().prec = 28

def simulated_cube_container(x_val, a_val, max_dimension):
    """
    Calculates the raw simulated cube volume (x - a)^n and the 
    factorial-bounded sector volume (x - a)^n / n! across dimensions 1 to max_dimension.
    """
    x = Decimal(str(x_val))
    a = Decimal(str(a_val))
    radial_distance = x - a

    print(f"--- Simulated Cube & Factorial Container (x={x}, a={a}, distance={radial_distance}) ---")
    print(f"{'Dim (n)':<10} | {'Raw Cube (x-a)^n':<22} | {'Container (n!)':<18} | {'Bounded Sector Volume'}")
    print("-" * 80)

    total_converging_sum = Decimal('0')

    for n in range(1, max_dimension + 1):
        raw_cube_volume = radial_distance ** n
        factorial_container = Decimal(math.factorial(n))
        bounded_sector = raw_cube_volume / factorial_container
        total_converging_sum += bounded_sector

        print(f"{n:<10} | {str(raw_cube_volume):<22} | {str(factorial_container):<18} | {bounded_sector:.10f}")

    print("-" * 80)
    print(f"Total Converging Shell Sum (up to n={max_dimension}): {total_converging_sum:.10f}\n")

if __name__ == "__main__":
    # Example: radial expansion x = 5 around center a = 2 up to 10 dimensions
    simulated_cube_container(x_val=5, a_val=2, max_dimension=10)
