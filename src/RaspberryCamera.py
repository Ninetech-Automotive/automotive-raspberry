from ObjectDetection.Camera import Camera
from picamera2 import Picamera2
import os
from datetime import datetime

class RaspberryCamera(Camera):

    def __init__(self, camera_index=0):   
        self.camera = Picamera2(0)
        self.camera.preview_configuration.main.format = "RGB888"
        self.camera.preview_configuration.main.size = (1920, 1080)

    def enable(self):
        self.camera.start()

    def disable(self):
        self.camera.stop()

    def get_width(self):
        return self.camera.preview_configuration.main.size[0]

    def get_height(self):
        return self.camera.preview_configuration.main.size[1]

    def get_image_array(self):
        return self.camera.capture_array()

    def capture_and_save_image(self):
        output_dir = "test_images"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(output_dir, f"image_{timestamp}.jpg")
        self.camera.capture_file(file_path)