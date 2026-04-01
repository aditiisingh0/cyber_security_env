def calculate_reward(action, env):
    reward = 0
    
    if action == "block_ip" and env.suspicious_ips > 0:
        reward += 1
    elif action == "scan_file" and env.malware_detected:
        reward += 2
    elif action == "quarantine_file" and env.malware_detected:
        reward += 3
    elif action == "enable_firewall" and env.ddos_attack:
        reward += 2
    else:
        reward -= 0.5

    return reward