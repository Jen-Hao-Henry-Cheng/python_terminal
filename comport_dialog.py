import tkinter as tk

class ComportDialog:
    def __init__(self):
        self.dialog = tk.Toplevel()
        
        # close button
        self.closeButton = tk.Button(self.dialog, text="Close", command=self.close_dialog)
        self.closeButton.grid(row=0,column=0)

    def close_dialog(self):
        self.dialog.destroy()