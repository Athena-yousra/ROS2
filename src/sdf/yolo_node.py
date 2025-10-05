import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO

class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.bridge = CvBridge()

        # Subscribe to camera topic
        self.subscription = self.create_subscription(
            Image, '/camera', self.listener_callback, 10)

        # Load your YOLO11n trained model
        self.model = YOLO("/home/yousra/Downloads/CRTI/CRTI/src/Code/best.pt")  # change path if needed

        self.get_logger().info("✅ YOLO11n node started, waiting for /camera frames...")

    def listener_callback(self, msg):
        # Convert ROS Image to OpenCV
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Run YOLO prediction
        results = self.model(frame, verbose=False)

        # Draw results on frame
        annotated_frame = results[0].plot()

        # Show detections in a window
        cv2.imshow("YOLO11n Detection", annotated_frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = YoloNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
