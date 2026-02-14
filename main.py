from src.data_loader import load_transactions

df= load_transactions('data/transactions.xlsx')
print(df.head())

