import numpy as np
from backend.gra_core import nullification_operator, chiral_mapping

def verify_nullification():
    pi = np.array([0.5, -0.3, 0.8])
    w = np.array([0.1, 0.2, -0.1])
    s = np.array([0.4, -0.1, 0.3])
    pi_prime, w_prime, s_prime = nullification_operator(pi, w, s)
    R, L = chiral_mapping(pi)
    expected_pi_prime = np.concatenate([R, L])
    assert np.allclose(pi_prime, expected_pi_prime), "pi_prime mismatch"
    assert w_prime == 0.0 and s_prime == 0.0, "w or s not zero"
    print("Nullification verification passed: w and s are zero, pi' is chiral pair.")

if __name__ == "__main__":
    verify_nullification()
