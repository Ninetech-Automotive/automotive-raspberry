from Communication.Receiver import Receiver
from Navigation.NavigationController import NavigationController
from CommunicationInterface import CommunicationInterface

class RaspberryReceiver(Receiver):

    def __init__(self, controller: NavigationController, interface: CommunicationInterface):
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
            "set_target": self.controller.on_set_target,
            "line_missing": self.controller.on_line_missing,
            "stop": self.controller.on_stop,
        }

    def __on_receive(self, message):
        print(f"[uc->pi]{message}")
        if ":" in message:
            message, value = message.split(":")
            try:
                num_value = float(value)
                self.messageHandlers[message](num_value)
            except ValueError:
                self.messageHandlers[message](value)
        else:
            self.messageHandlers[message]()

    def receive(self):
        message = self.interface.read()
        if message:
            self.__on_receive(message)
