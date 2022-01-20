#!/usr/bin/env python3
import base64, pyotp, time
# Generate a secret key
secret = pyotp.random_base32()
# Generate a TOTP object
totp = pyotp.TOTP(secret)

# Let user store this.
print("Secret:", secret)
print("Keep this sir.")

current = 000000
last = 000000

print("Make sure your time is synchronized with the user")

while True:
    last = totp.now()
    # To check if the TOTP is same as the last one
    # If it is, it won't output, and vice versa
    if last == current:
        # To avoid too much power consumption
        # Well you know, TOTP can't generate codes that fast and .5 seconds is totally enough
        time.sleep(.5)
        pass
    else:
        current = last
        # Get time so that users can know their TOTP to expire or if their time is synchronized
        # In best cases, the time is synchronized
        # But if not, you can have 30 secs to let it breathe a little
        # Or you can just wait for the next code
        # LOL
        utc = time.ctime(time.time())
        print(utc, " New Code Caught!:", current)
        # So far not considering about the storage of it
        # Because why....
        # Well there is a reason. You know what if user's time is not synchronized and it is rediculous to off 30 secs.
        # Then they will never match, and you will never get the code.
        # So in the future, maybe I will store the -1, 0 and +1, three codes, and check if the code is in the range of them.
        
# Sudden Inspriation
# Why don't I push them to Telegram bot?
# Yeah, why not.
# Let's go.
