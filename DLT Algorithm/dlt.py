import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd
from cv2 import projectPoints

def calibrate_camera(world_points, image_points):
    """
    Função para encontrar a matriz de câmera C usando o algoritmo DLT.
    
    Args: 
        world_points: Array de pontos 3D na cena.
        image_points: Array de pontos 2D projetados na imagem.

    Return: 
        C_matrix: numpy array contendo a matriz de câmera estimada. 
    """

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
    print(Q)

    # Resolva o sistema de equações usando SVD
    _, _, V = svd(Q)
    c = V[-1, :12]
    print(c)

    # Reconstrua a matriz de projeção da câmera
    C_matrix = c.reshape(3, 4)
    print(C_matrix)

    return C_matrix

def create_world_points(num_points:int):
    """
    Função para gerar um conjunto de pontos 3D.

    Args:
        num_points: número de pontos 3D a serem gerados.

    Return: 
        world_points: Array de pontos 3D gerados. 
    """
    world_points = np.random.rand(num_points, 3) 

    return world_points

def create_image_points(world_points, rotation_matrix, translation_vector, k_matrix):
    """
    Função para gerar um conjunto de pontos 2D, projetados por uma câmera virtual.

    Args: 
        world_points: Array numpy que contém as coordenadas 3D dos pontos que você deseja projetar no plano de imagem. 
        Cada ponto é especificado como uma linha da matriz, onde cada linha é uma lista de coordenadas [X, Y, Z].
        rotation matrix: Matriz de rotação que representa a orientação da câmera no espaço 3D
        translation_vector: Vetor de translação que representa a posição da câmera no espaço 3D.
        k_matrix: Matriz que contém informações sobre os parâmetros intrínsecos da câmera
    
    Return: 
        image_points: Array numpy contendo os pontos 2D projetados 
    """
    image_points = projectPoints(world_points, rotation_matrix, translation_vector, k_matrix, None)[0]
    image_points = image_points.reshape(-1,2)

    return image_points

#TO-DO: 
#Função para projetar os pontos da imagem dada uma matriz de câmera C
#Vai ser usada para gerar os pontos da imagem utilizando a matriz de câmera estimada

