import os
from openai import OpenAI
from env import CyberSecurityEnv

API_BASE_URL = os.getenv("API_BASE_URL", "<your-api-base-url>")
MODEL_NAME = os.getenv("MODEL_NAME", "<your-active-model>")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

env = CyberSecurityEnv()
state = env.reset()
done = False

print("START")

step_num = 0
while not done:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a cybersecurity defense agent. Choose one action from: block_ip, scan_file, quarantine_file, enable_firewall, monitor. Reply with ONLY the action name, nothing else."
            },
            {
                "role": "user",
                "content": f"""Current system state:
- System Health: {state.system_health}
- Suspicious IPs: {state.suspicious_ips}
- Malware Detected: {state.malware_detected}
- DDoS Attack: {state.ddos_attack}
- CPU Usage: {state.cpu_usage}
- Network Traffic: {state.network_traffic}
- Time Step: {state.time_step}

What action should you take?"""
            }
        ],
        max_tokens=10,
        temperature=0
    )

    action = response.choices[0].message.content.strip().lower()
    valid_actions = ["block_ip", "scan_file", "quarantine_file", "enable_firewall", "monitor"]
    if action not in valid_actions:
        action = "monitor"

    state, reward, done, _ = env.step(action)
    
    print(f"STEP {step_num}: action={action}, reward={reward.reward}, health={state.system_health}")
    step_num += 1

print("END")