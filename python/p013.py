# Large sum

import os
import numpy as np

matrix = np.loadtxt(os.path.join("..", "data", "p013.txt"), dtype=object)

print(str(sum(int(n) for n in matrix))[:10])
