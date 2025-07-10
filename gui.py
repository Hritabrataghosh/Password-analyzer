import tkinter as tk
from tkinter import StringVar, END
from analyzer import analyze_password
from breach_check import check_pwned
import threading
import time

# --- App Window ---
app = tk.Tk()
app.title("Password Analyzer")
app.geometry("500x350")
app.resizable(False, False)

# --- Variables ---
password_var = StringVar()
entropy_var = StringVar()
strength_var = StringVar()
breach_var = StringVar()

# --- Spinner Placeholder ---
spinner = tk.Label(app, text="", fg="orange", font=("Segoe UI", 10))
spinner.pack(pady=5)

# --- Functions ---
def run_analysis():
    spinner.config(text="Analyzing...")
    time.sleep(0.8)  # a bit of drama

    pw = password_var.get()
    result = analyze_password(pw)
    breached, info = check_pwned(pw)

    entropy_var.set(f"{result['entropy']} bits")
    strength_var.set(result['strength'])

    if breached:
        breach_var.set(f"Found in {info:,} breaches!")
    elif info == 0:
        breach_var.set("No breach found.")
    else:
        breach_var.set(f"Error: {info}")

    result_label.config(text="Analysis complete", fg="green")
    spinner.config(text="")

def analyze():
    if not password_var.get():
        result_label.config(text="Please enter a password!", fg="red")
        return

    entropy_var.set("")
    strength_var.set("")
    breach_var.set("")
    result_label.config(text="")
    spinner.config(text="Analyzing...")
    threading.Thread(target=run_analysis).start()

def clear():
    password_entry.delete(0, END)
    entropy_var.set("")
    strength_var.set("")
    breach_var.set("")
    result_label.config(text="")
    spinner.config(text="")

# --- UI Components ---
tk.Label(app, text="Enter Password", font=("Segoe UI", 12)).pack(pady=10)

password_entry = tk.Entry(app, textvariable=password_var, font=("Segoe UI", 12), show="*", width=30)
password_entry.pack(pady=5)

tk.Button(app, text="Analyze", command=analyze, bg="lightgreen", width=12).pack(pady=5)
tk.Button(app, text="Clear", command=clear, bg="lightgray", width=12).pack()

# --- Output Frame ---
output_frame = tk.Frame(app, padx=10, pady=10)
output_frame.pack()

tk.Label(output_frame, text="Entropy: ", font=("Segoe UI", 10)).grid(row=0, column=0, sticky='w')
tk.Label(output_frame, textvariable=entropy_var, font=("Segoe UI", 10, "bold")).grid(row=0, column=1, sticky='w')

tk.Label(output_frame, text="Strength: ", font=("Segoe UI", 10)).grid(row=1, column=0, sticky='w')
tk.Label(output_frame, textvariable=strength_var, font=("Segoe UI", 10, "bold")).grid(row=1, column=1, sticky='w')

tk.Label(output_frame, text="Breach Status: ", font=("Segoe UI", 10)).grid(row=2, column=0, sticky='w')
tk.Label(output_frame, textvariable=breach_var, font=("Segoe UI", 10, "bold")).grid(row=2, column=1, sticky='w')

# --- Result Message ---
result_label = tk.Label(app, text="", font=("Segoe UI", 10))
result_label.pack(pady=10)

# --- Start App ---
app.mainloop()