import numpy as np
from backend.gra_core import simulate_foam_evolution

def verify_balance():
    pi = np.array([1.0, -1.0])
    w = np.array([0.5, 0.5])
    s = np.array([-0.5, 0.5])
    phi_hist, pi_hist = simulate_foam_evolution(pi, w, s, steps=20)
    # Check that foam oscillates (not strictly decreasing) indicating balance
    # Compute differences
    diffs = np.diff(phi_hist)
    # There should be both positive and negative diffs
    if np.all(diffs > 0) or np.all(diffs < 0):
        print("Warning: Foam monotonic, no balance observed.")
    else:
        print("Balance verification passed: foam oscillates.")
    # Check that final phi is not zero (generation prevents complete nullification)
    assert phi_hist[-1] > 1e-6, "Foam went to zero, balance not maintained."
    print(f"Final foam: {phi_hist[-1]:.4f}")

if __name__ == "__main__":
    verify_balance()
