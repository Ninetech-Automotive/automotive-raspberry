from Communication.Receiver import Receiver
from Navigation.NavigationController import NavigationController
from CommunciationInterface import CommunciationInterface


class RaspberryReceiver(Receiver):

    def __init__(self, controller: NavigationController, interface: CommunciationInterface):
        self.interface = interface
        self.controller = controller
        self.messageHandlers = {
            "pong": self.controller.on_pong,
            "on_waypoint": self.controller.on_waypoint,
            "angle": self.controller.on_angle,
            "point_scanning_finished": self.controller.on_point_scanning_finished,
            "turned_to_target_line": self.controller.on_turned_to_target_line,
            "cone_detected": self.controller.on_cone_detected,
            "obstacle_detected": self.controller.on_obstacle_detected,
        }

    def __on_receive(self, message):
        if ":" in message:
            message, value = message.split(":")
            self.messageHandlers[message](float(value))
        else:
            self.messageHandlers[message]()

    def receive(self):
        message = self.interface.read()
        if message:
            self.__on_receive(message)
