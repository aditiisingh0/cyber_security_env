from fastapi import FastAPI
from env import CyberSecurityEnv

app = FastAPI()
env = CyberSecurityEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return env.reset().dict()

@app.post("/step")
def step(action: str):
    state, reward, done, _ = env.step(action)
    return {
        "state": state.dict(),
        "reward": reward.reward,
        "done": done
    }

@app.get("/state")
def state():
    return env.state().dict()
