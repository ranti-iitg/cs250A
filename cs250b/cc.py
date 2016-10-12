from load import mnist
import numpy as np
from math import sqrt
A=[0,0]
B=[3,4]

print sqrt(sum( (a - b)**2 for a, b in zip(A, B)))
