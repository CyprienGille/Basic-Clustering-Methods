import matplotlib.pyplot as plt
from scipy.io import arff
# from mpl_toolkits.mplot3d import Axes3D

data, meta = arff.loadarff("Squash.arff")  # C'est le nom de la database sur mon ordi


N = 52  # nb de lignes que l'on veut prendre dans la database

for i in range(N):
    d =  data["Acceptability"][i]
    if d == b"excellent":
        data["Acceptability"][i] = 1
    elif d == b"ok":
        data["Acceptability"][i] = 2
    elif d == b"not_acceptable":
        data["Acceptability"][i] = 3
    


# On a ici choisi des attributs pour l'exemple on va pas se mentir
X = data['weight'][:N]
Y = data['pene'][:N]
Z = data['groundspot_a*'][:N]
C = data["Acceptability"][:N].astype(int)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X, Y, Z, c=C, s=60)

legend1 = ax.legend(*scatter.legend_elements(), title="Classes")
ax.add_artist(legend1)
plt.show()
