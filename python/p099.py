# Largest exponential

import os
import numpy as np

matrix = np.loadtxt(os.path.join("..", "data", "p099.txt"),
                    delimiter=",", dtype=np.uint64)

print(np.argmax(matrix[:, 1] * np.log10(matrix[:, 0])) + 1)
