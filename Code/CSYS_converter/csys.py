# Definition of the CSYS class containing the following properties:
# origin as 3-point vector representing the location of the coordinate system
# matrix as 3x3 matrix, which represent the direction vectors

import numpy as np

class CSYS:
    def __init__(self, origin, matrix):
        self.origin = np.array(origin, dtype=float)
        self.matrix = np.array(matrix, dtype=float)
