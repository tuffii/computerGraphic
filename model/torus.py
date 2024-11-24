import math
import numpy as np
from OpenGL.GL import *


class Torus:
    def __init__(self, inner_radius, outer_radius, sides, rings):
        vertices = []
        ring_step = 2 * math.pi / rings
        side_step = 2 * math.pi / sides

        for ring in range(rings + 1):
            ring_angle = ring * ring_step
            for side in range(sides + 1):
                side_angle = side * side_step
                x = (outer_radius + inner_radius * math.cos(side_angle)) * math.cos(ring_angle)
                y = (outer_radius + inner_radius * math.cos(side_angle)) * math.sin(ring_angle)
                z = inner_radius * math.sin(side_angle)
                nx, ny, nz = x - outer_radius * math.cos(ring_angle), y - outer_radius * math.sin(ring_angle), z
                length = math.sqrt(nx * nx + ny * ny + nz * nz)
                nx, ny, nz = nx / length, ny / length, nz / length
                u, v = ring / rings, side / sides
                vertices.extend([x, y, z, nx, ny, nz, u, v])

        indices = []
        for ring in range(rings):
            for side in range(sides):
                first = (ring * (sides + 1)) + side
                second = first + sides + 1
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

