from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QIODevice

class SerialPort:
    def __init__(self, device_name, baud):
        self.__serial = QSerialPort()
        self.__serial.setPortName(device_name)
        self.__serial.setBaudRate(baud)
        self.__serial.readyRead.connect(self.__handle_read)

    def open(self):
        self.__serial.open(QIODevice.ReadWrite)

    def close(self):
        if self.__serial.isOpen():
            self.__serial.close()

    def write(self, message):
        self.__serial.write(message)

    def connect_read_callback(self, function):
        self.__read_callback = function

    def __handle_read(self):
        rx_bytes_amount = self.__serial.bytesAvailable()
        rx_bytes = self.__serial.read(rx_bytes_amount)
        self.__read_callback(str(rx_bytes))
