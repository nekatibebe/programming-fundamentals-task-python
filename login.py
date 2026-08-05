from datetime import datetime, timedelta
import time
def login_system():
    credentials = {"feleke": "feleke123","guest": "guest21","hacker": "hacker32"}# Store credentials in a dictionary (Username: Password)
    failed_attempts = 0
    print("=== WELCOME TO THE LOGIN SYSTEM ===")
    while True:
        print("\n--- Enter Credentials ---")# Prompt for user input
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if username in credentials and credentials[username] == password:# Check credentials
            print("\n=================================")
            print("Login Successful!")
            print("=================================")
            break  # Terminate program on successful login
        else:
            failed_attempts += 1
            print(f"\n[ERROR] Invalid username or password.")
            print(f"Consecutive Failed Attempts: {failed_attempts}/5")
            if failed_attempts >= 5:# Trigger lockout after 5 consecutive failed attempts
                lockout_time = datetime.now()
                print(f"\n[ACCOUNT LOCKED] Too many failed attempts.")
                print(f"Lockout initiated at: {lockout_time.strftime('%Y-%m-%d %H:%M:%S')}")
                for remaining in range(60, 0, -1):# Countdown loop: Updates only the time on a single line every second
                    print(f"\rPlease wait {remaining:2d} seconds before trying again...", end="", flush=True)# \r moves the cursor back to the start of the line
                    time.sleep(1)# end="" prevents printing a new line
                print("\n\n[INFO] Lockout period has expired. You may try logging in again.")
                failed_attempts = 0  # Reset failed counter
if __name__ == "__main__":
    login_system()
