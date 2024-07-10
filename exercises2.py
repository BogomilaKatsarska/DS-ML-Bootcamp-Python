import pandas as pd

ecom = pd.read_csv('Ecommerce Purchases')
print(len(ecom.columns))
print(ecom.info())
print(ecom['Purchase Price'].mean())
print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())
print(sum(ecom['Language'] == 'en'))
print(ecom[ecom['Language'] == 'en']['Language'].count())
print(ecom[ecom['Job'] == 'Lawyer'].count())
print(ecom['AM or PM'].value_counts())
print(ecom['Job'].value_counts().head(5))
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])
print(ecom[ecom['Credit Card'] == '83972472093']['Email'])
print(ecom[(ecom['CC Provider'] == 'Americal Express') & (ecom['Purchase Price'] > 95)].count())
print(sum(ecom['CC Exp Date'].apply(lambda exp: exp[3] == 25)))
print(ecom['Email'].apply(lambda email: email.split("@")[1]).value_counts().head(5))


