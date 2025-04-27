import sys
sys.path.insert(1, './src/Core/src')
from Communication.Emitter import Emitter
from Communication.Receiver import Receiver
from ObjectDetection.ObjectDetector import ObjectDetector
from ObjectDetection.YOLODetector import YOLODetector
from ObjectDetection.Camera import Camera
from RaspberryCamera import RaspberryCamera
from Navigation.NavigationController import NavigationController
from RaspberryEmitter import RaspberryEmitter
from RaspberryReceiver import RaspberryReceiver
from Configuration.Configurator import Configurator
from pathlib import Path


def main():
    Configurator.initialize(Path("src/config.json"))
    camera: Camera = RaspberryCamera()
    object_detector: ObjectDetector = YOLODetector(camera)
    emitter: Emitter = RaspberryEmitter()
    navigation_controller = NavigationController(emitter, object_detector)
    receiver: Receiver = RaspberryReceiver(navigation_controller)

    while True:
        receiver.receive()

if __name__ == "__main__":
    main()