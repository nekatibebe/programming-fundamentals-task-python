import tkinter as tk
import time
class LockScreenApp:
    def __init__(self, root, secret_pin):
        self.root = root
        self.root.title("Mock Smartphone Lock Screen")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)
        self.secret_pin = secret_pin
        self.attempts = 0
        self.start_time = 0
        self.setup_ui()
    def setup_ui(self):
        left_frame = tk.Frame(self.root, bg="#1e1e2e", width=320, height=500)
        left_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        self.status_label = tk.Label(
            left_frame, 
            text="LOCKED", 
            font=("Helvetica", 16, "bold"),
            fg="#f38ba8", 
            bg="#1e1e2e"
        )
        self.status_label.pack(pady=(20, 10))
        self.pin_display = tk.Label(
            left_frame, 
            text="• • • •", 
            font=("Consolas", 24, "bold"),
            fg="#cdd6f4", 
            bg="#313244", 
            width=12, 
            height=2, 
            relief="solid", 
            bd=1
        )
        self.pin_display.pack(pady=10)
        self.info_label = tk.Label(
            left_frame, 
            text="Attempts: 0  |  Time: 0.00s",
            font=("Helvetica", 10), 
            fg="#a6adc8", 
            bg="#1e1e2e"
        )
        self.info_label.pack(pady=10)
        self.start_btn = tk.Button(
            left_frame, 
            text="Start Brute-Force", 
            font=("Helvetica", 11, "bold"),
            bg="#89b4fa", 
            fg="#11111b", 
            activebackground="#b4befe",
            padx=10, 
            pady=5, 
            command=self.run_brute_force
        )
        self.start_btn.pack(pady=15)
    right_frame = tk.Frame(self.root, bg="#1e1e2e")
        right_frame.pack(side="right", fill="both", expand=True, padx=(0, 20), pady=20)
        log_label = tk.Label(
            right_frame, 
            text="Attempted Pairs Log:", 
            font=("Helvetica", 11, "bold"), 
            fg="#cdd6f4", 
            bg="#1e1e2e"
        )
        log_label.pack(anchor="w", pady=(0, 5))
        scrollbar = tk.Scrollbar(right_frame)
        scrollbar.pack(side="right", fill="y")
        self.log_listbox = tk.Listbox(
            right_frame, 
            font=("Consolas", 10), 
            bg="#181825", 
            fg="#a6adc8", 
            selectbackground="#313244",
            bd=0, 
            yscrollcommand=scrollbar.set
        )
        self.log_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.log_listbox.yview)
    def run_brute_force(self):
        self.start_btn.config(state="disabled")
        self.status_label.config(text="ATTACKING...", fg="#fab387")
        self.log_listbox.delete(0, tk.END)
        self.start_time = time.time()
        def step(i=0):
            if i < 10000:
                current_attempt = f"{i:04d}"
                self.attempts = i + 1
                elapsed = time.time() - self.start_time
                self.pin_display.config(text=current_attempt)
                self.info_label.config(text=f"Attempts: {self.attempts}  |  Time: {elapsed:.2f}s")
                log_entry = f"Attempt #{self.attempts:04d}: [{current_attempt}]"
                self.log_listbox.insert(tk.END, log_entry)
                self.log_listbox.see(tk.END)
                if current_attempt == self.secret_pin:
                    self.status_label.config(text="UNLOCKED! ✅", fg="#a6e3a1")
                    self.pin_display.config(fg="#a6e3a1")
                    self.log_listbox.insert(tk.END, f"=== MATCH FOUND: {current_attempt} ===")
                    self.log_listbox.see(tk.END)
                    return
                self.root.after(1, step, i + 1)
            else:
                self.status_label.config(text="FAILED ❌", fg="#f38ba8")
        step()
if __name__ == "__main__":
    secret = input("Enter a 4-digit secret PIN to crack: ").strip()
    if len(secret) == 4 and secret.isdigit():
        root = tk.Tk()
        app = LockScreenApp(root, secret)
        root.mainloop()
    else:
        print("Invalid input! Please enter exactly 4 numeric digits.")
