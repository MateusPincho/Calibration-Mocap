# 📸 Camera Calibration Virtual Arena ![Status](https://img.shields.io/static/v1?style=flat&logo=github&label=status&message=active&color=blue) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)  
Camera calibration Guide using CoppeliaSim. 

> - This project came from the need to improve the camera calibration results of [Mocap Arena](https://github.com/debOliveira/MoCapRasp), once the system works with an error in focal distance calibration, which impacts the accuracy of the results.

Camera-based measurement and space reconstruction offer the advantages of automation, speed, and accuracy. However, precise measurements necessitate the determination of the camera's intrinsic parameters through calibration. This involves capturing images of a known calibration pattern and solving for the camera model parameters. Reprojection error, the discrepancy between predicted and observed image points, is a key factor influencing calibration accuracy. Minimizing this error is the goal of camera calibration to ensure reliable measurements.

This project presents a camera calibration test environment, developed in CoppeliaSim Robot Simulator, where it's possible to test camera calibration methods and evaluate the accuracy of state of art technics available for parameters estimation.

## 📖 This project also contains: 

- A workflow for generate ground truth calibration images. 
- A matematical explanation of camera models and the process to estimate the intrisics parameters.
- A pratical guideline to correctily estimate the intrisic parameters and have accurate measurements.
- An analisys of camera calibration methods with respect to accuracy evaluation. 

## 🗒️ Requirements

- CoppeliaSim EDU 4.6
- Python 3.x
- Numpy 
- OpenCV 



## 🖥️ Usage

### First use

- Install CoppeliaSim EDU in their [website](https://www.coppeliarobotics.com/)

- Make a clone of this repo
``` shell 
git clone https://github.com/MateusPincho/Calibration-MoCap.git
```

### Generate non-distorted calibration image

### Generate distorted calibration image

### Perfom camera calibration with virtual images

### Perfom camera calibration with real images

## 🔗 Useful Links: 

For more information about the camera calibration process, check: 

- [Mocap Arena Guideline](https://engenhariacommateus.notion.site/Funcionamento-da-Arena-fc169ef74e1e4d0f98e3627c3132c88c)
- [Mathematical Camera Model]()

<p align="center">
<img src="https://user-images.githubusercontent.com/48807586/177659981-d0c4ffe2-3738-45ec-886e-c289925b0546.png" height="100" align="center">
</p>

The camera used for test the calibration algorithms is a [Raspberry V2 Cam](https://www.raspberrypi.com/documentation/accessories/camera.html#hardware-specification). For test the algorithm perfomance with high distortion lenses, is used [Raspberry V1 Cam](https://www.raspberrypi.com/documentation/accessories/camera.html#hardware-specification).

The techniques is also tested in Mocap Arena, for analyse the their perfomance for optical tracking systems. 
<p align="center">
<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F61a60905-553c-4ac1-b434-015efaf3bc12%2FUntitled.jpeg?id=9e70f2cc-40ce-4df6-bf7c-6d4b1413bab4&table=block&spaceId=a904d409-e00a-4242-8a47-07265f36cce4&width=2000&userId=ebc47754-3afc-4c04-9529-5c9fc0097eb7&cache=v2" height="200" align="center">
</p>

Is used four models of calibration targets: **Chessboard, Circle Grids, ArUco and ChArUco**

## Developing team
Mateus Pincho de Oliveira

Lorenzo Carrera de Oliveira
