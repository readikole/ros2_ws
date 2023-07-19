#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
     
     
class NumberCounterNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("number_counter") # MODIFY NAME
        self.counter_=0
        self.number_subscriber_ = self.create_subscription(
            Int64, "number", self.callback_number, 10)
        self.get_logger().info("Number Counter has been started.")
    
    def callback_number(self, msg):
        self.counter_+=msg.data
        self.get_logger().info(str(self.counter_))
     
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()