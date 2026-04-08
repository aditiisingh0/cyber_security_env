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
    response = client.chat.completions.create(
        model=os.environ.get("MODEL_NAME", "meta-llama/Llama-3.1-8B-Instruct"),
        messages=[
            {
                "role": "system",
                "content": """You are a cybersecurity defense agent. 
Choose the best action from: block_ip, scan_file, quarantine_file, enable_firewall, monitor.
Reply with ONLY the action name, nothing else."""
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
    print(f"Action: {action}, Reward: {reward.reward}, Health: {state.system_health}")

print("Finished")