# Main function of the point conversion, responsbile for point transformation from CSYS1 to CSYS2
# Input: CSYS1 system, CSYS2 system, CSYS1 position
# Output: CSYS2 position

import numpy as np
import ortho_functions as ortho
from csys_validation import validate_csys, validate_point

def CSYS_point_converter(csys1, csys2, p1):

    # Validation and error handling before the main computation
    validate_csys(csys1, "CSYS1")
    validate_csys(csys2, "CSYS2")
    p1 = validate_point(p1)
    
    # Orthornormality check
    if not ortho.check_orthonormal(csys1.matrix):
        csys1.matrix = ortho.orthogonalize_axes(csys1.matrix)
    if not ortho.check_orthonormal(csys2.matrix):
        csys2.matrix = ortho.orthogonalize_axes(csys2.matrix)
 
    # Main transformation
    p_global = csys1.origin + csys1.matrix @ p1
    p2 = csys2.matrix.T @ (p_global - csys2.origin)

    return p2
    

