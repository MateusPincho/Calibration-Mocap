import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_image_points(image_points):
    """
    Plota os pontos 2D na imagem.

    :param image_points: Array de pontos 2D projetados na imagem.
    """

    if image_points.shape[1] != 2:
        raise ValueError("A matriz de image_points deve ter duas colunas (X e Y).")
    
    plt.figure(figsize=(8, 6))
    plt.scatter(image_points[:, 0], image_points[:, 1], c='b', marker='o', label='Pontos Projetados')
    plt.xlabel('Coordenada X na Imagem')
    plt.ylabel('Coordenada Y na Imagem')
    plt.title('Pontos 2D Projetados na Imagem')
    plt.grid()
    plt.legend()
    plt.show()

def plot_world_points_with_camera_position(world_points, camera_position):
    """
    Plota os pontos 3D no mundo real juntamente com a localização da câmera.

    :param world_points: Array de pontos 3D no mundo real.
    :param camera_position: Vetor 3D que representa a posição[X,Y,Z] da câmera no mundo real.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plota os pontos 3D no mundo real
    ax.scatter(world_points[:, 0], world_points[:, 1], world_points[:, 2], c='b', marker='o', label='Pontos 3D')
    
    # Plota a localização da câmera
    ax.scatter(camera_position[0], camera_position[1], camera_position[2], c='r', marker='s', s=200, label='Câmera')
    
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')
    ax.set_title('Pontos 3D no Mundo Real com Localização da Câmera')
    ax.legend()
    plt.show()

def plot_world_points_with_camera_reference(world_points, rotation_matrix, translation_vector):
    """
    Plota os pontos 3D no sistema de coordenadas da câmera com base no vetor de rotação e translação.

    :param world_points: Array de pontos 3D no sistema de coordenadas do mundo.
    :param rotation_matrix: Matriz de rotação da câmera.
    :param translation_vector: Vetor de translação da câmera.
    """
    num_points = world_points.shape[0]

    # Repete o vetor de translação para ter o mesmo número de linhas que world_points
    translation_matrix = np.repeat(translation_vector.reshape(1, -1), num_points, axis=0)

    # Transforma os pontos do sistema de coordenadas do mundo para o sistema da câmera
    camera_points = np.dot(world_points, rotation_matrix.T) + translation_matrix

    # Cria uma figura 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plota os pontos 3D no sistema de coordenadas da câmera
    ax.scatter(camera_points[:, 0], camera_points[:, 1], camera_points[:, 2], c='b', marker='o', label='Pontos 3D (Câmera)')

    ax.set_xlabel('Eixo X (Câmera)')
    ax.set_ylabel('Eixo Y (Câmera)')
    ax.set_zlabel('Eixo Z (Câmera)')
    ax.set_title('Pontos 3D no Sistema de Coordenadas da Câmera')
    ax.legend()
    plt.show()