def easy_grader(env):
    return 1.0 if env.malware_detected == False else 0.0

def medium_grader(env):
    return 1.0 if env.ddos_attack == False else 0.0

def hard_grader(env):
    return min(1.0, env.time_step / 50)