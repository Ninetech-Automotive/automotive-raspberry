from ObjectDetection.Camera import Camera
from picamera2 import Picamera2
import os
import cv2
import time
from flask import Flask, render_template, Response
from datetime import datetime

class RaspberryCamera(Camera):

    def __init__(self, camera_index=0):   
        self.camera_index = camera_index
        self.camera = Picamera2(camera_index)
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

    def start_streaming_server(self, host='0.0.0.0', port=5000):
        app = Flask(__name__)
        camera_instance = self

        def generate_frames():
            while True:
                frame = camera_instance.get_image_array()
                height, width, _ = frame.shape
                center_x = width // 2
                center_y = height // 2
                cv2.line(frame, (center_x, 0), (center_x, height), (0, 0, 255), 2)
                cv2.line(frame, (0, center_y), (width, center_y), (0, 0, 255), 2)
                _, buffer = cv2.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/video')
        def video():
            return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

        # Flask-Server in einem eigenen Thread starten, damit das Hauptprogramm nicht blockiert
        app.run(host=host, port=port)