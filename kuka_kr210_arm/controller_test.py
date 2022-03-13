#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
 
 
class Trajectory_publisher(Node): 
    def __init__(self):
        super().__init__("trajectory_publisher_node")
        publish_topic = "/joint_trajectory_controller/joint_trajectory"
        self.trajectory_publisher_ = self.create_publisher(JointTrajectory,publish_topic,10)
        timer_period = 1
        self.timer_ = self.create_timer(timer_period,self.timer_callback)
        self.joints_ = ['joint_1','joint_2','joint_3','joint_4','joint_5','joint_6','right_gripper_finger_joint','left_gripper_finger_joint']
        self.goal_positions_ = [0.5,0.5,0.5,0.5,0.5,0.5,0.0,0.0]
        #self.goal_positions_ = [-2.57, 1.59, 1.6]

    def timer_callback(self):
        msg = JointTrajectory()
        msg.joint_names = self.joints_
        point = JointTrajectoryPoint()
        point.positions = self.goal_positions_
        point.time_from_start = Duration(sec=2)
        msg.points.append(point)
        self.trajectory_publisher_.publish(msg)
 
 
def main(args=None):
    rclpy.init(args=args)
    node = Trajectory_publisher() 
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()