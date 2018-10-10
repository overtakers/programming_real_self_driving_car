from styx_msgs.msg import TrafficLight
import rospy

import tensorflow as tf
import datetime
import numpy as np
import cv2
import sys
import os

import time
import glob

class TLClassifier(object):
    def __init__(self, is_simulator):
	if is_simulator:
        	#GRAPH_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'traffic_light_classifier/model/sim/frozen_inference_graph.pb'))
		GRAPH_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "SSD_Inception_V2_Coco_sim.pb"))
                
#                GRAPH_PATH = "./SSD_Inception_V2_Coco_sim.pb"
                self.graph = tf.Graph()

        	self.prev_list_state = TrafficLight.RED

        	with self.graph.as_default():
            		od_graph_def = tf.GraphDef()
           		with tf.gfile.GFile(GRAPH_PATH, 'rb') as fid:
                		od_graph_def.ParseFromString(fid.read())
                		tf.import_graph_def(od_graph_def, name='')

            	self.image_tensor = self.graph.get_tensor_by_name('image_tensor:0')
            	self.boxes = self.graph.get_tensor_by_name('detection_boxes:0')
            	self.scores = self.graph.get_tensor_by_name('detection_scores:0')
            	self.classes = self.graph.get_tensor_by_name('detection_classes:0')
            	self.num_detections = self.graph.get_tensor_by_name(
                	'num_detections:0')

        	self.sess = tf.Session(graph=self.graph)
	else: # car model to be used
            rospy.loginfo("is_simulator=False")
    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        if not self.graph: #used to test is_simulator
            return  TrafficLight.UNKNOWN


        with self.graph.as_default():
            img_expand = np.expand_dims(image, axis=0)
            start = datetime.datetime.now()
            (boxes, scores, classes, num_detections) = self.sess.run(
                [self.boxes, self.scores, self.classes, self.num_detections],
                feed_dict={self.image_tensor: img_expand})
            end = datetime.datetime.now()
            c = end - start

        boxes = np.squeeze(boxes)
        scores = np.squeeze(scores)
        classes = np.squeeze(classes).astype(np.int32)

        print("=====================")
        print("Time Cost:   {time:.4f} s".format(time=c.total_seconds()))
        print('Scores:      {score:.6f}'.format(score=scores[0]))
        print('Classes:     {classes}'.format(classes=classes[0]))
        
        if scores[0] > 0.15:
            if classes[0] == 1:
                print('Light State: GREEN')
                self.prev_list_state = TrafficLight.GREEN
                return TrafficLight.GREEN
            elif classes[0] == 2:
                print('Light State: RED')
                self.prev_list_state = TrafficLight.RED
                return TrafficLight.RED
            elif classes[0] == 3:
                print('Light State: YELLOW')
                self.prev_list_state = TrafficLight.YELLOW
                return TrafficLight.YELLOW
        print('Light State: UNKNOWN')
        return self.prev_list_state if self.prev_list_state != TrafficLight.GREEN else TrafficLight.UNKNOWN
