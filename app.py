import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import Canvas
import json
from c3po import C3PO

class C3POApp:
    """
    C3PO Navigation System application.

    This class creates a GUI application for navigating the Millennium Falcon
    and the Empire's JSON data, allowing file uploads and calculations.
    """

    def __init__(self, root):
        """
        Initialize the C3POApp.

        Parameters:
        root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("C3PO Navigation System")

        self.mf_file_path = None
        self.empire_file_path = None
        self.c3po = None

        self.setup_ui()

    def setup_ui(self):
        """
        Set up the user interface by creating the necessary frames and widgets.
        """
        self.create_upload_frame()
        self.create_results_frame()

    def create_upload_frame(self):
        """
        Create the frame for file uploads, including labels and buttons for
        selecting files and calculating results.
        """
        self.upload_frame = ttk.Frame(self.root, padding="10")
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

    def create_results_frame(self):
        """
        Create the frame for displaying results, including a label to show
        the maximum probability of success.
        """
        self.results_frame = ttk.Frame(self.root, padding="10")
        self.results_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.result_label = ttk.Label(self.results_frame, text="Maximum Probability of Success:")
        self.result_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.result_value = ttk.Label(self.results_frame, text="N/A")
        self.result_value.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    
    def load_mf_file(self):
        """
        Open a file dialog to select the Millennium Falcon JSON file and update the label with the selected file's name.

        This method updates `self.mf_file_path` with the path of the selected file and changes the label
        text to display the file name. It only updates the label if a file is successfully selected.
        """
        self.mf_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.mf_file_path:
            self.mf_file_label.config(text=f"Millennium Falcon JSON: {self.mf_file_path.split('/')[-1]}")
    
    def load_empire_file(self):
        """
        Open a file dialog to select the Empire JSON file and update the label with the selected file's name.

        This method updates `self.empire_file_path` with the path of the selected file and changes the label
        text to display the file name. It only updates the label if a file is successfully selected.
        """
        self.empire_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.empire_file_path:
            self.empire_file_label.config(text=f"Empire JSON: {self.empire_file_path.split('/')[-1]}")
    
    def calculate(self):
        """
        Perform calculations based on the loaded JSON files and update the results display.

        This method first checks if both file paths are selected. If not, it shows an error message. If both
        files are selected, it attempts to create an instance of the `C3PO` class using the Millennium Falcon
        JSON file, then calculates the probability of success using the Empire JSON file. The result is displayed
        with four decimal places. If any error occurs during this process, an error message is shown.
        """
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
