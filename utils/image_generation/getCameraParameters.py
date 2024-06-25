# Make sure to have the add-on "ZMQ remote API" running in
# CoppeliaSim and have following scene loaded:
#
# Load the scene: 
# calibration.ttt
#
# Do not launch simulation, but run this script
#
# All CoppeliaSim commands will run in blocking mode (block
# until a reply from CoppeliaSim is received). For a non-
# blocking example, see simpleTest-nonBlocking.py

import time
import math
import numpy as np
import cv2
import random

from coppeliasim_zmqremoteapi_client import RemoteAPIClient

patternSize = (9,9)

def randt(L): # Confined in a cube with an edge of length L
    return [2*L*random.random()-L for _ in range(3)]
    
def sum_coord(A, B):
    for coord in range(len(A)):
        B[coord] += A[coord]
    return B

# ------------------------------------------------------------------

print('Program started')


# Connect and configure the simulation 
client = RemoteAPIClient()
sim = client.getObject('sim')

# When simulation is not running, ZMQ message handling could be a bit
# slow, since the idle loop runs at 8 Hz by default. So let's make
# sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)   
sim.setInt32Param(sim.intparam_idle_fps, 0)

# Get the vision sensor handle
visionSensorHandle = sim.getObject('/Vision_sensor')
#cubo = sim.getObject('/Cuboid[3]')

# Start simulation in CoppeliaSim
sim.startSimulation()

# Number of calibration images
number_images = 10

# See the Vision sensor image

while (t := sim.getSimulationTime()) < 5:
    #p=sim.getObjectPosition(cubo,-1)

    for idx in range(number_images):
        # New aleatory position
        ds = randt(0.3)
        #sim.setObjectPosition(cubo,-1, sum_coord(p,ds))

        # Take a photo
        img, resX, resY = sim.getVisionSensorCharImage(visionSensorHandle)
        img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
        img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)

        # Check if are visible corners
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detected, _ = cv2.findChessboardCornersSB(gray, patternSize, None)
        
        print(detected)
        
        if detected == True:
            print(f"Corners detected in image {idx}")
                
            # Write the image
            cv2.imwrite(f'image4{idx}.jpg',img)
            time.sleep(0.75)

sim.stopSimulation()

# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

cv2.destroyAllWindows()

print('Program ended')
