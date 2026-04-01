import os
from openai import OpenAI
from env import CyberSecurityEnv

client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("HF_TOKEN")
)

env = CyberSecurityEnv()
state = env.reset()
done = False

while not done:
    action = "monitor"
    state, reward, done, _ = env.step(action)

print("Finished")