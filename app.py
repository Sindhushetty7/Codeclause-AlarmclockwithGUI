import tkinter as tk
from tkinter import messagebox
import datetime
def set_alarm():
    alarm_time_str = entry.get() 
    try:
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM")
        return
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == alarm_time_str:
        messagebox.showinfo("Alarm", "Time's up! Wake up!")
    else:
        delay = (alarm_time - datetime.datetime.now()).seconds * 1000
        root.after(delay, set_alarm) 
# GUI Setup
root = tk.Tk()
root.title("Alarm Clock")
# Label
label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack()
# Entry
entry = tk.Entry(root)
entry.pack()
# Button
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack()
# Run the main event loop
root.mainloop()
