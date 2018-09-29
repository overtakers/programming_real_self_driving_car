from styx_msgs.msg import TrafficLight
import rospy

import tensorflow as tf
import cv2
import sys
import os

# from traffic_light_classifier.nets import inception_v4
# from traffic_light_classifier.preprocessing import inception_preprocessing

# from traffic_light_classifier.nets.tl_model import TLModel
import time
import glob

class TLClassifier(object):
#    def __init__(self):
#        #TODO load classifier
#        ckpt_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'traffic_light_classifier'))
#        modelPath = os.path.join(ckpt_path, "logs/deploy/graph_optimized.pb")
#        # rospy.loginfo("path: %s", modelPath)
#
#        with tf.gfile.GFile(modelPath, 'rb') as f:
#            graph_def_optimized = tf.GraphDef()
#            graph_def_optimized.ParseFromString(f.read())
#
#        G = tf.Graph()
#        self.sess = tf.InteractiveSession(graph=G)
#        tf.import_graph_def(graph_def_optimized, name='')
#        self.predictions = G.get_tensor_by_name('predictions:0')
#        self.img_input = G.get_tensor_by_name('inputs:0')

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
#        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#        pred = self.sess.run(self.predictions,
#             feed_dict={ self.img_input: image})
#
#       return pred[0]
        return TrafficLight.UNKNOWN
