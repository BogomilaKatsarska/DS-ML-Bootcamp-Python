import pandas as pd

sal = pd.read_csv('Salaries.csv')
print(sal.head[2])
print(sal.inf())
print(sal['BasePay'].mean())
print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])
print(sal.loc[sal['TotalPayBenefits'].idxmax()])
print(sal.iloc[sal['TotalPayBenefits'].argmin()])
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()])
print(sal.groupby('Year').mean()['BasePay'])
print(sal['JobTitle'].nunique())
print(sal['JobTitle'].value_counts().head(5))
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))


def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False


print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['TotalPayBenefits', 'title_len']].corr())

