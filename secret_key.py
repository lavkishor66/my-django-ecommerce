import os
from django.core.management.utils import get_random_secret_key

# File path for the secret key
key_file_path = os.path.join(os.path.dirname(__file__), 'secret_key.txt')

# Check if the secret key file exists
if os.path.exists(key_file_path):
    with open(key_file_path, 'r') as key_file:
        secret_key = key_file.read().strip()
else:
    secret_key = get_random_secret_key()
    with open(key_file_path, 'w') as key_file:
        key_file.write(secret_key)

# Make sure to include this line to expose secret_key
__all__ = ['secret_key']

