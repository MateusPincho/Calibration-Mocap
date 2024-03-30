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

images = glob.glob('images/chess/cam-v2/chessV6-SalaAfastado/*.jpg')
patternSize = (10,7)
squareSize = 30
imgSize = (3280,2460)


#Reconstrução do tabuleiro

def construct3DPoints(patternSize,squareSize):
    X = np.zeros((patternSize[0]*patternSize[1],3), np.float32)
    X[:,:2] = np.mgrid[0:patternSize[0],0:patternSize[1]].T.reshape(-1,2)
    X = X * squareSize
    return X

#boardPoints = construct3DPoints(patternSize,squareSize)


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

    print("Using "+str(counter)+" of "+str(len(images))+" images")
    print("RMS re-projection error:", ret)
    print("Camera Matrix:\n", cameraMatrix)
    print("Distortion Parameters:\n", k)

def main():
    
    def tuple_arg(string):
        try:
            # Divida a string pelos espaços em branco e converta cada parte em um inteiro
            parts = map(int, string.split(','))
            return tuple(parts)
        except ValueError:
            raise argparse.ArgumentTypeError("A tupla deve ser fornecida no formato 'x,y' onde x e y são números inteiros")

    parser = argparse.ArgumentParser()
    parser.add_argument('--usefisheye', '-f', action='store_true', help='Calibrar considerando o modelo Fisheye')
    parser.add_argument('--height', '-h', type=int, help= 'Altura da imagem')
    parser.add_argument('--width', '-w', type= int, help= 'Largura da imagem')
    parser.add_argument('--image_resolution', '-r', type=tuple_arg, help = 'Resolucao da Imagem')
    parser.add_argument('--partern_size', '-p', type=tuple_arg, help='Tamanho do objeto de calibracao')
    parser.add_argument('--square_size', '-s', type=int, help="Tamanho do quadrado")

    args = parser.parse_args()
    boardPoints = construct3DPoints(args.partern_size, args.square_size)
    worldPoints, imagePoints = detectCorners(images, boardPoints, args.partern_size)
    calibrate(args.usefisheye, worldPoints, imagePoints, args.image_resolution) 

if __name__ == '__main__':
    main()