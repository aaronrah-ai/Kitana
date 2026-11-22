import math

def run_consolidated_pages():
    print("=== PAGE 1: PYTHAGORAS THEOREM & THE GOLDEN RATIO ===")
    
    # 1. Primary Right Triangle & Golden Ratio (Phi)
    leg1, leg2 = 1.0, 0.5
    hyp1 = math.sqrt(leg1**2 + leg2**2)  # sqrt(1.25)
    phi = leg2 + hyp1                    # 0.5 + sqrt(1.25) ≈ 1.618034
    print(f"Hypotenuse 1 (sqrt(1.25)): {hyp1:.6f}")
    print(f"Golden Ratio (Phi): {phi:.6f}")

    # 2. Second Triangle & Inverse Tangent
    frac_sum = 2 * (32 / 4) + (1 / 4)    # 64/4 + 1/4 = 65/4 = 16.25
    hyp2 = math.sqrt(frac_sum)           # sqrt(16.25) ≈ 4.031129
    half_hyp2 = hyp2 / 2                 # sqrt(65/4) / 2 ≈ 2.015564
    theta_tan = math.degrees(math.atan(half_hyp2))
    print(f"Fraction Sum (65/4): {frac_sum}")
    print(f"Inverse Tangent Angle (theta): {theta_tan:.2f} degrees\n")

    print("=== PAGE 2: TRIANGLES COMPARING HYPOTENUSE ===")
    
    # 1. Inverse Cosine & Angle Complement
    cos_ratio = 2 / 4.5
    angle_a = math.degrees(math.acos(cos_ratio))
    angle_complement = 180 - 90 - angle_a
    print(f"cos^-1(2 / 4.5): {angle_a:.2f} degrees (Complement: {angle_complement:.2f} degrees)")

    # 2. Kepler Triangle & Solving for n
    phi_sq = phi**2                      # (0.5 + sqrt(1.25))^2 ≈ 2.618034
    n_kepler = phi_sq / (4.5 * half_hyp2)
    kepler_check = 1**2 + (math.sqrt(phi))**2
    print(f"Phi^2: {phi_sq:.6f} (Kepler Check 1^2 + sqrt(Phi)^2 = {kepler_check:.6f})")
    print(f"Solved n (Kepler block): {n_kepler:.4f}")

    # 3. Binomial Square of Roots Identity (1 + Phi = Phi^2)
    binomial_expansion = 0.25 + (2 * math.sqrt(1.25) * math.sqrt(0.25)) + 1.25
    print(f"Binomial Expansion ((sqrt(0.25) + sqrt(1.25))^2): {binomial_expansion:.5f}")

    # 4. Final Scaling & Convergence Steps
    scaled_n = n_kepler * 10             # 2.886
    step1 = math.sqrt(phi_sq / scaled_n) * 4.5
    step2_exact = 4.5 - step1            # 0.214 (or 0.21 using rounded 4.29)
    final_n_rounded = phi / 0.21         # 7.705
    final_n_exact = phi / step2_exact    # 7.561
    
    print(f"Step 1 (sqrt(2.618 / 2.886) * 4.5): {step1:.3f} (Rounded: 4.29)")
    print(f"Final n (using rounded 0.21): {final_n_rounded:.2f}")
    print(f"Final n (using unrounded 0.214): {final_n_exact:.2f}")

if __name__ == "__main__":
    run_consolidated_pages()
