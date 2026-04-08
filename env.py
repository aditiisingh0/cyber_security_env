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

    # Penalize only if no condition met
    if reward == 0:
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