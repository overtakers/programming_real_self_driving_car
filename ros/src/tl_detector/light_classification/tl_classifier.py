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

    def __init__(self):
        graph_file = "frozen_inference_graph.pb"
        self.graph = tf.Graph()
        with graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(graph_file, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        # `get_tensor_by_name` returns the Tensor with the associated name in the Graph.
        self.image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

        # The classification of the object (integer id).
        self.detection_classes = self.graph.get_tensor_by_name('detection_classes:0')
        self.sess = tf.InteractiveSession(graph=self.graph)

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#        pred = self.sess.run(self.predictions,
#             feed_dict={ self.img_input: image})
#
#       return pred[0]
        


        classes = self.sess.run(self.detection_classes, feed_dict={self.image_tensor: image})
        confidence_class = int(classes[0])
        if confidence_class == 1:
            return TrafficLight.GREEN
        if confidence_class == 2:
            return TrafficLight.RED
        if confidence_class == 3:
            return TrafficLight.YELLOW

        return TrafficLight.UNKNOWN
