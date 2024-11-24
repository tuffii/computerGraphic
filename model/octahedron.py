import math
import numpy as np
from OpenGL.GL import *


class Octahedron:
    def __init__(self):
        vertices = [
            # Positions         Normals          Texture Coords
            1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
            -1.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.5, 1.0,
            0.0, -1.0, 0.0, 0.0, -1.0, 0.0, 0.5, 0.0,
            0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.5,
            0.0, 0.0, -1.0, 0.0, 0.0, -1.0, 0.5, 0.5,
        ]

        indices = [
            0, 2, 4,
            2, 1, 4,
            0, 3, 4,
            3, 1, 4,
            0, 2, 5,
            2, 1, 5,
            0, 3, 5,
            3, 1, 5,
        ]

        self._indices_count = len(indices)
        self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)
        self.EBO = glGenBuffers(1)

        vertices = np.array(vertices, dtype='float32')
        indices = np.array(indices, dtype='uint32')

        glBindVertexArray(self.VAO)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

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
        glDrawElements(GL_TRIANGLES, self._indices_count, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)
