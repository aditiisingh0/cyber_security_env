---
title: Cyber Security OpenEnv
emoji: 🛡️
colorFrom: blue
colorTo: red
sdk: docker
app_file: app.py
pinned: false
---

# Cyber Security Defense OpenEnv Environment

## Overview
This project is a real-world OpenEnv environment that simulates a cyber security defense system where an AI agent must protect a server from cyber attacks such as malware, DDoS attacks, and suspicious IP activity.

The agent interacts with the environment using actions and receives rewards based on how well it protects the system.

## Environment State (Observation Space)
The agent receives the following state:

- system_health (0–100)
- cpu_usage
- network_traffic
- suspicious_ips
- malware_detected (True/False)
- ddos_attack (True/False)
- time_step

## Actions (Action Space)
The agent can take the following actions:

- monitor
- block_ip
- scan_file
- quarantine_file
- enable_firewall
- shutdown_server

## Reward Design
The agent receives rewards based on performance:

| Action | Reward |
|-------|--------|
| Block suspicious IP | +1 |
| Detect malware | +2 |
| Remove malware | +3 |
| Stop DDoS | +2 |
| Wrong action | -0.5 |
| Unnecessary shutdown | -2 |
| System damage | Negative |

## Tasks

### Easy Task
Detect and remove malware.

### Medium Task
Stop DDoS attack.

### Hard Task
Protect the system for 50 steps.

## Grading
Each task is graded from 0.0 to 1.0 based on performance.

## How to Run
```bash
docker build -t cyber-env .
docker run cyber-env