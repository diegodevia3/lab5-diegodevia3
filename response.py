def check_guess(secret, guess):
    
    if guess < secret:
        return "Too low! Try a higher number."
    elif guess > secret:
        return "Too high! Try a lower number."
    else:
        return "Correct!"
    