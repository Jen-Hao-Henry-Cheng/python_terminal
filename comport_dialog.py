import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

class ComportDialog:
    def __init__(self):
        self.device_name = "" # device name
        self.baud = 9600 # baud rate

        self.dialog = tk.Toplevel()
        self.dialog.title("COM Port")

        # Lables
        self.deviceLabel = tk.Label(self.dialog, text="Port")
        self.deviceLabel.grid(row=0,column=0)
        self.baudLabel = tk.Label(self.dialog, text="Baud")
        self.baudLabel.grid(row=2,column=0)

        # Device List
        self.deviceList = ttk.Combobox(self.dialog, state="readonly")
        self.deviceList.grid(row=0,column=1)
        self.deviceList.bind("<<ComboboxSelected>>", self.select_device)
        self.refresh_comports() # init device list

        # Refresh button
        self.refreshButton = tk.Button(self.dialog, text="Refresh", command=self.refresh_comports)
        self.refreshButton.grid(row=1,column=0,columnspan=2)

        # Baud list
        self.baudList = ttk.Combobox(self.dialog,
                                     state="readonly",
                                     values=["9600", "115200"])
        self.baudList.grid(row=2,column=1)
        self.baudList.bind("<<ComboboxSelected>>", self.select_baud)

        # close button
        self.closeButton = tk.Button(self.dialog, text="Close", command=self.close_dialog)
        self.closeButton.grid(row=3,column=0,columnspan=2)

    # SLOT methods
    def refresh_comports(self):
        ports = list(serial.tools.list_ports.comports()) # get current devices
        devices = []
        for port in ports:
            devices.append(port.device)
        self.deviceList['values'] = devices
    
    def select_device(self, event):
        self.device_name = self.deviceList.get()
    
    def select_baud(self, event):
        selected_baud = self.baudList.get()
        if selected_baud == "9600":
            self.baud = 9600
        elif selected_baud == "115200":
            self.baud = 115200

    def close_dialog(self):
        self.dialog.destroy()