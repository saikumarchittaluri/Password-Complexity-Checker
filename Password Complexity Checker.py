import re

# Function to check password complexity
def check_password_strength(password):
    # Criteria to check the password
    length_criteria = len(password) >= 8  # At least 8 characters
    uppercase_criteria = re.search(r'[A-Z]', password)  # At least one uppercase letter
    lowercase_criteria = re.search(r'[a-z]', password)  # At least one lowercase letter
    digit_criteria = re.search(r'[0-9]', password)  # At least one digit
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)  # At least one special character

    # Calculate the score based on the number of criteria met
    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    # Provide feedback based on the score
    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria

# Feedback function to help user improve the password
def provide_feedback(strength, length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria):
    feedback = []
    
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character (!@#$%^&*()).")

    return feedback

# Input the password from the user
password = input("Enter a password to check its strength: ")

# Check password strength
strength, length, uppercase, lowercase, digit, special_char = check_password_strength(password)

# Display the result
print(f"Password Strength: {strength}")

# Provide suggestions if the password is weak or moderate
if strength != "Strong":
    feedback = provide_feedback(strength, length, uppercase, lowercase, digit, special_char)
    print("Suggestions to improve your password:")
    for suggestion in feedback:
        print(f"- {suggestion}")