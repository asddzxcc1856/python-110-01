import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dic = {
    "col 1": [1, 2, 3], 
    "col 2": [10, 20, 30],
    "col 3": list('xyz'),
    "col 4": ['a', 'b', 'c'],
    "col 5": pd.Series(range(3))
}
df = pd.DataFrame(dic)
print(df)

a = np.arange(10)

print(a)

print(1)