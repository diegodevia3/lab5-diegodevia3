from secret_number import generate_secret
from response import check_guess

def main():
    
    seed = int(input("Enter a seed number: "))
    secret = generate_secret(seed)
    