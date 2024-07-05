import pandas as pd

data = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350],
}
df = pd.DataFrame(data)
print(df)
by_company = df.groupby('Company') #pandas automatically ignores non-numeric column
print(by_company.mean())
print(by_company.sum())
#.count() returns the numbers of instances
#transpose is used to create diff format - FB, GOOG and MSFT to be names of rows
print(df.groupby('Company').describe().transpose()) #gives a bunch of info: count, mean, std, min, max, 25%, 50%, etc.