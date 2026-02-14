from src.data_loader import load_transactions

df= load_transactions("data/transactions.xlsx")

print("first 5 rows of the transactions data:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nInfo:")
print(df.info())

