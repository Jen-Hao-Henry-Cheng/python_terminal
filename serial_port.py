import serial
import threading

class SerialPort:
    def __init__(self, device_name, baud):
        self.serial = serial.Serial()
        self.serial.port = device_name
        self.serial.baudrate = baud

    def set_data_received_func(self, func):
        self.data_handler = func

    def open(self):
        self.serial.open()
        self.readThreadEnable = True
        self.create_read_thread()

    def close(self):
        if self.serial.isOpen():
            self.readThreadEnable = False
            self.serial.close()

    def create_read_thread(self):
        self.readThread = threading.Thread(target = self.read_loop)
        self.readThread.start()

    def read_loop(self):
        while self.readThreadEnable:
            if self.serial.in_waiting:
                data_raw = self.serial.readline()
                print(f'data type: {type(data_raw)}')
                print(f'data: {data_raw}')

    def write(self, message):
        self.serial.write(message)