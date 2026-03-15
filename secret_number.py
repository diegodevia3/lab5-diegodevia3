import random

def generate_secret(seed):
    random.seed(seed)
    return random.randint(1, 100)