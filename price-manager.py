import tkinter as tk

ans_dict = {}

class gui : 
    def __init__(self): 
            ans_dict.clear()
            self.root = tk.Tk()
            self.label = tk.Label(self.root, text = "Enter the people splitting here, seperated by commas.", font = ('Arial', 18))
            self.label.pack(padx = 10, pady = 10)

            self.textbox = tk.Text(self.root, font = ('Arial', 16), height = 2)
            self.textbox.pack(padx = 10, pady = 10)

            self.label = tk.Label(self.root, text = "Enter the price below. Exclude any currency markers.", font = ('Arial', 16))
            self.label.pack(padx = 10, pady = 10)

            self.myentry = tk.Entry(self.root)
            self.myentry.pack(padx = 10)

            self.button = tk.Button(self.root, text = "Calculate", font = ('Arial', 16), command = self.calculate)
            self.button.pack(padx = 10, pady = 10)

            self.res = tk.Text(self.root, font = ('Arial', 16))
            self.res.pack(padx = 10, pady = 10)

            self.root.mainloop()

    def calculate(self) : 
        ppl = self.textbox.get("1.0", tk.END).strip().split(",")
        price = float(self.myentry.get())
        self.det_split(price, ppl)
        self.print_results()


    def det_split(self, price, splitters) : 
        per_person = price / len(splitters)
        for s in splitters : 
            s = s.strip()
            ans_dict[s.lower()] = ans_dict.get(s.lower(), 0) + per_person

    def print_results(self) : 
        self.res.delete("1.0", tk.END)
        self.res.insert(tk.END, "Results:\n")
        for d in ans_dict: 
            self.res.insert(tk.END, f'{d} owes {str(ans_dict[d])}\n')

if __name__ == "__main__":
    my_gui = gui()

