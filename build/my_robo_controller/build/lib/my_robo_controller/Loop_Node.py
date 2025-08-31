#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from functools import partial

class TurtlesimLoopNode(Node):

    def __init__(self):
        super().__init__("turtle_loop")
        self.previous_x = 1
        self.turtle_publisher = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10
        )
        self.turtle_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10)
        
    def pose_callback(self, position: Pose):
        msg = Twist()
        if (position.x or position.y) > 9.0 or (position.x or position.y) < 2.0:
            msg.angular.z = 0.9
            msg.linear.x = 1.0
        else:
            msg.linear.x = 5.0
            msg.angular.z = 0.0

        self.turtle_publisher.publish(msg)
        if position.x >= 5.5 and self.previous_x == 1:
            self.previous_x = 0
            self.get_logger().info("Pen color set : Red")
            self.call_pen_service(255, 0, 0, 3, 0)
        elif position.x < 5.5 and self.previous_x == 0:
            self.previous_x = 1
            self.get_logger().info("Pen color set : Green")
            self.call_pen_service(0, 255, 0, 3, 0)

    def call_pen_service(self, r, g, b, width, off):
        client = self.create_client(SetPen, "/turtle1/set_pen")

        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for service")
        
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = TurtlesimLoopNode()
    rclpy.spin(node)
    rclpy.shutdown()