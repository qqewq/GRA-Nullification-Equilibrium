import pytest
import numpy as np
from backend.gra_core import compute_foam, chiral_mapping, nullification_operator, wave_nullification

def test_compute_foam():
    pi = np.array([1.0, 0.0])
    w = np.array([0.0, 1.0])
    s = np.array([0.5, 0.5])
    phi = compute_foam(pi, w, s)
    # expected: |1-0|+|0-1|+|1-0.5|+|0-0.5| + ... actually compute
    expected = (abs(1-0)+abs(0-1)+abs(1-0.5)+abs(0-0.5))  # simplified
    assert phi == expected, f"Expected {expected}, got {phi}"

def test_chiral_mapping():
    pi = np.array([1.0, -2.0, 3.0])
    R, L = chiral_mapping(pi)
    np.testing.assert_array_equal(R, pi)
    expected_L = np.array([1.0, 2.0, 3.0])  # because odd index (1) sign flipped
    np.testing.assert_array_equal(L, expected_L)

def test_nullification_operator():
    pi = np.array([1.0, 2.0])
    w = np.array([0.5, 0.5])
    s = np.array([-0.2, 0.8])
    pi_prime, w_prime, s_prime = nullification_operator(pi, w, s)
    # pi_prime should be concatenation of R and L
    R, L = chiral_mapping(pi)
    expected_pi_prime = np.concatenate([R, L])
    np.testing.assert_array_equal(pi_prime, expected_pi_prime)
    assert w_prime == 0.0
    assert s_prime == 0.0

def test_wave_nullification():
    phi = 0.5
    psi = wave_nullification(phi, lam=2.0)
    expected = np.exp(-2.0 * 0.5)  # exp(-1)
    assert psi == expected
