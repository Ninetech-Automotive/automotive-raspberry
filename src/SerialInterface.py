import serial
from CommunciationInterface import CommunicationInterface
from Configuration.Configurator import Configurator

class SerialInterface(CommunicationInterface):
    def __init__(self):
        configurator = Configurator()
        device = configurator.get_communication()["device"]
        baud = configurator.get_communication()["baud"]
        self.serial = serial.Serial(device, baudrate=baud, timeout=1)

    def write(self, message):
        self.serial.write(message.encode())

    def read(self):
        return self.serial.readline().decode('utf-8', errors='ignore').strip()