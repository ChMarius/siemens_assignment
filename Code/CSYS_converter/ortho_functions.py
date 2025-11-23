# Orthornormality checks and orthogonalization process for the CSYS systems

import numpy as np

# Vectors are orthonormal if 
# a) each axis has length 1
# b) all dot products are zero, as axes must be perpendicular (x*y=0)

# Details about formulas and implementation are in ortho_functions.txt


def check_orthonormal(csys_matrix ,tol=1e-6):
    
    x_axis, y_axis, z_axis = csys_matrix[:,0], csys_matrix[:,1], csys_matrix[:,2]
    # a)
    if not (abs(np.linalg.norm(x_axis) - 1) < tol and 
            abs(np.linalg.norm(y_axis) - 1) < tol and
            abs(np.linalg.norm(z_axis) - 1) < tol):
        return False
    
    # b)
    if not (abs(np.dot(x_axis, y_axis)) < tol and
            abs(np.dot(x_axis, z_axis)) < tol and
            abs(np.dot(y_axis, z_axis)) < tol):
        return False
    
    return True

# Orthogonalization is done with the Gram-Schmidt method

def orthogonalize_axes(csys_matrix):
    x_axis, y_axis = csys_matrix[:,0], csys_matrix[:,1]
    
    # Normalization of the x_axis
    ux_axis = x_axis / np.linalg.norm(x_axis)
    
    # Normalization of the y_axis
    y_perp_axis = y_axis - np.dot(y_axis, ux_axis) * ux_axis
    uy_axis = y_perp_axis / np.linalg.norm(y_perp_axis)

    # Normalization of the z_axis
    uz_axis = np.cross(ux_axis, uy_axis)
    uz_axis = uz_axis / np.linalg.norm(uz_axis)

    # Modifying the matrix with the orthogonalized values
    csys_matrix[:,0] = ux_axis
    csys_matrix[:,1] = uy_axis
    csys_matrix[:,2] = uz_axis

    return  csys_matrix

