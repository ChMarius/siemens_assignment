# Unit test for the csys_point_converter function

import numpy as np
from csys import CSYS
from CSYS_converter import CSYS_point_converter

def test_CSYS_point_converter():

    # Arrange
    origin1 = [0,0,0]
    origin2 = [0,0,0]

    matrix1 = np.eye(3)
    matrix2 = np.eye(3)

    csys1 = CSYS(origin1, matrix1)
    csys2 = CSYS(origin2, matrix2)

    p1 = np.array([1,2,3])

    # Act
    p2 = CSYS_point_converter(csys1, csys2, p1)
    print("Converted point: ", p2)

    # Assert
    assert np.allclose(p1, p2), "Conversion failed!"

if __name__ == "__main__":
    test_CSYS_point_converter()
    print("Test passed!")
