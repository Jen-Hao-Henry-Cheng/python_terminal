import tkinter as tk
import serial_port
import comport_dialog

class MainWindow:
    def __init__(self):
        # Window
        self.window = tk.Tk()
        self.window.title('Serial Terminal')
        self.window.geometry('380x400')
        self.window.resizable(False, False)

        # Menu
        self.menu = tk.Menu()
        self.window.config(menu=self.menu)
        self.subMenuSetting = tk.Menu(activebackground="green", tearoff=0)
        self.menu.add_cascade(label="Setting", menu=self.subMenuSetting)
        self.subMenuSetting.add_command(label="COMPort", command=self.open_setting_dialog)
        self.subMenuSetting.add_command(label="Connect", command=self.open_serial)
        self.subMenuSetting.add_command(label="Disconnect", command=self.close_serial)

        # status Bar
        self.statusBar = tk.Label(text='status bar', bd=1, anchor=tk.W)
        self.statusBar.pack(side="bottom", fill="x")

        # Input
        self.inputFrame = tk.Frame()
        self.inputFrame.pack(side="top", fill="x")
        self.inputLabel = tk.Label(self.inputFrame, text='Input', anchor=tk.W)
        self.inputLabel.grid(row=0, column=0)
        self.inputTextBox = tk.Text(self.inputFrame, height=5, width=30, state=tk.NORMAL)
        self.inputTextBox.grid(row=1, column=0)
        self.sendButton = tk.Button(self.inputFrame, text="Send", state=tk.DISABLED,
                                    command=self.send_message)
        self.sendButton.grid(row=1, column=1)

        # Output
        self.outputFrame = tk.Frame()
        self.outputFrame.pack(side="top", fill="x")
        self.outputLabel = tk.Label(self.outputFrame, text='Output', anchor=tk.W)
        self.outputLabel.grid(row=0, column=0)
        self.outputTextBox = tk.Text(self.outputFrame, height=5, width=30, state=tk.DISABLED)
        self.outputTextBox.grid(row=1, column=0)


        self.window.mainloop()

    def open_setting_dialog(self):
        self.setting_dialog = comport_dialog.ComportDialog()
    
    def open_serial(self):
        self.serial = serial_port.SerialPort(self.setting_dialog.device_name, 
                                             self.setting_dialog.baud)
        self.serial.open()
        self.sendButton.config(state=tk.NORMAL) # enable the send button
        # print log in status bar
        self.statusBar.config(text="device name: " + self.setting_dialog.device_name + ", baud: " + str(self.setting_dialog.baud))
    
    def close_serial(self):
        self.serial.close()
        self.sendButton.config(state=tk.DISABLED) # disable the send button
        # print log in status bar
        self.statusBar.config(text="device name: " + self.setting_dialog.device_name + ", baud: " + str(self.setting_dialog.baud) + " is closed")

    def send_message(self):
        message = self.inputTextBox.get("1.0", "end-1c")
        self.statusBar.config(text="message: " + message)


if __name__ == '__main__':
    MainWindow()