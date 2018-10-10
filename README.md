# Udacity - Self Driving Nanodegree - Capstone Project

The code in this repo is our submission for the final project of the Udacity Self-Driving Car Nanodegree: Programming a Real Self-Driving Car.  For more information about the project, see the project introduction [here](https://classroom.udacity.com/nanodegrees/nd013/parts/6047fe34-d93c-4f50-8336-b70ef10cb4b2/modules/e1a23b06-329a-4684-a717-ad476f0d8dff/lessons/462c933d-9f24-42d3-8bdc-a08a5fc866e4/concepts/5ab4b122-83e6-436d-850f-9f4d26627fd9).

Our group, the "Overtakers", consists of the following members:

 - [Martin Kan](mailto:martinkan@gmail.com) 
 - [Batururimi Ezistas](mailto:s.batururimi@gmail.com)
 - [Shuang Gao](mailto:rebecca.shuang@gmail.com)
 - [Yue Jiang](mailto:maze1024@gmail.com)
 - [Yocheved Weill](mailto:yocheved.ovits@gmail.com)
 
## Setup instructions

Please use **one** of the two installation options, either native **or** docker installation.

### Native Installation

* Be sure that your workstation is running Ubuntu 16.04 Xenial Xerus or Ubuntu 14.04 Trusty Tahir. [Ubuntu downloads can be found here](https://www.ubuntu.com/download/desktop).
* If using a Virtual Machine to install Ubuntu, use the following configuration as minimum:
  * 2 CPU
  * 2 GB system memory
  * 25 GB of free hard drive space

  The Udacity provided virtual machine has ROS and Dataspeed DBW already installed, so you can skip the next two steps if you are using this.

* Follow these instructions to install ROS
  * [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu) if you have Ubuntu 16.04.
  * [ROS Indigo](http://wiki.ros.org/indigo/Installation/Ubuntu) if you have Ubuntu 14.04.
* [Dataspeed DBW](https://bitbucket.org/DataspeedInc/dbw_mkz_ros)
  * Use this option to install the SDK on a workstation that already has ROS installed: [One Line SDK Install (binary)](https://bitbucket.org/DataspeedInc/dbw_mkz_ros/src/81e63fcc335d7b64139d7482017d6a97b405e250/ROS_SETUP.md?fileviewer=file-view-default)
* Download the [Udacity Simulator](https://github.com/udacity/CarND-Capstone/releases).

### Docker Installation
[Install Docker](https://docs.docker.com/engine/installation/)

Build the docker container

**Pure ROS**
```bash
docker build --rm . -t capstone
```
Run the docker file
```bash
docker run --rm -it -p 4567:4567  -v "/$(pwd)":/capstone -v /tmp/log:/root/.ros/ capstone
```

or

**tensorflow GPU**
```bash
docker build --rm . -f GPU.dockerfile -t capstone
```


### Docker Installation With Nvidia GPU
Install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

Build the docker container
```bash
docker build --file GPU.dockerfile . -t capstone-gpu
```
Run the docker file
```bash
docker run --runtime=nvidia --rm -it -p 4567:4567  -v "/$(pwd)":/capstone -v /tmp/log:/root/.ros/ capstone-gpu
```

Run Sim
```
source "/opt/ros/$ROS_DISTRO/setup.bash"
catkin_make
source devel/setup.sh
roslaunch launch/styx.launch
```




**NB**
You may need to update the cryptography packages:
```bash
apt-get --auto-remove --yes remove python-openssl
pip install pyopenssl
apt-get install ros-kinetic-cv-bridge
apt-get install ros-kinetic-pcl-ros
```



### Port Forwarding
To set up port forwarding, please refer to the [instructions from term 2](https://classroom.udacity.com/nanodegrees/nd013/parts/40f38239-66b6-46ec-ae68-03afd8a601c8/modules/0949fca6-b379-42af-a919-ee50aa304e6a/lessons/f758c44c-5e40-4e01-93b5-1a82aa4e044f/concepts/16cf4a78-4fc7-49e1-8621-3450ca938b77)

### Usage

1. Clone the project repository
```bash
git clone https://github.com/udacity/CarND-Capstone.git
```

2. Install python dependencies
```bash
cd CarND-Capstone
pip install -r requirements.txt
pip install Pillow --upgrade #necessary to fix the camera problem
```
3. Install tensorflow
```bash
# For CPU only 
pip install tensorflow 
# For CUDA enabled GPU cards
pip install tensorflow-gpu
```

4. Update ROS environment
```bash
rosdep update # yes, even if we have that in Dockerfile
```
5. Make and run styx
```bash
cd ros
catkin_make
source devel/setup.sh
roslaunch launch/styx.launch
```
6. Run the simulator

### Simulator dataset
You can extract simulator images by uncommenting the following code in `ros/src/tl_detector/tl_detector.py` in `image_cb`:
```python
if self.dbw_enabled:
            # create the directory to save to if not already create
            if not os.path.exists(SIMULATOR_DIR):
                os.makedirs(SIMULATOR_DIR)

            cv_image = self.bridge.imgmsg_to_cv2(self.camera_image, "bgr8")
            filename = os.path.join(SIMULATOR_DIR, "{}.png".format(str(uuid.uuid4())))
            cv2.imwrite(filename, cv_image)
```
Some already extracted images can be found [here](https://transfer.sh/QpFVG/dataset_sim.zip)

### Real world testing
1. Download [training bag](https://s3-us-west-1.amazonaws.com/udacity-selfdrivingcar/traffic_light_bag_file.zip) that was recorded on the Udacity self-driving car.
2. Unzip the file
```bash
unzip traffic_light_bag_file.zip
```
3. Play the bag file
```bash
rosbag play -l traffic_light_bag_file/traffic_light_training.bag
```
4. Launch your project in site mode
```bash
cd CarND-Capstone/ros
roslaunch launch/site.launch
```
5. Confirm that traffic light detection works on real life images

## Results

To be completed
