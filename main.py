from pyscript import display, document

def create_account(e):
    document.getElementById('output').innerHTML = ' '

    username = document.getElementById('username').value
    password = document.getElementById('password').value
    password_length = len(password)
    username_length = len(username)

    if not password.isalpha():
        if password.isdigit():
            display(f'Password must contain at least one letter.', target="output")
        elif password_length < 10:
            display(f'Password must be at least 10 characters long', target="output")
        elif username_length < 7:
            display(f'Username must be at least 7 characters long', target="output")
        else:
            display(f'Account created! Please proceed to the Team Checker.', target="output")
    else:
        display(f'Password must contain at least one number.', target="output")