import re

# password must be:
# 1. at least 8 characters long
# 2. contains both uppercase and lowercase
# 3. has at least one digit

pswd_regex = re.compile(r'[A-Za-z]{8,}')
# pswd_regex = re.compile(r'\W{8,}')
password = 'ABcdeH111DD'
x = pswd_regex.search(password)

if x is None:
    print('Password not strong enough')