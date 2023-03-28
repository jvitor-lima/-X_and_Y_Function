import numpy as np
import matplotlib.pyplot as plt

def input_function():
    print("EX: -x*y*np.exp(-x**2-y**2) | np.sin(x*y)")
    funcao_xy = input("Digite a função: ")
    return funcao_xy

print("Digite os valores iniciais e finais de x e y:")
x_min = float(input("Digite o valor inicial de x: "))
x_max = float(input("Digite o valor final de x: "))
y_min = float(input("Digite o valor inicial de y: "))
y_max = float(input("Digite o valor final de y: "))

x = np.linspace(x_min, x_max)
y = np.linspace(y_min, y_max)
x, y = np.meshgrid(x, y)

funcao_xy = input_function()

z = eval(funcao_xy)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(1, 2, 1, projection="3d")
ax.plot_surface(x, y, z, cmap="coolwarm")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax = fig.add_subplot(1, 2, 2)
ax.contour(x, y, z, cmap="coolwarm")
ax.set_xlabel("X")
ax.set_ylabel("Y")

plt.show()