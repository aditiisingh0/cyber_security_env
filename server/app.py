from fastapi import FastAPI
from env import CyberSecurityEnv
import uvicorn

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

def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
