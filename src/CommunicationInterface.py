from abc import ABC, abstractmethod

class CommunicationInterface(ABC):
    @abstractmethod
    def write(self, message):
        pass

    @abstractmethod
    def read(self):
        pass