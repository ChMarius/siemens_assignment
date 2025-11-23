# Definition of the 3d object class, with the following properties:
# location as 3-point vector
# orientation as 3x3 matrix

import numpy as np

class Object3d:
    def __init__(self, location, orientation):
        self.location = np.array(location, dtype=float)
        self.orientation = np.array(orientation, dtype=float)
