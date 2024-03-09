import tkinter as tk

import comport_dialog

class MainWindow:
    def __init__(self):
        # Window
        self.window = tk.Tk()
        self.window.title('Hello world')
        self.window.geometry('380x400')
        self.window.resizable(False, False)

        # Menu
        self.menu = tk.Menu()
        self.window.config(menu=self.menu)
        self.subMenuSetting = tk.Menu(activebackground="green", tearoff=0)
        self.menu.add_cascade(label="Setting", menu=self.subMenuSetting)
        self.subMenuSetting.add_command(label="COMPort", command=self.open_setting_dialog)
        self.subMenuSetting.add_command(label="Connect")
        self.subMenuSetting.add_command(label="Disconnect")

        self.label = tk.Label(text="my label", font=("Arial", 14, "bold"), padx=5, pady=5, bg="red", fg="yellow")
        self.label.grid(row=2,column=2)

        self.button = tk.Button(text="Click Me", font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="light green", command=self.button_clicked)
        self.button.grid(row=3,column=2)

        self.window.mainloop()

    def open_setting_dialog(self):
        self.setiing_dialog = comport_dialog.ComportDialog()

    def button_clicked(self):
        self.label.config(text="Hello World!")






if __name__ == '__main__':
    MainWindow()