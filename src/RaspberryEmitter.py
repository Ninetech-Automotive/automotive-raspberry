from Communication.Emitter import Emitter
from CommunicationInterface import CommunicationInterface

class RaspberryEmitter(Emitter):

    def __init__(self, interface: CommunicationInterface):
        self.interface = interface

    def emit(self, message):
        self.interface.write(message)
