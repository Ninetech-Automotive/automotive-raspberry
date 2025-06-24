import serial
from CommunicationInterface import CommunicationInterface
from Configuration.Configurator import Configurator

class SerialInterface(CommunicationInterface):
    def __init__(self):
        device = Configurator().get_communication()["device"]
        baud = Configurator().get_communication()["baud"]
        self.serial = serial.Serial(device, baudrate=baud, timeout=1)

    def write(self, message):
        if not message.endswith('\n'):
            message += '\n'
        self.serial.write(message.encode())

    def read(self):
        return self.serial.readline().decode('utf-8', errors='ignore').replace('\x00', '').strip()