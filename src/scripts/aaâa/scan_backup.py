import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class QRDetectorNode(Node):
    def __init__(self):
        super().__init__('qr_detector_node')
        self.bridge = CvBridge()
        self.sub = self.create_subscription(Image, '/image_raw', self.image_callback, 10)
        self.pub_debug = self.create_publisher(Image, '/qr_debug', 10)
        self.detector = cv2.QRCodeDetector()
        self.get_logger().info("✅ OpenCV QR Node started — waiting for /image_raw frames")

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        data, points, _ = self.detector.detectAndDecode(frame)
        if points is not None:
            points = points[0].astype(int)
            cv2.polylines(frame, [points], True, (0, 255, 0), 2)
            if data:
                cv2.putText(frame, data, (points[0][0], points[0][1]-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                self.get_logger().info(f"📷 QR Detected: {data}")

        self.pub_debug.publish(self.bridge.cv2_to_imgmsg(frame, encoding='bgr8'))

def main(args=None):
    rclpy.init(args=args)
    node = QRDetectorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

