import random
from models import Observation, Reward

# ✅ --- GRADER FUNCTIONS ADD KIYE ---
def grade_easy(env):
    return not env.malware_detected  # malware remove hona chahiye

def grade_medium(env):
    return not env.ddos_attack  # ddos band hona chahiye

def grade_hard(env):
    return env.system_health > 0 and env.time_step >= 50  # survive 50 steps


# ✅ --- TASKS WITH GRADERS ---
tasks = [
    {
        "name": "easy",
        "description": "Detect and remove malware",
        "grader": grade_easy
    },
    {
        "name": "medium",
        "description": "Stop DDoS attack",
        "grader": grade_medium
    },
    {
        "name": "hard",
        "description": "Protect system for 50 steps",
        "grader": grade_hard
    }
]


class CyberSecurityEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.system_health = 100
        self.cpu_usage = random.randint(10, 50)
        self.network_traffic = random.randint(50, 100)
        self.suspicious_ips = random.randint(0, 3)
        self.malware_detected = random.choice([True, False])
        self.ddos_attack = random.choice([True, False])
        self.time_step = 0
        return self.state()

    def state(self):
        return Observation(
            system_health=self.system_health,
            cpu_usage=self.cpu_usage,
            network_traffic=self.network_traffic,
            suspicious_ips=self.suspicious_ips,
            malware_detected=self.malware_detected,
            ddos_attack=self.ddos_attack,
            time_step=self.time_step
        )

    def step(self, action):
        reward = 0

        if action == "block_ip" and self.suspicious_ips > 0:
            self.suspicious_ips -= 1
            reward += 1

        if action == "scan_file" and self.malware_detected:
            reward += 2

        if action == "quarantine_file" and self.malware_detected:
            self.malware_detected = False
            reward += 3

        if action == "enable_firewall" and self.ddos_attack:
            self.ddos_attack = False
            reward += 2

        if action == "shutdown_server":
            self.system_health += 5
            reward -= 2

        if reward == 0:
            reward -= 0.5

        if random.random() < 0.3:
            self.malware_detected = True

        if random.random() < 0.2:
            self.ddos_attack = True

        if self.ddos_attack:
            self.system_health -= 3

        if self.suspicious_ips > 0:
            self.system_health -= 2

        self.time_step += 1
        done = self.system_health <= 0 or self.time_step >= 50

        return self.state(), Reward(reward=reward), done, {}
