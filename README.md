# 📸 Camera Calibration in Mocap Arena ![Status](https://img.shields.io/static/v1?style=flat&logo=github&label=status&message=active&color=blue) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)  
Camera calibration Guide for Optical Tracking Systems

<p align="center">
<img src="https://user-images.githubusercontent.com/48807586/177659981-d0c4ffe2-3738-45ec-886e-c289925b0546.png" height="200" align="center">
</p>

> - This project came from the need to improve the camera calibration results of [Mocap Arena](https://github.com/debOliveira/MoCapRasp), once the system works with an error in focal distance calibration, which impacts the accuracy of the results when switching between pairs of cameras.

This project presents a study of the calibration methods accuracy, analysing the state of art technics available for parameters estimation and your impacts in object tracking systems. If you wanna perfom camera calibration, this repository contains a general guideline to correctily estimate the intrisic parameters and have accurate measurements for visual systems. 

## 📖 This project will study: 

- The matematical modeling of a camera and the process to estimate the intrisics parameters
- The state of art calibration techniques and your residual reprojection error
-  The parameters otimization process using non-linear algorithms

## 🗒️ Materials

The camera used for test the calibration algorithms is a [Raspberry V2 Cam](https://www.raspberrypi.com/documentation/accessories/camera.html#hardware-specification). For test the algorithm perfomance with high distortion lenses, is used [Raspberry V1 Cam](https://www.raspberrypi.com/documentation/accessories/camera.html#hardware-specification).

The techniques is also tested in Mocap Arena, for analyse the their perfomance for optical tracking systems. 
<p align="center">
<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F61a60905-553c-4ac1-b434-015efaf3bc12%2FUntitled.jpeg?id=9e70f2cc-40ce-4df6-bf7c-6d4b1413bab4&table=block&spaceId=a904d409-e00a-4242-8a47-07265f36cce4&width=2000&userId=ebc47754-3afc-4c04-9529-5c9fc0097eb7&cache=v2" height="200" align="center">
</p>

Is used four models of calibration targets: **Chessboard, Circle Grids, ArUco and ChArUco**

## 🔗 Useful links: 

For more information about the camera calibration process, check: 

- [Mocap Arena Guideline](https://engenhariacommateus.notion.site/Funcionamento-da-Arena-fc169ef74e1e4d0f98e3627c3132c88c)
- [Mathematical Camera Model]()
