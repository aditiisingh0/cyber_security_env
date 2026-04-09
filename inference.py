import os
from openai import OpenAI
from env import CyberSecurityEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://api-inference.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Llama-3.1-8B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)


def run_task(task_name):
    env = CyberSecurityEnv()
    state = env.reset()
    done = False

    print(f"[START] task={task_name}", flush=True)

    step_num = 0
    while not done:
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a cybersecurity defense agent. Choose one action from: block_ip, scan_file, quarantine_file, enable_firewall, monitor. Reply with ONLY the action name."
                    },
                    {
                        "role": "user",
                        "content": f"Health:{state.system_health} IPs:{state.suspicious_ips} Malware:{state.malware_detected} DDoS:{state.ddos_attack}. Action?"
                    }
                ],
                max_tokens=10,
                temperature=0
            )

            action = response.choices[0].message.content.strip().lower()
            valid = ["block_ip","scan_file","quarantine_file","enable_firewall","monitor"]

            if action not in valid:
                action = "monitor"

        except Exception as e:
            print(f"API error: {e}", flush=True)
            action = "monitor"

        state, reward, done, _ = env.step(action)

        print(f"[STEP] task={task_name} step={step_num} action={action} reward={round(reward.reward, 2)}", flush=True)
        step_num += 1

    score = max(0.01, min(0.99, round(state.system_health / 100, 2)))
    print(f"[END] task={task_name} score={score} steps={step_num}", flush=True)


# ✅ RUN ALL 3 TASKS
run_task("easy")
run_task("medium")
run_task("hard")
