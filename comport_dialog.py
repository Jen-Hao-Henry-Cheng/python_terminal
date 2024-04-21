from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QComboBox, QPushButton
from PySide6.QtSerialPort import QSerialPortInfo

class ComportDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.device_name = "" # device name
        self.baud = 9600 # baud rate

        self.setWindowTitle("COM Port")

        # Layout
        self.__layout = QGridLayout()
        self.setLayout(self.__layout)

        ## Device selection
        # device label
        deviceLabel = QLabel("Port")
        self.__layout.addWidget(deviceLabel, 0, 0)
        # device combo
        self.__device_combo = QComboBox()
        self.__device_combo.currentTextChanged.connect(self.__select_device)
        self.__layout.addWidget(self.__device_combo, 0, 1)
        # refresh button
        refreshButton = QPushButton("Refresh")
        refreshButton.clicked.connect(self.__refresh_comports)
        self.__layout.addWidget(refreshButton, 1, 1)

        ## Baud selection
        # Baud label
        baudLabel = QLabel("Baud")
        self.__layout.addWidget(baudLabel, 2, 0)
        # Baud combobox
        self.__baud_combo = QComboBox()
        self.__baud_combo.addItems(["9600", "38400", "115200"])
        self.__baud_combo.currentTextChanged.connect(self.__select_baud)
        self.__layout.addWidget(self.__baud_combo, 2, 1)

        ## Init
        self.__refresh_comports()

        ## exec
        self.exec()

    # SLOT methods
    def __refresh_comports(self):
        serialPortInfos = QSerialPortInfo.availablePorts()
        self.__device_combo.clear()
        for portInfo in serialPortInfos:
            self.__device_combo.addItem(portInfo.portName())
    
    def __select_device(self, deviceText):
        self.device_name = deviceText
        print(f'Device: {self.device_name}')

    def __select_baud(self, baudText):
        baudText
        if baudText == "9600":
            self.baud = 9600
        if baudText == "38400":
            self.baud = 38400
        elif baudText == "115200":
            self.baud = 115200