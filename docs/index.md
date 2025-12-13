<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />

# Mukhlas Adib Rasyidy

![Profile photo](pics/myphoto.jpeg){ .circle-photo }

<div class="intro-points" markdown="1">

{{ icon("person_check") }} Professional ML/AI Engineer and Consultant

{{ icon("lab_research") }} Passionate in doing research and writing

{{ icon("history_edu") }} Loves teaching about AI

{{ icon("diversity_1") }} Long leadership experience

</div>

## Edge AI System for Real-time CCTV Analysis for High-level Safety System  

TBA

## Training Diffusion XL LoRa for Object-specific Image Generation

TBA

## PyStream Pipeline: Real-time Python Data Pipeline Framework

TBA

## ONNX Exporter for SOLOv2 Instance Segmentation Model

TBA

## Smart Split-Bill: Split Your Bill with Friends Easily

TBA

## Sample Data Forecasting Dashboard

TBA

## Environment Mapping for Autonomous Vehicle with OGM and DGM

![DGM](pics/dgm.gif)

One of the classic way to do environment mapping for robotics is what is known as Occupancy Grid Mapping (OGM). This Bayesian-inference-based simple method is able to classify surrounding environment of the robot as occupied or free space. An extension of this method is called Dynamic Grid Mapping (DGM) which is able to also estimate the possible moving objects in the environment using Dampster-Shafer theory.

This project implements both OGM and DGM for autonomous vehicle using mono-camera and LiDAR sensor and tested it on KITTI dataset. Road segmentation (MobileNet + DeepLabv3+) is trained to detects road which will be transformed into bird-eye-view perspective and fused with LiDAR point cloud to build OGM and DGM.

- [GitHub: KITTI Mapping](https://github.com/MukhlasAdib/KITTI_Mapping) 

## Detection and Mapping of Road Boundaries for Autonomous Vehicle

![RBM](pics/rbm.png)

Recognizing road boundaries is an essential task for autonomous vehicles navigation. Based on mono-camera and LiDAR sensor, I developed a new method to not only extract road boundaries, but also build the map of the city roads. This method uses image segmentation (custom trained MobileNet + DeepLabv3+), camera-lidar alignment, hierarchical clustering, RANSAC, and particle filter.

- [Regression with Ensemble of RANSAC in Camera-LiDAR Fusion for Road Boundary Detection and Modeling](https://ieeexplore.ieee.org/abstract/document/9913856)
- [A New Approach on Simultaneous Occupancy Grid Mapping and Particle-based Road Boundary Mapping for Autonomous Vehicles](https://ieeexplore.ieee.org/abstract/document/10004377)

## Autonomous Vehicle Research with Carla Simulator

![CARLA](pics/carla.png)

I did a significant amount of research on autonomous vehicles using [Carla Simulator](https://carla.org/) to validate verious algorithms for perception system. With the use of the simulator, it is significantly easier to gather ground truth and simulate various cases for my research in terms of object detection, road segmentation, road mapping, etc. 

- [GitHub: CARLA Vehicle 2D Bounding Box Annotation Module](https://github.com/MukhlasAdib/CARLA-2DBBox)
- [TechRxiv: A Framework for Road Boundary Detection based on Camera-LIDAR Fusion in World Coordinate System and Its Performance Evaluation Using Carla Simulator](https://www.techrxiv.org/doi/full/10.36227/techrxiv.21277656)
