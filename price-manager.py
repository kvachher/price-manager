import tkinter as tk

ans_dict = {}

class gui:
    def __init__(self):
        ans_dict.clear()
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Enter the people splitting here, separated by commas.", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=('Arial', 16), height=2)
        self.textbox.pack(padx=10, pady=10)

        self.label = tk.Label(self.root, text="Enter the price below. Exclude any currency markers.", font=('Arial', 16))
        self.label.pack(padx=10, pady=10)

        self.myentry = tk.Entry(self.root)
        self.myentry.pack(padx=10)

        self.button = tk.Button(self.root, text="Calculate", font=('Arial', 16), command=self.calculate)
        self.button.pack(padx=10, pady=10)

        self.res = tk.Text(self.root, font=('Arial', 16))
        self.res.pack(padx=10, pady=10)

        self.running_sum_label = tk.Label(self.root, text="Running Sum: ", font=('Arial', 16))
        self.running_sum_label.pack(padx=10, pady=10)
        
        self.running_sum_value = tk.StringVar()
        self.running_sum_display = tk.Label(self.root, textvariable=self.running_sum_value, font=('Arial', 16))
        self.running_sum_display.pack(padx=10, pady=10)

        self.root.mainloop()

    def calculate(self):
        ppl = self.textbox.get("1.0", tk.END).strip().split(",")
        price = float(self.myentry.get())
        self.det_split(price, ppl)
        self.print_results()
        self.update_running_sum()

    def det_split(self, price, splitters):
        per_person = price / len(splitters)
        for s in splitters:
            s = s.strip()
            ans_dict[s.upper()] = round(ans_dict.get(s.upper(), 0) + per_person, 2)

    def print_results(self):
        self.res.delete("1.0", tk.END)
        self.res.insert(tk.END, "Results:\n")
        for d in ans_dict:
            self.res.insert(tk.END, f'{d} owes {ans_dict[d]:.2f}\n')

    def update_running_sum(self):
        total_sum = round(sum(ans_dict.values()), 2)
        self.running_sum_value.set(str(total_sum))

if __name__ == "__main__":
    my_gui = gui()