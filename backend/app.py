from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from typing import List
from gra_core import compute_foam, nullification_operator, simulate_foam_evolution

app = FastAPI(title="GRA Nullification Equilibrium API")

class InputData(BaseModel):
    pi: List[float]
    w: List[float]
    s: List[float]
    steps: int = 10

class OutputData(BaseModel):
    phi_history: List[float]
    pi_history: List[List[float]]
    final_pi: List[float]
    final_w: float
    final_s: float

@app.get("/")
def root():
    return {"message": "GRA Nullification Equilibrium API"}

@app.post("/simulate", response_model=OutputData)
def simulate(data: InputData):
    try:
        pi = np.array(data.pi)
        w = np.array(data.w)
        s = np.array(data.s)
        steps = data.steps
        if len(pi) != len(w) or len(w) != len(s):
            raise HTTPException(status_code=400, detail="Vectors must have same length")
        phi_hist, pi_hist = simulate_foam_evolution(pi, w, s, steps)
        # final state after last iteration
        final_pi = pi_hist[-1].tolist()
        # after nullification, w and s are zero, but in simulation they are reset each step
        # we return last computed w,s (which are zero)
        return OutputData(
            phi_history=phi_hist,
            pi_history=[p.tolist() for p in pi_hist],
            final_pi=final_pi,
            final_w=0.0,
            final_s=0.0
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
