#!/usr/bin/env python

from simulation_only_msgs.msg import DeltaTrajectoryWithID
import time
import rospy
import unittest
import sys
PKG = "simulation_initialization_ros_tool"


class Listener:
    """
    Can be used to block and wait for a message
    """

    def __init__(self, topic, msg):
        """
        Create a Listener
        :param topic: string: name of the topic
        :param msg: message object for this topic
        """
        self.subscriber = rospy.Subscriber(topic, msg, self._on_message, queue_size=5)

    def wait_for_message(self, timeout=rospy.Duration(20)):
        """
        Blocks until a message is received on the subscribed topic or timeout is reached
        :param timeout: Duration: maximum time to wait
        :return: message, if received - otherwise None
        """
        self.msg = None
        waitcount = 0
        while waitcount < 20 and not self.msg and not rospy.is_shutdown():
            waitcount += 1
            time.sleep(timeout.to_sec() / 20.)
        return self.msg

    def _on_message(self, msg):
        self.msg = msg


class TestPlannerOutput(unittest.TestCase):

    def test_if_desired_motion_published(self):

        topic = rospy.get_param("~desired_motion_topic")

        listener = Listener(topic, DeltaTrajectoryWithID)
        msg = listener.wait_for_message()
        self.assertIsNotNone(msg, "Did not receive message on topic \"" + topic + "\"")


if __name__ == '__main__':
    import rostest

    rospy.init_node('whole_framework_test')
    rostest.rosrun(PKG, 'simulation_initialization_ros_tool', TestPlannerOutput)
