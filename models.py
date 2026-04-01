from pydantic import BaseModel

class Observation(BaseModel):
    system_health: int
    cpu_usage: int
    network_traffic: int
    suspicious_ips: int
    malware_detected: bool
    ddos_attack: bool
    time_step: int

class Action(BaseModel):
    action: str

class Reward(BaseModel):
    reward: float