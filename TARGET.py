# This code is for educational purposes only. Brute-forcing logins is unethical
# and can violate terms of service. It's recommended to use strong passwords
# and two-factor authentication for your accounts.

import time

print("""
This script is for educational purposes only. Brute-forcing logins is unethical
and can violate terms of service. It's recommended to use strong passwords
and two-factor authentication for your accounts.

Press Enter to continue or Ctrl+C to exit.
""")

while True:
    try:
        input()
        break
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()

print("\nNot performing brute-force login. Security is important!")
time.sleep(1)
