#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("Draw_circle")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(0.5, self.vel_pub)
        self.get_logger().info("code executed")

    def vel_pub(self):
        vel = Twist()
        vel.linear.x = 2.0
        vel.angular.z = 1.0
        self.cmd_vel_pub.publish(vel)


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()
    