# Error handling and validation for the csys_point_converter function
# Validates the format of the systems' matrices and of CSYS1 point

import numpy as np

def validate_point(p1):
    # Validate that p1 is a numeric 3-element vector.
    try:
        p1 = np.array(p1, dtype=float)
    except Exception:
        raise ValueError("p1 must be a numeric 3-element vector")
    return p1


def validate_csys_matrix(matrix, name="CSYS.matrix"):
    # Validate that CSYS.matrix is a 3×3 numeric numpy array.

    if matrix.shape != (3, 3):
        raise ValueError(f"{name} must be a 3×3 numpy array, got shape {matrix.shape}")
    return matrix


def validate_csys_origin(origin, name="CSYS.origin"):
    # Validate that CSYS.origin is a numeric 3-element numpy array.
    if origin.shape != (3,):
        raise ValueError(f"{name} must be a 3-element numpy array, got shape {origin.shape}")

    return origin


def validate_csys(csys, name="CSYS"):
    # Validate both origin and matrix for a CSYS object.
    validate_csys_matrix(csys.matrix, f"{name}.matrix")
    validate_csys_origin(csys.origin, f"{name}.origin")