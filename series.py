#Series - can be indexed by a label
import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {
    'a': 10,
    'b': 20,
    'c': 30,
}
print(pd.Series(data=my_data))
print(pd.Series(data=my_data, index=labels))
print(pd.Series(arr))
print(pd.Series(d))
ser1 = pd.Series([1, 2, 3, 4], ['USA', 'DE', 'BG', 'UK'])
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'IT', 'CA', 'DE'])
print(ser1['USA'])
print(ser1 + ser2)