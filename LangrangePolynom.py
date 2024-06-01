import numpy as np
import matplotlib.pyplot as plt

x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def lagrange_interpolation(x_values, y_values, x_point):
    def basis(j):
        p = [(x_point - x_values[m]) / (x_values[j] - x_values[m]) for m in range(len(x_values)) if m != j]
        return np.prod(p, axis=0)

    return sum(y_values[j] * basis(j) for j in range(len(x_values)))

x_plot = np.linspace(5, 40, 100)
y_plot_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_plot]

def test_lagrange_interpolation():
    test_x = np.array([7, 12, 18, 28, 33, 38])
    test_y = [lagrange_interpolation(x, y, xi) for xi in test_x]
    return test_x, test_y

test_x, test_y = test_lagrange_interpolation()

plt.plot(x_plot, y_plot_lagrange, label="Interpolasi Lagrange")
plt.scatter(x, y, color='red', label='Titik Data')
plt.scatter(test_x, test_y, color='blue', label='Titik Interpolasi', marker='x')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)
plt.show()

for i, xi in enumerate(test_x):
    print(f'Interpolasi pada x = {xi}: y = {test_y[i]}')
