import matplotlib.pyplot as plt

x = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
y = [0.401651656746949, 0.367180273279436, 0.361519702953281, 0.362547551222806, 0.366431488868316, 0.372167903223974, 0.377063565226695, 0.386809261803106, 0.392733584930759, 0.388797803005541]

x.reverse()
y.reverse()

plt.plot(x, y, marker='o')
plt.xlabel('Mach')
plt.ylabel('Drag coefficient')
plt.title('Drag coefficient vs Mach for R5A')
plt.grid(True)
plt.show()

