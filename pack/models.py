from .db_custom import User

def pwdchecker(password):
    message = None

    if len(password) < 10:
        message = "Password must be at least 10 characters long."
    elif len(password) > 20:
        message = "Password must be at most 20 characters long."
    elif not any(char.isdigit() for char in password):
        message = "Password must contain at least one digit."
    elif not any(char.isupper() for char in password):
        message = "Password must contain at least one uppercase letter."
    elif not any(char.islower() for char in password):
        message = "Password must contain at least one lowercase letter."
    elif not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password):
        message = "Password must contain at least one special character."
    elif any(char.isspace() for char in password):
        message = "Password must not contain any whitespace."
    return message

def userchecker(username):
    message = None
    user = User.query.filter_by(username=username).first()

    if len(username) < 5:
        message = "Username must be at least 5 characters long."
    elif len(username) > 20:
        message = "Username must be at most 20 characters long."
    elif any(char.isspace() for char in username):
        message = "Username must not contain any whitespace."
    elif not username.isalnum():
        message = "Username must contain only alphanumeric characters."
    elif not username.islower():
        message = "Username must contain only lowercase characters."
    elif user:
        message = "Username already exists. Try another one."
    return message

def emailchecker(email):
    message = None
    user = User.query.filter_by(email=email).first()

    # length and format of email
    if len(email) < 8:
        message = "Spam Email address detected. Try another one."
    elif len(email) > 25:
        message = "Email must be at most 25 characters long."
    elif not email.count('@') == 1:
        message = "Email must contain exactly one '@' character."
    elif not email.count('.') >= 1:
        message = "Email must contain at least one '.' character."
    elif any(char.isspace() for char in email):
        message = "Email must not contain any space."
    elif user:
        message = "Email already exists. Try another one."

    # supported email domains
    if email.endswith('gmail.com'):
        message = None
    elif email.endswith('yahoo.com'):
        message = None
    elif email.endswith('hotmail.com'):
        message = None
    elif email.endswith('outlook.com'):
        message = None
    else:
        message = "The email domain is not supported. Try with Gmail, Hotmail, Yahoo or Outlook"
    
    return message