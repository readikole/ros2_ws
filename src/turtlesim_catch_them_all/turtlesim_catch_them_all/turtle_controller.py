#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from my_robot_interfaces.msg import Turtle
from my_robot_interfaces.msg import TurtleArray

class TurleControllerNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("turtle_controller") # MODIFY NAME
        self.turtle_to_catch_ = None
        self.pose_ = None
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(
            Pose, "turtle1/pose", self.callback_turtle_pose, 10)
        self.alive_turtles_subscriber_ = self.create_subscription(
            TurtleArray, "alive_turtles", self.callback_alive_turtles, 10)
        self.control_loop_timer_ = self.create_timer(0.01 ,self.control_loop)
         
    def callback_turtle_pose(self, msg):
        self.pose_ = msg
    
    def callback_alive_turtles(self, msg):
        if len(msg.turtles)>0:
            self.turtle_to_catch_ = msg.turtles[0]


    def control_loop(self):
        
        if self.pose_==None  or self.turtle_to_catch_== None:
            return
        
        dist_x = self.turtle_to_catch_.x - self.pose_.x
        dist_y = self.turtle_to_catch_.y - self.pose_.y
        distance = math.sqrt(dist_x*dist_x + dist_y*dist_y)
        msg = Twist()

        if distance >0.5:
            #position
            msg.linear.x = 2*distance
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta
            if diff>math.pi:
                diff -=2*math.pi
            elif diff < -math.pi:
                dif +=2*math.pi
            msg.angular.z = 6*diff
        else:
            msg.linear.x=0.0
            msg.angular.z = 0.0
        self.cmd_vel_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurleControllerNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
