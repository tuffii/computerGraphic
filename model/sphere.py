import math
import numpy as np
from OpenGL.GL import *


class Sphere:

    def __init__(self, radius, stacks, sectors):
        vertices = []
        for stack in range(stacks + 1):
            stack_angle = math.pi / 2 - stack * math.pi / stacks
            xy = radius * math.cos(stack_angle)
            z = radius * math.sin(stack_angle)

            for sector in range(sectors + 1):
                sector_angle = 2 * math.pi * sector / sectors
                x = xy * math.cos(sector_angle)
                y = xy * math.sin(sector_angle)
                nx, ny, nz = x / radius, y / radius, z / radius
                u, v = sector / sectors, stack / stacks
                vertices.extend([x, y, z, nx, ny, nz, u, v])

        indices = []
        for stack in range(stacks):
            for sector in range(sectors):
                first = stack * (sectors + 1) + sector
                second = first + sectors + 1
                indices.extend([first, second, first + 1, second, second + 1, first + 1])

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
