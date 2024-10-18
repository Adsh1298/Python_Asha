import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("phone_data.csv")

df=pd.DataFrame(data)
print(df.describe())
#Price Distribution

plt.figure(figsize=(8,4))
sns.histplot(df['Price'],bins=5, kde=True, color='green')
#sns.histplot(df['Price'],bins=5, kde=True, color='green')

plt.title("Price Distribution")
plt.xlabel("Price:")
plt.ylabel("Frequency")
plt.show()

#Price vs. Rating:
plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x="Price",y="Rating",sizes=(50,200))
plt.title("Price vs. Rating")
plt.xlabel("Price: ₹")
plt.ylabel("Rating: ")
plt.show()
data1=["Player1","Player2","Player3"]
values=[30, 45, 25]
plt.figure(figsize=(8,6))
#sns.barplot(data=df,x="Price",y="Rating")
plt.pie(values,labels=data1)
plt.show()

###########using Bar graph###############
data1=['India','US','Japan','China']
values=[40,20,10,67]
plt.xlabel("Countries")
plt.ylabel("Sales")
plt.show()

##################using line graph##########################
###Get stock price of Apple:
apple_stock = yf.download("AAPL", start="2024-01-01", end="2024-10-01")
ms_stock = yf.download("MSFT", start="2024-01-01", end="2024-10-01")

plt.plot(apple_stock.index, apple_stock["Close"], label="Apple", marker='o')
plt.plot(ms_stock.index, ms_stock["Close"], label="Microsoft", marker='s')

plt.xlabel("Date")
plt.ylabel("Srock Price: ")
plt.title("Stock Prices of top S/w Companies")
plt.legend()

plt.show()



