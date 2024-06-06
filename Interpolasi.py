import numpy as np
import matplotlib as plt

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk menghitung polinomial Lagrange
def lagrange_interpolation(x, y, xi):
    def L(k, xi):
        li = 1
        for j in range(len(x)):
            if j != k:
                li *= (xi - x[j]) / (x[k] - x[j])
        return li

    yi = 0
    for k in range(len(x)):
        yi += y[k] * L(k, xi)
    return yi

# Fungsi untuk menghitung polinomial Newton
def newton_interpolation(x, y, xi):
    def divided_diff(x, y):
        n = len(y)
        coef = np.zeros([n, n])
        coef[:,0] = y

        for j in range(1,n):
            for i in range(n-j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

        return coef[0, :]

    coef = divided_diff(x, y)
    n = len(coef) - 1
    yi = coef[n]
    for i in range(n-1, -1, -1):
        yi = yi * (xi - x[i]) + coef[i]
    return yi

# Rentang nilai x untuk plot
x_plot = np.linspace(5, 40, 500)

# Hitung nilai interpolasi untuk setiap x dalam rentang menggunakan kedua metode
y_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_plot]
y_newton = [newton_interpolation(x, y, xi) for xi in x_plot]

# Plot hasil interpolasi
plt.figure(figsize=(12, 6))
plt.plot(x_plot, y_lagrange, label='Interpolasi Lagrange', linestyle='-', color='blue')
plt.plot(x_plot, y_newton, label='Interpolasi Newton', linestyle='--', color='red')
plt.scatter(x, y, color='black', zorder=5, label='Data Asli')

# label dan judul
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Grafik Hasil Interpolasi Lagrange dan Newton')
plt.legend()
plt.grid(True)

# Tampilkan plot
plt.show()
