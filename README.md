
# Password Strength Checker

## Overview
This project is a Python-based tool designed to assess the strength of a password. It evaluates the password based on the following criteria:
- Length of the password (minimum 8 characters).
- Presence of uppercase letters.
- Presence of lowercase letters.
- Presence of numbers.
- Presence of special characters.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kur1an/SCT_CS_03.git
   cd SCT_CS_03
   ```

2. **Ensure Python is installed**:
   Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Usage
1. **Run the Script**:
   Navigate to the directory where the script is saved and run the following command:
   ```bash
   python password_strength_checker.py
   ```

2. **Input a Password**:
   When prompted, enter a password to check its strength. The script will assess the password based on the defined criteria and provide a strength rating.

## Example
Here's an example of running the script and checking a password:

```bash
$ python password_strength_checker.py
Enter a password to check its strength: MySecureP@ssw0rd!
Password Strength: Very Strong
```

## Criteria
- **Very Strong**: Meets all five criteria.
- **Strong**: Meets four criteria.
- **Medium**: Meets three criteria.
- **Weak**: Meets two criteria.
- **Very Weak**: Meets one or no criteria.


## Topics
- Password Strength
- Python
- Cybersecurity
- Regular Expressions
- Command Line Tool