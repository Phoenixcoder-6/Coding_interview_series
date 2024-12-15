import pandas as pd

transaction= [
    {"user_id": 1, "product": "Laptop", "amount": 1000},
    {"user_id": 2, "product": "Phone", "amount": 500},
    {"user_id": 1, "product": "Headphones", "amount": 200},
    {"user_id": 3, "product": "Laptop", "amount": 1000},
    {"user_id": 2, "product": "Tablet", "amount": 300},
    {"user_id": 4, "product": "Phone", "amount": 500},
    {"user_id": 1, "product": "Laptop", "amount": 1000},
    {"user_id": 3, "product": "Mouse", "amount": 50},
    {"user_id": 5, "product": "Keyboard", "amount": 70},
    {"user_id": 2, "product": "Headphones", "amount": 200},
]

df= pd.DataFrame(transaction)
user_spending = df.groupby('user_id')['amount'].sum().reset_index()
top_5_users = user_spending.sort_values(by='amount', ascending=False).head(5)
most_purchased_product= df['product'].value_counts().idxmax()
most_purchased_count=df['product'].value_counts().max()

print("Total Spending Per User:")
print(user_spending)

print("\n Top 5 Users by Spending:")
print(top_5_users)

print(f"\nMost Purchased Product: {most_purchased_product} (Purchased {most_purchased_count} times)")


