# breach_check.py

import hashlib
import requests

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        res = requests.get(url)
        if res.status_code != 200:
            return False, "API error"
        hashes = (line.split(':') for line in res.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return True, int(count)
        return False, 0
    except Exception as e:
        return False, f"Error: {str(e)}"