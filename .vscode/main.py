import numpy as np
import matplotlib.pyplot as plt

# Parameter
L = 1.0          # Länge
E = 210e9        # Elastizitätsmodul (Pa)
A = 0.01         # Querschnitt
F = 1000         # Kraft (N)
n = 5            # Anzahl Elemente

# Diskretisierung
nodes = np.linspace(0, L, n+1)
h = L / n

# Steifigkeitsmatrix
K = np.zeros((n+1, n+1))
f = np.zeros(n+1)

# Elementmatrix
k_local = (E*A/h) * np.array([[1, -1], [-1, 1]])

# Assembly
for i in range(n):
    K[i:i+2, i:i+2] += k_local

# Randbedingungen
K[0, :] = 0
K[0, 0] = 1
f[0] = 0

f[-1] = F

# Lösen
u = np.linalg.solve(K, f)

# Plot
plt.plot(nodes, u, marker='o')
plt.title("FEM Verschiebung")
plt.xlabel("Position")
plt.ylabel("Verschiebung")
plt.grid()
plt.show()