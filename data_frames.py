import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101) #get the same random number

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print(df['W'])
print(type(df['W'])) # -> Series - can also use:    df.W
print(df[['W', 'Z']])

df['new'] = df['W'] + df['Y']
print(df)

df.drop('new', axis=1, inplace=True) #for removing column, inplace=True to actually drop data
print('Dropped :')
print(df)
df.drop('E', axis=0, inplace=True)
print(df)
print(df.shape)

#Selecting rows:
print(df.loc['C']) #returns series
print(df.iloc[2])

print(df.loc['B', 'Y'])
print(df.loc[['A', 'B'], ['W', 'Y']])

#Conditional Selection
print(df > 0)
booldf = df > 0
print(df[booldf])

print(df[df['W'] > 0])
print(df[df['W'] > 0]['X'])
print(df[(df['W'] > 0) & (df['Y'] > 1)]) # use '&' instead of 'and'
# operators: &, |

print(df)
# df.reset_index(inplace=True)
# print('Reset table:')
# print(df)

new_ind = 'CA NY OR CO'.split()
print(new_ind)
df['States'] = new_ind
print(df)
df.set_index('States', inplace=True)
print(df)

#Multi-Level Index -> Index hierarchy
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df)
print(df.loc['G1'].loc[1]) #from outside to nside
df.index.names = ['Groups', 'Num']
print(df)
print(df.loc['G2'].loc[2]['B'])

#cross-section function - xs
df.xs('G1') #has the ability to skip or go inside a multi-level index
df.xs(1, level='Num')
