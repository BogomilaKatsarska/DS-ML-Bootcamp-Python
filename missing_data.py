import numpy as np
import pandas as pd

d = {
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1, 2, 3],
}

df = pd.DataFrame(d)
print(df)

# df.dropna(inplace=True) #if axis=1 => it drops the cols with NaN; thresh=2(has at least 2NaN values)
# print(df)

#replacing NaN-s
df.fillna(value='FILL VALUE', inplace=True)
print(df)
# fill with the 'mean' of the value:
df['A'].fillna(value=df['A'].mean())
