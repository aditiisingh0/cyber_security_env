import random
from models import Observation, Reward

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

        elif action == "scan_file" and self.malware_detected:
            reward += 2

        elif action == "quarantine_file" and self.malware_detected:
            self.malware_detected = False
            reward += 3

        elif action == "enable_firewall" and self.ddos_attack:
            self.ddos_attack = False
            reward += 2

        elif action == "shutdown_server":
            self.system_health += 5
            reward -= 2

        else:
            reward -= 0.5

        # Random attacks
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