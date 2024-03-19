import numpy as np 
import matplotlib.pyplot as plt
from scipy.linalg import svd, rq
from modules.rigid import to_homo, rectangle, split_homo

def generate_random_points(n_points):
    '''
    Generate random points in the given limits

    ---
    Returns the points as column vectors
    '''
    x = np.random.rand(1,n_points)
    y = np.random.rand(1,n_points)
    z = np.random.rand(1,n_points)
    
    return np.vstack((x, y, z))

def create_intrinsic_matrix (focal_distance): 
    '''
    Cria a matriz de intrínsecos da câmera, desconsiderando um plano de imagem discreto    
    
    Parameters
    ---------
    focal_distance: the focal distance of the camera

    Return
    ------
    K: the corresponding 3x3 intrinsic matrix
    '''

    K = np.array([  [focal_distance, 0, 0,],
                    [0, focal_distance, 0 ],
                    [0, 0, 1]])
    
    return K

def crete_image_plane(width, height, camera_extrinsic, focal_distance): 
    '''
    Função para criar o image plane da câmera
    Returna os pontos do plano
    '''

    image_plane = rectangle(width,height)
    image_plane = to_homo(image_plane)

    image_plane = camera_extrinsic @ image_plane

    R, t = split_homo(camera_extrinsic)

    z_cam = R[:,2]
    image_plane = image_plane.T + focal_distance*z_cam
    image_plane = image_plane.T

    return image_plane

def project_points(K,E,world_points): 
    '''
    world_points -> world points ndarray (3,n_points)
    E -> Extrinsic Matrix (3,4)
    K -> Intrinsic Matrix (3,3)  

    return the image points projections 
    '''
    # Write the world points in the camera coordinate system


    # Write in homogeneous coordinates -> (4,n_points)
    world_points_homo = np.vstack((world_points,np.ones(world_points.shape[1])))

    # Convert to the camera frame -> (3,n_points)
    camera_points = E @ world_points_homo

    # Project the camera points

    image_points_homo = K @ camera_points 

    image_points_homo[0, :] = image_points_homo[0, :] / image_points_homo[2, :]
    image_points_homo[1, :] = image_points_homo[1, :] / image_points_homo[2, :]

    image_points = image_points_homo[:2, :] 

    return image_points


# Função para encontrar a matriz de câmera C usando o algoritmo DLT.
def calibrate_camera(world_points, image_points):

    if len(world_points) != len(image_points): 
        raise ValueError("Must be the same number of World points and Image points")
            
    if len(world_points) < 6 | len(image_points) < 6 :
        raise ValueError("Must have a minimum of 6 points to compute the camera matrix")

    Q = []
    for i in range(len(world_points)):
        X, Y, Z = world_points[i]
        u,v  = image_points[i]
        Q.append([X, Y, Z, 1, 0, 0, 0, 0, -u*X, -u*Y, -u*Z, -u])
        Q.append([0, 0, 0, 0, X, Y, Z, 1, -v*X, -v*Y, -v*Z, -v])

    Q = np.array(Q)

    # Resolva o sistema de equações usando SVD
    _, _, V = svd(Q)
    c = V[-1, :12]

    # Reconstrua a matriz de projeção da câmera
    C_matrix = c.reshape(3, 4)
    print("DLT camera matrix: \n", C_matrix)

    return C_matrix

def extract_camera_parameters(projection_matrix):
    # Decompor a matriz de projeção em RQ (decomposição de R e Q)
    K, RT = rq(projection_matrix, mode='full')
    
    # Certificar-se de que a diagonal da matriz intrínseca K seja positiva
    if K[0, 0] < 0:
        K = -K
        RT = -RT

    # Extrair a matriz de rotação R
    R = RT[:3, :3]

    # Extrair o vetor de translação t
    t = RT[:3, 3]

    return K, R, t