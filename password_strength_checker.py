import re

def password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength

def main():
    password = input("Enter a password to check its strength: ")
    strength = password_strength(password)
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()