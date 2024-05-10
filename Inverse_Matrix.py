import numpy as np

def solve_using_inverse_matrix(A, b):
    # Menghitung matriks balikan dari A
    A_inv = np.linalg.inv(A)
    # Mengalikan matriks balikan dengan vektor b
    x = np.dot(A_inv, b)
    return x

# Contoh sistem persamaan linear
A = np.array([[2, 1, -1], [1, 3, 2], [3, 2, -1]])
b = np.array([8, 13, 9])

# Menyelesaikan dengan metode matriks balikan
solution_inverse_matrix = solve_using_inverse_matrix(A, b)
print("Solusi dengan metode matriks balikan:", solution_inverse_matrix)
