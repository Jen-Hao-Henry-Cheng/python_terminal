from PySide6.QtWidgets import (QApplication, QMainWindow, QStatusBar,
                               QGridLayout, QGroupBox, QLabel,
                               QTextEdit, QPushButton)
from PySide6.QtGui import QAction
from PySide6.QtCore import QByteArray

from comport_dialog import ComportDialog
from serial_port import SerialPort

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ## Window
        self.setWindowTitle("Serial Terminal")
        self.resize(600, 400)
        
        ## Menu
        self.__set_menu_bar()

        ## Status Bar
        self.setStatusBar(QStatusBar(self))

        ## Central Widget
        groupBox = QGroupBox()       
        layout = QGridLayout()
        groupBox.setLayout(layout)
        self.setCentralWidget(groupBox)
        
        # Input Screen
        inputLabel = QLabel("Input")
        layout.addWidget(inputLabel, 0, 0)
        self.__input_screen = QTextEdit()
        layout.addWidget(self.__input_screen, 1, 0)
        # Send Button
        sendButton = QPushButton("Send")
        sendButton.clicked.connect(self.__send_message)
        layout.addWidget(sendButton, 0, 1)
        # Output Screen
        outputLabel = QLabel("Output")
        layout.addWidget(outputLabel, 2, 0)
        self.__output_screen = QTextEdit()
        self.__output_screen.setReadOnly(True)
        layout.addWidget(self.__output_screen, 3, 0)
        # Clear Button
        clearButton = QPushButton("Clear")
        clearButton.clicked.connect(self.__clear_output_screen)
        layout.addWidget(clearButton, 2, 1)

    def __set_menu_bar(self):
        # Comport action
        comport_action = QAction("COMPort", self)
        comport_action.setStatusTip("Comport setting")
        comport_action.triggered.connect(self.__open_setting_dialog)
        # Connect action
        connect_action = QAction("Connect", self)
        connect_action.triggered.connect(self.__open_serial)
        # Disconnect action
        disconnect_action = QAction("Disconnect", self)
        disconnect_action.triggered.connect(self.__close_serial)

        menu = self.menuBar()
        setting_menu = menu.addMenu("Setting")
        setting_menu.addAction(comport_action)
        setting_menu.addAction(connect_action)
        setting_menu.addAction(disconnect_action)

    def __open_setting_dialog(self):
        self.__comport_dialog = ComportDialog()
    
    def __open_serial(self):
        self.__serial = SerialPort(self.__comport_dialog.device_name, 
                                   self.__comport_dialog.baud)
        self.__serial.connect_read_callback(self.__show_message)
        self.__serial.open()
        # print log in status bar
        logMsg = "device name: " + self.__comport_dialog.device_name + ", baud: " + str(self.__comport_dialog.baud)
        self.statusBar().showMessage(logMsg)
        
    def __close_serial(self):
        self.__serial.close()
        # TODO disable dissconnect button and send button
        # print log in status bar
        logMsg = "device name: " + self.__comport_dialog.device_name + ", baud: " + str(self.__comport_dialog.baud) + " is closed"
        self.statusBar().showMessage(logMsg)

    def __show_message(self, output_message):
        self.__output_screen.setPlainText(output_message)
    
    def __send_message(self):
        message = self.__input_screen.toPlainText()
        self.__serial.write(QByteArray(message.encode()))
    
    def __clear_output_screen(self):
        self.__output_screen.clear()


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()