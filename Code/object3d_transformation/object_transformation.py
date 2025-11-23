# Main function for the object transformation functionality
# Input: the 3d object, the CSYS1 system, the CSYS2 system
# Output: updated object with new location and orientation value

from Code.CSYS_converter.CSYS_converter import CSYS_point_converter
import numpy as np

def Object3d_transform(object3d, csys1, csys2):

    # Point converter function from CSYS_converter.py to transform the location
    new_location = CSYS_point_converter(csys1, csys2, object3d.location) 

    # Transform the orientation with the formula: Q2 = R2^T * R1 * Q1
    new_orientation = (csys2.matrix.T @ csys1.matrix) @ object3d.orientation

    return object3d(new_location, new_orientation)
