"""
Definisi kelas Node dan method yang berhubungan dengan pemrosesan Node
"""
from math import sin, cos, sqrt, atan2, radians

class Node:
    def __init__(self, name, x, y):
        self.name = name            # Nama node
        self.x = x                  # Titik latitude
        self.y = y                  # Titik longitude
        self.neighbors = dict()     # Dictionary of node, menunjukkan hubungan neighbors antar Node dengan sebuah weight
    
    def addNeighbors(self, N, weight):
        # Menambahkan neighbor self dengan node N dan bobot weight
        self.neighbors[N.name] = weight

    def printNode(self):
        print(f"{self.name} at ({self.x}, {self.y})")

        for neighbor, weight in self.neighbors.items():
            print(f"Neighbor: {neighbor} ({weight})")

        print()
    
    def calcHaversineDist(self, n):
        # Menghitung jarak dari node dan node lain (n) berdasarkan longitude dan latitude
        # Menggunakan Haversine formula dalam meter
        haversineDist(self, n)


def haversineDist(n1, n2):
    # Menghitung jarak dari node n1 dan n2 berdasarkan longitude dan latitude
    # Menggunakan Haversine formula dalam meter

    # Aproksimasi radius bumi dalam meter
    R = 6373.0 * 1000

    lat1 = radians(n1.x)
    lon1 = radians(n1.y)

    lat2 = radians(n2.x)
    lon2 = radians(n2.y)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance