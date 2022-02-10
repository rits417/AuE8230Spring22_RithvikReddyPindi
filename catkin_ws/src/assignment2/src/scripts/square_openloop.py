#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI= 3.1415926535897
x = 0
def move():

    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print('Lets make the turtlesim make a square')
    x = 1
    while(x<10):

        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        vel_msg.linear.x = 0.2
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        t0 = rospy.Time.now().to_sec()
        distance = 0

        while(distance < 2):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            distance= 0.2*(t1-t0)

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0.2
        ta =  rospy.Time.now().to_sec()
        angle = 0
        while(angle<1.57):
            velocity_publisher.publish(vel_msg)
            tb=rospy.Time.now().to_sec()
            angle= 0.2*(tb-ta)
        vel_msg.angular.z = 0
        x = x+1
        #Making the robot stop
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass


