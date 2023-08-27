import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random
import math


class Cube:
    def __init__(self, x, y, z, l):
        self.x = x
        self.y = y
        self.z = z
        self.l = l

    def get_vertices(self):
        return [
            [self.x, self.y, self.z],
            [self.x + self.l, self.y, self.z],
            [self.x + self.l, self.y + self.l, self.z],
            [self.x, self.y + self.l, self.z],
            [self.x, self.y, self.z + self.l],
            [self.x + self.l, self.y, self.z + self.l],
            [self.x + self.l, self.y + self.l, self.z + self.l],
            [self.x, self.y + self.l, self.z + self.l]
        ]

    def get_faces(self):
        vertices = self.get_vertices()
        return [
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[7], vertices[6], vertices[2], vertices[3]],
            [vertices[0], vertices[4], vertices[7], vertices[3]],
            [vertices[1], vertices[5], vertices[6], vertices[2]],
            [vertices[4], vertices[5], vertices[6], vertices[7]]
        ]

    def get_poly3dcollection(self):
        faces = self.get_faces()
        return Poly3DCollection(faces, linewidths=1, edgecolors='r', alpha=0.1)


class Plotter:
    def __init__(self, cubes: list):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.cubes = cubes

    def show(self):
        for cube in self.cubes:
            self.ax.add_collection3d(cube.get_poly3dcollection())

        self.ax.set_xlim([0, math.sqrt(len(self.cubes)) + 1])
        self.ax.set_ylim([0, math.sqrt(len(self.cubes)) + 1])
        self.ax.set_zlim([0, math.sqrt(len(self.cubes)) + 1])
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        plt.show()


class CarreLatin:
    def __init__(self, size):
        self.size = size
        self.square = self.generate_square()

    def shuffle_array(self, array):
        for i in range(len(array) - 1, 0, -1):
            j = random.randint(0, i)
            array[i], array[j] = array[j], array[i]

    def generate_square(self):
        square = [[0] * self.size for _ in range(self.size)]

        # Remplir la première ligne avec des nombres consécutifs
        for i in range(self.size):
            square[0][i] = i + 1

        # Mélanger la première ligne de manière aléatoire
        self.shuffle_array(square[0])

        # Générer les lignes suivantes
        for i in range(1, self.size):
            for j in range(self.size):
                square[i][j] = square[i - 1][(j + 1) % self.size]

        return square

    def get_cubes(self):
        cubes = []
        for i in range(self.size):
            for j in range(self.size):
                cubes.append(Cube(i, j, self.square[i][j], 1))
        return cubes


if __name__ == "__main__":
    size = int(input("Taille du carré latin: "))
    carre_latin = CarreLatin(size)
    cubes = carre_latin.get_cubes()
    print(len(cubes))
    plotter = Plotter(cubes)
    plotter.show()
