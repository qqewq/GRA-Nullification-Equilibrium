# Helper to generate initial states for demos
import numpy as np

def random_state(dim=3):
    pi = np.random.uniform(-1, 1, dim)
    w = np.random.uniform(-1, 1, dim)
    s = np.random.uniform(-1, 1, dim)
    return pi, w, s
