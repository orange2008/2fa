#!/usr/bin/env python3
import base64, pyotp, time
# Get the secret key from the user
secret = input("Secret: ")
# Generate a TOTP object
totp = pyotp.TOTP(secret)
# Verify
usr = input("Code: ")
if totp.verify(usr):
    print("Valid")
else:
    print("Invalid")

