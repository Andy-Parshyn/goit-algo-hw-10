import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# 1. Визначення функції та меж
def f(x):
    return x ** 2

a = 0
b = 2

# 2. Налаштування методу Монте-Карло
N = 15000
x_rand = np.random.uniform(a, b, N)
y_max = f(b) # f(2) = 4
y_rand = np.random.uniform(0, y_max, N)

# 3. Перевірка умови (чи точка під кривою)
under_curve = y_rand < f(x_rand)

# 4. Обчислення площі
count_under = np.sum(under_curve)
area_rect = (b - a) * y_max
integral_mc = (count_under / N) * area_rect

# Теоретичне (точне) значення інтеграла
integral_exact = 8 / 3

# Значення інтреграла згідно 'quad'
result,error = spi.quad(f,a,b)

print(f'Обчислене значення (Монте-Карло): {integral_mc:.5f}')
print(f'Точне значення: {integral_exact:.5f}')
print(f'Похибка: {abs(integral_mc - integral_exact):.5f}')
print(f'Значенння (quad): {result:.5f}')
print(f'Похибка (quad): {error:.5f}')

# --- ВІЗУАЛІЗАЦІЯ ---

x_line = np.linspace(-0.5, 2.5, 400)
y_line = f(x_line)
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x_line, y_line, 'k', linewidth=2, label='f(x) = x^2')

# Точки під кривою - зелені, над кривою - червоні
ax.scatter(x_rand[under_curve], y_rand[under_curve], color='green', s=1, alpha=0.3, label='Під кривою')
ax.scatter(x_rand[~under_curve], y_rand[~under_curve], color='red', s=1, alpha=0.3, label='Над кривою')

ax.set_xlim([x_line[0], x_line[-1]])
ax.set_ylim([0, y_max + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.legend()
ax.set_title(f'Метод Монте-Карло: N={N}\nРезультат: {integral_mc:.4f}')

plt.grid(True)
plt.show()