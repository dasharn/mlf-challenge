import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import Canvas
import json
from c3po import C3PO

class C3POApp:
    def __init__(self, root):
        self.root = root
        self.root.title("C3PO Navigation System")
        
        # Frame for file uploads
        self.upload_frame = ttk.Frame(root, padding="10")
        self.upload_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.mf_file_label = ttk.Label(self.upload_frame, text="Millennium Falcon JSON:")
        self.mf_file_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.mf_file_button = ttk.Button(self.upload_frame, text="Select File", command=self.load_mf_file)
        self.mf_file_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.empire_file_label = ttk.Label(self.upload_frame, text="Empire JSON:")
        self.empire_file_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.empire_file_button = ttk.Button(self.upload_frame, text="Select File", command=self.load_empire_file)
        self.empire_file_button.grid(row=1, column=1, padx=5, pady=5)
        
        self.calculate_button = ttk.Button(self.upload_frame, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        
        # Frame for results
        self.results_frame = ttk.Frame(root, padding="10")
        self.results_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        self.result_label = ttk.Label(self.results_frame, text="Maximum Probability of Success:")
        self.result_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.result_value = ttk.Label(self.results_frame, text="N/A")
        self.result_value.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Initialize variables
        self.mf_file_path = None
        self.empire_file_path = None
        self.c3po = None
    
    def load_mf_file(self):
        self.mf_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.mf_file_path:
            self.mf_file_label.config(text=f"Millennium Falcon JSON: {self.mf_file_path.split('/')[-1]}")
    
    def load_empire_file(self):
        self.empire_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.empire_file_path:
            self.empire_file_label.config(text=f"Empire JSON: {self.empire_file_path.split('/')[-1]}")
    
    def calculate(self):
        if not self.mf_file_path or not self.empire_file_path:
            messagebox.showerror("Error", "Please select both files.")
            return
        
        try:
            self.c3po = C3PO(self.mf_file_path)
            probability = self.c3po.giveMeTheOdds(self.empire_file_path)
            self.result_value.config(text=f"{probability:.4f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
app = C3POApp(root)
root.mainloop()
