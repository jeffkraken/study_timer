import tkinter as tk
from tkinter import ttk
import time

class StudyTimer:
    def __init__(self, root):
        self.root = root
        self.study_time = 25 * 60
        self.break_time = 5 * 60
        self.current_time = self.study_time
        self.on_break = False
        self.running = False

        # display label
        self.time_label = ttk.Label(root, text=self.format_time(self.current_time), font=("Helvetica", 48))
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

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def stop(self):
        self.running = False
        self.on_break = False
        self.current_time = self.study_time
        self.update_display()

    def update_timer(self):
        if self.running:
            if self.current_time > 0:
                self.current_time -= 1
            else:
                if self.on_break:
                    self.current_time = self.study_time
                    self.on_break = False
                else:
                    self.current_time = self.break_time
                    self.on_break = True

            self.update_display()

        self.root.after(1000, self.update_timer)

    def update_display(self):
        self.time_label.config(text=self.format_time(self.current_time))

# Set up  root 
root = tk.Tk()
root.title("Study Timer")
root.geometry("300x200")

# Initialize 
timer = StudyTimer(root)

# Start the loop
root.mainloop()
