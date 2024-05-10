import numpy as np
import scipy.linalg

def solve_using_Crout(A, b):
    # Mendekomposisi matriks A menjadi LU menggunakan metode Crout
    LU, piv = scipy.linalg.lu_factor(A)
    # Menyelesaikan sistem persamaan linear menggunakan LU yang sudah diperoleh
    x = scipy.linalg.lu_solve((LU, piv), b)
    return x

# Contoh sistem persamaan linear
A = np.array([[2, 1, -1], [1, 3, 2], [3, 2, -1]])
b = np.array([8, 13, 9])

# Menyelesaikan dengan metode dekomposisi Crout
solution_Crout = solve_using_Crout(A, b)
print("Solusi dengan metode dekomposisi Crout:", solution_Crout)
