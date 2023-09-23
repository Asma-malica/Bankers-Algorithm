import tkinter as tk
from tkinter import messagebox
from bankers import Banker

class BankerUI:
    def __init__(self, root):
        self.root = root
        self.banker = None

        self.num_processes_entry = tk.Entry(root)
        self.num_resources_entry = tk.Entry(root)
        self.entries = []

        self.create_widgets()

    def create_widgets(self):
        processes_label = tk.Label(self.root, text="Number of Processes:")
        processes_label.pack()
        self.num_processes_entry.pack()

        resources_label = tk.Label(self.root, text="Number of Resources:")
        resources_label.pack()
        self.num_resources_entry.pack()

        submit_button = tk.Button(self.root, text="Submit", command=self.process_input)
        submit_button.pack()

    def process_input(self):
        num_processes = int(self.num_processes_entry.get())
        num_resources = int(self.num_resources_entry.get())

        self.banker = Banker(num_processes, num_resources)

        input_frame = tk.Toplevel(self.root)

        for i in range(num_processes):
            process_label = tk.Label(input_frame, text=f"Process {i + 1}:")
            process_label.grid(row=i, column=0)

            max_entry = tk.Entry(input_frame)
            max_entry.grid(row=i, column=1)

            allocation_entry = tk.Entry(input_frame)
            allocation_entry.grid(row=i, column=2)

            self.entries.append((max_entry, allocation_entry))

        available_label = tk.Label(input_frame, text="Enter the available resources:")
        available_label.grid(row=num_processes, column=0)

        available_entry = tk.Entry(input_frame)
        available_entry.grid(row=num_processes, column=1)

        self.entries.append((available_entry,))

        submit_button = tk.Button(input_frame, text="Submit", command=self.process_resources)
        submit_button.grid(row=num_processes + 1, column=0, columnspan=3)

    def process_resources(self):
        try:
            num_processes = len(self.entries) - 1 # Last entry is available resources
            num_resources = len(self.entries[0]) - 1 # Last entry is process allocation

            for i in range(num_processes):
                max_values = list(map(int, self.entries[i][0].get().split()))
                allocation_values = list(map(int, self.entries[i][1].get().split()))
                self.banker._max.append(max_values)
                self.banker.allocation.append(allocation_values)

            self.banker.available = list(map(int, self.entries[-1][0].get().split()))

            self.banker.calculate_need()
            self.banker.table()
            self.banker.display_safe_sequence()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter integers.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Banker's Algorithm")

    banker_ui = BankerUI(root)

    root.mainloop()

