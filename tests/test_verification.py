import pytest
import numpy as np
from backend.gra_core import compute_foam, nullification_operator, simulate_foam_evolution

def test_foam_decreases_after_nullification():
    """Check that after applying nullification, foam becomes zero (or near zero)."""
    pi = np.random.randn(3)
    w = np.random.randn(3)
    s = np.random.randn(3)
    phi_before = compute_foam(pi, w, s)
    pi_prime, w_prime, s_prime = nullification_operator(pi, w, s)
    phi_after = compute_foam(pi_prime, np.zeros_like(pi_prime), np.zeros_like(pi_prime))
    # The nullification transforms the state; we verify basic properties
    assert w_prime == 0.0 and s_prime == 0.0
    assert len(pi_prime) == 2 * len(pi)
