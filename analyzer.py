# analyzer.py

import math
import string

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)
    if pool == 0:
        return 0
    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)

def analyze_password(password):
    entropy = calculate_entropy(password)
    length = len(password)

    if length == 0:
        strength = "Empty"
    elif length < 6 or entropy < 28:
        strength = "Very Weak"
    elif entropy < 40:
        strength = "Weak"
    elif entropy < 60:
        strength = "Moderate"
    elif entropy < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "password": password,
        "length": length,
        "entropy": entropy,
        "strength": strength
    }