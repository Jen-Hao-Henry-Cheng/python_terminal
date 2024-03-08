import tkinter as tk

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Hello world')
        self.window.geometry('380x400')
        self.window.resizable(False, False)

        self.label = tk.Label(text="my label", font=("Arial", 14, "bold"), padx=5, pady=5, bg="red", fg="yellow")
        self.label.grid(row=2,column=2)

        self.button = tk.Button(text="Click Me", font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="light green", command=self.button_clicked)
        self.button.grid(row=3,column=2)

        self.window.mainloop()

    def button_clicked(self):
        self.label.config(text="Hello World!")






if __name__ == '__main__':
    MainWindow()