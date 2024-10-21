import tkinter as tk
from tkinter import ttk
import time

class StudyTimer:
    def __init__(self, root):
        self.root = root
        self.minutes = 0
        self.seconds = 0
        self.running = False

        # display label
        self.time_label = ttk.Label(root, text="00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        # buttons for start, pause, stop
        self.start_button = ttk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side="left", padx=10)

        self.pause_button = ttk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(side="left", padx=10)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left", padx=10)

        # Update second
        self.update_timer()

    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def stop(self):
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.update_display()

    def update_timer(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 25:
                self.minutes = 0

            self.update_display()

        self.root.after(1000, self.update_timer)

    def update_display(self):
        self.time_label.config(text=f"{self.minutes:02}:{self.seconds:02}")

# Set up  root 
root = tk.Tk()
root.title("Study Timer")
root.geometry("300x200")

# Initialize 
timer = StudyTimer(root)

# Start the loop
root.mainloop()
