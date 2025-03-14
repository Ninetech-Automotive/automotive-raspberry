from Communication.Emitter import Emitter

class RaspberryEmitter(Emitter):

    def emit(self, message):
        # dummy implementation
        print("emit:", message)
