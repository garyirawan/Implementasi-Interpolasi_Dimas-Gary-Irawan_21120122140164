import numpy as np
import matplotlib.pyplot as plt

x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def divided_diff(x_values, y_values):
    n = len(y_values)
    coef = np.zeros([n, n])
    coef[:, 0] = y_values
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x_values[i + j] - x_values[i])
    
    return coef[0, :]

def newton_interpolation(x_values, y_values, x_point):
    coef = divided_diff(x_values, y_values)
    n = len(coef)
    y_interp = coef[0]
    for i in range(1, n):
        y_interp += coef[i] * np.prod([x_point - x_values[j] for j in range(i)])
    return y_interp

x_plot = np.linspace(5, 40, 100)
y_plot_newton = [newton_interpolation(x, y, xi) for xi in x_plot]

def test_newton_interpolation():
    test_x = np.array([7, 12, 18, 28, 33, 38])
    test_y = [newton_interpolation(x, y, xi) for xi in test_x]
    return test_x, test_y

test_x, test_y = test_newton_interpolation()

plt.plot(x_plot, y_plot_newton, label="Interpolasi Newton")
plt.scatter(x, y, color='red', label='Titik Data')
plt.scatter(test_x, test_y, color='blue', label='Titik Interpolasi', marker='x')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)
plt.show()

for i, xi in enumerate(test_x):
    print(f'Interpolasi pada x = {xi}: y = {test_y[i]}')
