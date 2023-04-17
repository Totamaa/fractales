import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange, tqdm

# Taille de l'image
SIZE = 5000

# Définir les paramètres de la fractale
xmin, xmax = -2.0, 0.5
ymin, ymax = -1.25, 1.25
radius = 2
max_iter = int(SIZE * np.log(SIZE))  # max_iter varie en fonction de la taille

# Générer les coordonnées des points dans la grille
x = np.linspace(xmin, xmax, SIZE)
y = np.linspace(ymin, ymax, SIZE)
X, Y = np.meshgrid(x, y)

# Initialiser la matrice de couleurs
colors = np.zeros_like(X, dtype=int)

# Calculer la fractale
with tqdm(total=SIZE) as pbar:
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            c = complex(X[i,j], Y[i,j])
            z = complex(0, 0)
            for k in range(max_iter):
                if abs(z) > radius:
                    colors[i,j] = k
                    break
                z = z*z + c
        pbar.update(1)

# Afficher l'image
plt.figure(figsize=(8,8))
plt.imshow(colors, cmap='twilight_shifted')
plt.axis('off')
plt.show()
