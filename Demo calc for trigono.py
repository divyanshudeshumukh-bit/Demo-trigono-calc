import tkinter as tk
from tkinter import ttk, messagebox
import math

# ================= CORE LOGIC ================= #

class TrigonometryCalculator:

    @staticmethod
    def calculate_ratio(angle, operation):
        rad = math.radians(angle)

        try:
            operations = {
                "sin": math.sin(rad),
                "cos": math.cos(rad),
                "tan": math.tan(rad),
                "cosec": 1 / math.sin(rad),
                "sec": 1 / math.cos(rad),
                "cot": 1 / math.tan(rad),
            }

            return round(operations[operation], 4)

        except ZeroDivisionError:
            return "Not Defined"


    @staticmethod
    def standard_values(angle):
        values = {
            0: (0, 1),
            30: (0.5, math.sqrt(3)/2),
            45: (math.sqrt(2)/2, math.sqrt(2)/2),
            60: (math.sqrt(3)/2, 0.5),
            90: (1, 0)
        }

        if angle not in values:
            raise ValueError("Invalid Angle")

        sin_val, cos_val = values[angle]

        tan_val = "Not Defined" if cos_val == 0 else round(sin_val/cos_val, 4)

        return sin_val, cos_val, tan_val


    @staticmethod
    def verify_identity(angle):
        rad = math.radians(angle)
        value = math.sin(rad)**2 + math.cos(rad)**2
        return abs(value - 1) < 0.0001


# ================= UI ================= #

class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Trigonometry Calculator")
        self.root.geometry("600x500")
        self.root.configure(bg="#1f1f2e")

        self.build_ui()

    def build_ui(self):

        title = tk.Label(self.root, text="Trigonometry Calculator",
                         font=("Arial", 18, "bold"),
                         bg="#1f1f2e", fg="white")
        title.pack(pady=10)

        self.create_ratio_section()
        self.create_standard_section()
        self.create_identity_section()

    # -------- Section 1 -------- #

    def create_ratio_section(self):
        frame = tk.LabelFrame(self.root, text="1. Ratios",
                              bg="#2c2c3c", fg="white")
        frame.pack(fill="x", padx=20, pady=10)

        self.angle_input = tk.Entry(frame)
        self.angle_input.pack(pady=5)

        self.operation = ttk.Combobox(frame, values=[
            "sin", "cos", "tan", "cosec", "sec", "cot"
        ])
        self.operation.pack(pady=5)

        tk.Button(frame, text="Calculate",
                  command=self.handle_ratio).pack(pady=5)

        self.result1 = tk.Label(frame, text="", bg="#2c2c3c", fg="white")
        self.result1.pack()

    def handle_ratio(self):
        try:
            angle = float(self.angle_input.get())
            op = self.operation.get()

            result = TrigonometryCalculator.calculate_ratio(angle, op)
            self.result1.config(text=f"Result: {result}")

        except:
            messagebox.showerror("Error", "Invalid Input")

    # -------- Section 2 -------- #

    def create_standard_section(self):
        frame = tk.LabelFrame(self.root, text="2. Standard Angles",
                              bg="#2c2c3c", fg="white")
        frame.pack(fill="x", padx=20, pady=10)

        self.degree = ttk.Combobox(frame, values=[0, 30, 45, 60, 90])
        self.degree.pack(pady=5)

        tk.Button(frame, text="Get Values",
                  command=self.handle_standard).pack(pady=5)

        self.result2 = tk.Label(frame, text="", bg="#2c2c3c", fg="white")
        self.result2.pack()

    def handle_standard(self):
        try:
            angle = int(self.degree.get())
            sin_v, cos_v, tan_v = TrigonometryCalculator.standard_values(angle)

            text = f"""
sin({angle}) = {round(sin_v, 3)}
cos({angle}) = {round(cos_v, 3)}
tan({angle}) = {tan_v}
"""
            self.result2.config(text=text)

        except:
            messagebox.showerror("Error", "Invalid Selection")

    # -------- Section 3 -------- #

    def create_identity_section(self):
        frame = tk.LabelFrame(self.root, text="3. Identity",
                              bg="#2c2c3c", fg="white")
        frame.pack(fill="x", padx=20, pady=10)

        self.identity_input = tk.Entry(frame)
        self.identity_input.pack(pady=5)

        tk.Button(frame, text="Check",
                  command=self.handle_identity).pack(pady=5)

        self.result3 = tk.Label(frame, text="", bg="#2c2c3c", fg="white")
        self.result3.pack()

    def handle_identity(self):
        try:
            angle = float(self.identity_input.get())

            if TrigonometryCalculator.verify_identity(angle):
                self.result3.config(text="✔ Verified: sin²θ + cos²θ = 1")
            else:
                self.result3.config(text="❌ Failed")

        except:
            messagebox.showerror("Error", "Invalid Input")


# ================= RUN ================= #

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
