from OpenGL.GL import *
from .Mesh import *
import numpy as np
import pygame
import random
from .Utils import *



class LoadMesh(Mesh):
    def __init__(self, filename, imagefile, draw_type=GL_TRIANGLES,
                 location=pygame.Vector3(0, 0, 0),
                 rotation=Rotation(0, pygame.Vector3(0, 1, 0)),
                 scale=pygame.Vector3(1, 1, 1),
                 move_rotation=Rotation(0, pygame.Vector3(0, 1, 0)),
                 move_translate=pygame.Vector3(0, 0, 0),
                 move_scale=pygame.Vector3(1, 1, 1),
                 material=None
                 ):
        coordinates, triangles, uvs, uvs_ind, normals, normal_ind = self.load_drawing(filename)
        vertices = format_vertices(coordinates, triangles)
        vertex_normals = format_vertices(normals, normal_ind)
        vertex_uvs = format_vertices(uvs, uvs_ind)
        colors = []
        for i in range(len(vertices)):
            colors.append(1)
            colors.append(1)
            colors.append(1)
        super().__init__(vertices,
                         imagefile=imagefile,
                         vertex_normals=vertex_normals,
                         vertex_uvs=vertex_uvs,
                         vertex_colors=colors,
                         draw_type=draw_type,
                         translation=location,
                         rotation=rotation,
                         scale=scale,
                         move_rotation=move_rotation,
                         move_translate=move_translate,
                         move_scale=move_scale,
                         material=material)

    def load_drawing(self, filename):
        vertices = []
        triangles = []
        normals = []
        normal_ind = []
        uvs = []
        uvs_ind = []
        with open(filename) as fp:
            line = fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    vertices.append((vx, vy, vz))
                if line[:2] == "vn":
                    vx, vy, vz = [float(value) for value in line[3:].split()]
                    normals.append((vx, vy, vz))
                if line[:2] == "vt":
                    vx, vy = [float(value) for value in line[3:].split()]
                    uvs.append((vx, vy))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    triangles.append([int(value) for value in t1.split('/')][0]-1)
                    triangles.append([int(value) for value in t2.split('/')][0]-1)
                    triangles.append([int(value) for value in t3.split('/')][0]-1)
                    uvs_ind.append([int(value) for value in t1.split('/')][1] - 1)
                    uvs_ind.append([int(value) for value in t2.split('/')][1] - 1)
                    uvs_ind.append([int(value) for value in t3.split('/')][1] - 1)
                    normal_ind.append([int(value) for value in t1.split('/')][2] - 1)
                    normal_ind.append([int(value) for value in t2.split('/')][2] - 1)
                    normal_ind.append([int(value) for value in t3.split('/')][2] - 1)
                line = fp.readline()
        return vertices, triangles, uvs, uvs_ind, normals, normal_ind

