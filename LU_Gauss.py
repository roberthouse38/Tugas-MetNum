import numpy as np
import scipy.linalg

def solve_using_LU_Gauss(A, b):
    # Mendekomposisi matriks A menjadi LU
    P, L, U = scipy.linalg.lu(A)
    # Menyelesaikan Ly = b menggunakan substitusi maju
    y = np.linalg.solve(L, b)
    # Menyelesaikan Ux = y menggunakan substitusi mundur
    x = np.linalg.solve(U, y)
    return x

# Contoh sistem persamaan linear
A = np.array([[2, 1, -1], [1, 3, 2], [3, 2, -1]])
b = np.array([8, 13, 9])

# Menyelesaikan dengan metode dekomposisi LU Gauss
solution_LU_Gauss = solve_using_LU_Gauss(A, b)
print("Solusi dengan metode dekomposisi LU Gauss:", solution_LU_Gauss)
