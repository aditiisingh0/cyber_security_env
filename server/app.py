import sys
sys.path.insert(0, '/app')

from fastapi import FastAPI
from models import Action
import uvicorn

# Import with fallback
try:
    from env import CyberSecurityEnv
except ImportError:
    import importlib.util
    spec = importlib.util.spec_from_file_location("env", "/app/env.py")
    env_module = importlib.util.load_from_spec(spec)
    spec.loader.exec_module(env_module)
    CyberSecurityEnv = env_module.CyberSecurityEnv

app = FastAPI()
env = CyberSecurityEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return env.reset().dict()

@app.post("/step")
def step(action: Action):
    state, reward, done, _ = env.step(action.action)
    return {
        "state": state.dict(),
        "reward": reward.reward,
        "done": done
    }

@app.get("/state")
def state():
    return env.state().dict()

def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()