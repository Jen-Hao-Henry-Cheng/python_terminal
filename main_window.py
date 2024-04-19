from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar
from PySide6.QtGui import QAction

# import comport_dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle("Serial Terminal")
        self.resize(600, 400)
        
        # Menu
        self.__set_menu_bar()

        # Status Bar
        self.setStatusBar(QStatusBar(self))

    def __set_menu_bar(self):

        comport_action = QAction("COMPort", self)
        comport_action.setStatusTip("Comport setting")
        comport_action.triggered.connect(self.__open_setting_dialog)

        connect_action = QAction("Connect", self)
        disconnect_action = QAction("Disconnect", self)

        menu = self.menuBar()
        setting_menu = menu.addMenu("Setting")
        setting_menu.addAction(comport_action)
        setting_menu.addAction(connect_action)
        setting_menu.addAction(disconnect_action)

    def __open_setting_dialog(self):
        self.statusBar().showMessage("Open setting dialog")
    #     self.setting_dialog = comport_dialog.ComportDialog()
    
    # def open_serial(self):
    #     self.serial = serial_port.SerialPort(self.setting_dialog.device_name, 
    #                                          self.setting_dialog.baud)
    #     self.serial.open()
    #     self.sendButton.config(state=tk.NORMAL) # enable the send button
    #     # print log in status bar
    #     self.statusBar.config(text="device name: " + self.setting_dialog.device_name + ", baud: " + str(self.setting_dialog.baud))
    
    # def close_serial(self):
    #     self.serial.close()
    #     self.sendButton.config(state=tk.DISABLED) # disable the send button
    #     # print log in status bar
    #     self.statusBar.config(text="device name: " + self.setting_dialog.device_name + ", baud: " + str(self.setting_dialog.baud) + " is closed")

    # def send_message(self):
    #     message = self.inputTextBox.get("1.0", "end-1c")
    #     self.statusBar.config(text="message: " + message)


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()