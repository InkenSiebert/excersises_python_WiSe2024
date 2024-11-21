import numpy as np

data=np.arange(1,11)


D = np.tile(data, 10).reshape(10,10)
print(D.sum(axis=0))

print(D.mean(axis=1))    #axis1 siehe Folie. geht über Spalten

