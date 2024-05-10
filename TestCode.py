import numpy as np

def solve_using_inverse_matrix(A, b):
    # Menghitung matriks balikan dari A
    A_inv = np.linalg.inv(A)
    # Mengalikan matriks balikan dengan vektor b
    x = np.dot(A_inv, b)
    return x

def solve_using_LU_Gauss(A, b):
    # Mendekomposisi matriks A menjadi LU
    P, L, U = scipy.linalg.lu(A)
    # Menyelesaikan Ly = b menggunakan substitusi maju
    y = np.linalg.solve(L, b)
    # Menyelesaikan Ux = y menggunakan substitusi mundur
    x = np.linalg.solve(U, y)
    return x

def solve_using_Crout(A, b):
    # Mendekomposisi matriks A menjadi LU menggunakan metode Crout
    LU, piv = scipy.linalg.lu_factor(A)
    # Menyelesaikan sistem persamaan linear menggunakan LU yang sudah diperoleh
    x = scipy.linalg.lu_solve((LU, piv), b)
    return x

# Contoh sistem persamaan linear
A = np.array([[2, 1, -1], [1, 3, 2], [3, 2, -1]])
b = np.array([8, 13, 9])

# Menyelesaikan dengan metode matriks balikan
solution_inverse_matrix = solve_using_inverse_matrix(A, b)
print("Solusi dengan metode matriks balikan:", solution_inverse_matrix)

# Menyelesaikan dengan metode dekomposisi LU Gauss
solution_LU_Gauss = solve_using_LU_Gauss(A, b)
print("Solusi dengan metode dekomposisi LU Gauss:", solution_LU_Gauss)

# Menyelesaikan dengan metode dekomposisi Crout
solution_Crout = solve_using_Crout(A, b)
print("Solusi dengan metode dekomposisi Crout:", solution_Crout)

# Uji kesamaan solusi
print("Apakah solusi menggunakan matriks balikan sama dengan solusi menggunakan dekomposisi LU Gauss?", np.allclose(solution_inverse_matrix, solution_LU_Gauss))
print("Apakah solusi menggunakan matriks balikan sama dengan solusi menggunakan dekomposisi Crout?", np.allclose(solution_inverse_matrix, solution_Crout))