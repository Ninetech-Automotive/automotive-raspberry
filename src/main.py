#! /home/remote/automotive-raspberry/.venv/bin/python3

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
from SerialInterface import SerialInterface
from CommunicationInterface import CommunicationInterface
from pathlib import Path


def main():
    Configurator.initialize(Path("src/config.json"))
    top_camera: Camera = RaspberryCamera(0)
    bottom_camera: Camera = RaspberryCamera(1)
    object_detector: ObjectDetector = YOLODetector(top_camera, bottom_camera)
    communication_interface: CommunicationInterface = SerialInterface()
    emitter: Emitter = RaspberryEmitter(communication_interface)
    navigation_controller = NavigationController(emitter, object_detector)
    receiver: Receiver = RaspberryReceiver(navigation_controller, communication_interface)

    while True:
        receiver.receive()

def start_streaming_server():
    camera: Camera = RaspberryCamera(1)
    camera.enable()
    camera.start_streaming_server()


if __name__ == "__main__":
    main()
    start_streaming_server()