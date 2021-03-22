#!/usr/bin/env python
import rospy
from my_pkg.msg import two_ints
from std_msgs.msg import Int16

sum=Int16()
 
def callback(msg):
    rospy.loginfo("a+b=%d", msg.a + msg.b)
    sum =msg.a + msg.b
def listener():
    rospy.init_node('two_ints_subscriber', anonymous=True)
    rospy.Subscriber("two_ints", two_ints, callback)
    pub = rospy.Publisher("sum", Int16, queue_size=1)
    r=rospy.Rate(1)
    while not rospy.is_shutdown():
      pub.publish(sum)
      
# spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
