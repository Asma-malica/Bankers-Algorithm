import tkinter as tk

class BankerUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Banker's Algorithm")

        self.num_processes = 0
        self.num_resources = 0

        self.processes_label = tk.Label(self, text="Enter the number of processes:")
        self.processes_entry = tk.Entry(self)
        self.resources_label = tk.Label(self, text="Enter the number of resources:")
        self.resources_entry = tk.Entry(self)
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_input)

        self.processes_label.pack()
        self.processes_entry.pack()
        self.resources_label.pack()
        self.resources_entry.pack()
        self.submit_button.pack()

    def submit_input(self):
        self.num_processes = int(self.processes_entry.get())
        self.num_resources = int(self.resources_entry.get())

        self.destroy()  # Close the input window
        self.show_output()

    def show_output(self):
        banker = Banker(self.num_processes, self.num_resources)
        banker.get_input()
        banker.calculate_need()

        output_window = tk.Toplevel(self)
        output_window.title("Banker's Algorithm - Output")

        output_label = tk.Label(output_window, text="Output:")
        output_label.pack()

        text_widget = tk.Text(output_window)
        text_widget.pack()

        def display_table():
            text_widget.insert(tk.END, "Process\t\tMax\t\tAllocation\tNeed\t\tAvailable\n")
            for i in range(banker.num_processes):
                text_widget.insert(tk.END,
                                   f"P{i + 1}\t\t{banker._max[i]}\t{banker.allocation[i]}\t{banker.need[i]}\t{banker.available}\n")

        def display_safe_sequence():
            sequence = banker.safe_state()
            if sequence is None:
                text_widget.insert(tk.END, "No safe sequence found.\n")
            else:
                text_widget.insert(tk.END, "Safe Sequence: " + " -> ".join(sequence) + "\n")

        display_table()
        display_safe_sequence()

        text_widget.config(state=tk.DISABLED)  # Disable editing

if __name__ == "__main__":
    banker_ui = BankerUI()
    banker_ui.mainloop()
