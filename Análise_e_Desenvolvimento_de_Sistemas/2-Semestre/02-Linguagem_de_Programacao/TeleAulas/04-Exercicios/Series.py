import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

print(s)

d = {'b':1, 'a':0, 'c':2}
print(d)

sd=pd.Series(d)
print(sd)