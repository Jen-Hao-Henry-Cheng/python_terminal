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

        # status Bar
        self.statusBar = tk.Label(text='status bar', bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side="bottom", fill="x")

        self.button = tk.Button(text="Click Me", font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="light green", command=self.button_clicked)
        self.button.pack(side="top")

        self.window.mainloop()

    def open_setting_dialog(self):
        self.setting_dialog = comport_dialog.ComportDialog()

    def button_clicked(self):
        self.statusBar.config(text="device name: " + self.setting_dialog.device_name + ", baud: " + str(self.setting_dialog.baud))






if __name__ == '__main__':
    MainWindow()