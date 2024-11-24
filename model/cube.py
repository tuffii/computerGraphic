import math
import numpy as np
from OpenGL.GL import *


class Cube:
    def __init__(self):
        vertices = np.array([
            # positions        normals         tex coords
            # Задняя сторона
            -1, -1, -1, 0, 0, -1, 0, 0,
            1, -1, -1, 0, 0, -1, 1, 0,
            1, 1, -1, 0, 0, -1, 1, 1,
            1, 1, -1, 0, 0, -1, 1, 1,
            -1, 1, -1, 0, 0, -1, 0, 1,
            -1, -1, -1, 0, 0, -1, 0, 0,

            # Передняя сторона
            -1, -1, 1, 0, 0, 1, 0, 0,
            1, -1, 1, 0, 0, 1, 1, 0,
            1, 1, 1, 0, 0, 1, 1, 1,
            1, 1, 1, 0, 0, 1, 1, 1,
            -1, 1, 1, 0, 0, 1, 0, 1,
            -1, -1, 1, 0, 0, 1, 0, 0,

            # Левая сторона
            -1, 1, 1, -1, 0, 0, 1, 0,
            -1, 1, -1, -1, 0, 0, 1, 1,
            -1, -1, -1, -1, 0, 0, 0, 1,
            -1, -1, -1, -1, 0, 0, 0, 1,
            -1, -1, 1, -1, 0, 0, 0, 0,
            -1, 1, 1, -1, 0, 0, 1, 0,

            # Правая сторона
            1, 1, 1, 1, 0, 0, 1, 0,
            1, 1, -1, 1, 0, 0, 1, 1,
            1, -1, -1, 1, 0, 0, 0, 1,
            1, -1, -1, 1, 0, 0, 0, 1,
            1, -1, 1, 1, 0, 0, 0, 0,
            1, 1, 1, 1, 0, 0, 1, 0,

            # Нижняя сторона
            -1, -1, -1, 0, -1, 0, 0, 1,
            1, -1, -1, 0, -1, 0, 1, 1,
            1, -1, 1, 0, -1, 0, 1, 0,
            1, -1, 1, 0, -1, 0, 1, 0,
            -1, -1, 1, 0, -1, 0, 0, 0,
            -1, -1, -1, 0, -1, 0, 0, 1,

            # Верхняя сторона
            -1, 1, -1, 0, 1, 0, 0, 1,
            1, 1, -1, 0, 1, 0, 1, 1,
            1, 1, 1, 0, 1, 0, 1, 0,
            1, 1, 1, 0, 1, 0, 1, 0,
            -1, 1, 1, 0, 1, 0, 0, 0,
            -1, 1, -1, 0, 1, 0, 0, 1,
        ], dtype='float32')

        self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)

        glBindVertexArray(self.VAO)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        stride = 8 * ctypes.sizeof(ctypes.c_float)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, None)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(3 * ctypes.sizeof(ctypes.c_float)))
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(6 * ctypes.sizeof(ctypes.c_float)))
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def render(self):
        glBindVertexArray(self.VAO)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        glBindVertexArray(0)