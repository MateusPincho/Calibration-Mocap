#!/usr/bin/env python3
#Mocap Arena Camera Calibrate Program
#Mateus Pincho - calibrate intrisics
import argparse
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np

useFisheye = False
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

images = glob.glob('images/chess/virtual/*.jpg')
patternSize = (7,7)
squareSize = 30
imgSize = (480,480)

#Reconstrução do tabuleiro
def construct3DPoints(patternSize,squareSize):
    X = np.zeros((patternSize[0]*patternSize[1],3), np.float32)
    X[:,:2] = np.mgrid[0:patternSize[0],0:patternSize[1]].T.reshape(-1,2)
    X = X * squareSize
    return X

#Detectando os corners
def detectCorners(images, boardPoints, patternSize):
    worldPoints = []
    imagePoints = [] 

    counter = 0
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCornersSB(gray, patternSize, None)
        if ret == True:
            print("Corners found in image " + str(fname)) #- see if corners are found 
            imagePoints.append(corners)
            worldPoints.append(boardPoints)
            counter+=1

    print("Corners found in " + str(counter) + " images")
    return worldPoints, imagePoints

#Descobrindo os intrisicos 
def calibrate(useFisheye, worldPoints, imagePoints, imgSize):

    if useFisheye:
        flagsCalib = cv2.fisheye.CALIB_RECOMPUTE_EXTRINSIC+cv2.fisheye.CALIB_FIX_SKEW+cv2.fisheye.CALIB_CHECK_COND
        calibrateCriteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30, 1e-12)

        ret, cameraMatrix, k, R, t = cv2.fisheye.calibrate(np.expand_dims(np.asarray(worldPoints), -2), imagePoints, imgSize, None, None,
                                                                    flags=flagsCalib,criteria=calibrateCriteria)
    else:
        flagsCalib = cv2.CALIB_RATIONAL_MODEL

        ret, cameraMatrix, k, rvecs, tvecs = cv2.calibrateCamera(worldPoints, imagePoints, imgSize, None, None,
                                                                flags=flagsCalib)

    print("RMS re-projection error:", ret)
    print("Camera Matrix:\n", cameraMatrix)
    print("Distortion Parameters:\n", k)

def main():
    boardPoints = construct3DPoints(patternSize, squareSize)
    worldPoints, imagePoints = detectCorners(images, boardPoints, patternSize)
    calibrate(useFisheye, worldPoints, imagePoints, imgSize) 

if __name__ == '__main__':
    main()