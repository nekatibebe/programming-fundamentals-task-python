import time

def brute_force_pin(secret_pin):
    """
    Simulates a brute-force attack to guess a 4-digit secret PIN.
    """
    attempts = 0
    start_time = time.time()  # Start the timer

    print(f"Starting brute-force attack to crack PIN: {secret_pin}\n")

    # Loop through all possible numbers from 0000 to 9999
    for i in range(10000):
        # Format the integer into a 4-digit string with leading zeros (e.g., 5 -> "0005")
        current_attempt = f"{i:04d}"
        attempts += 1

        print(f"Attempt {attempts}: Trying PIN -> {current_attempt}")

        # Check if the generated PIN matches the secret PIN
        if current_attempt == secret_pin:
            end_time = time.time()  # Stop the timer
            time_taken = end_time - start_time

            print("\n" + "=" * 40)
            print("SUCCESS! PIN Cracked Successfully!")
            print(f"Secret PIN : {current_attempt}")
            print(f"Total Attempts: {attempts}")
            print(f"Time Taken  : {time_taken:.4f} seconds")
            print("=" * 40)
            
            return  # Stop the function/program once found

    print("\nPIN not found.")

# Main Execution
if __name__ == "__main__":
    while True:
          Secret_PIN= input("Enter the 4-digit Number:")
          if Secret_PIN.isdigit() and len(Secret_PIN)== 4:
              break
          print("Invalid input, please enter exactly 4 digits!")
           #Run the brute force function
    brute_force_pin(Secret_PIN)
