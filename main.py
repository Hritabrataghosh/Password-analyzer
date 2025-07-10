# cli.py

from analyzer import analyze_password
from breach_check import check_pwned


def main():
    print("🔐 Password Analyzer CLI 🔐")
    while True:
        password = input("Enter a password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break

        result = analyze_password(password)
        print("\n📊 Analysis Report:")
        print(f"Password: {'*' * len(result['password'])}")
        print(f"Length  : {result['length']}")
        print(f"Entropy : {result['entropy']} bits")
        print(f"Strength: {result['strength']}")

        breached, info = check_pwned(password)
        if breached:
            print(f"⚠️ WARNING: This password has been found in {info:,} breaches!")
        elif info == 0:
            print("✅ Good news! This password is not found in known breaches.")
        else:
            print(f"⚠️ Could not check breach status: {info}")

        print("-" * 40)


if __name__ == "__main__":
    main()