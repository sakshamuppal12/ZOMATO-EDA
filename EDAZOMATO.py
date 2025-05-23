import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\Saksham\OneDrive\Desktop\zomato (1).csv", encoding='latin1') 
df.head()


df.info()


df.describe()



top_cities = df['City'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index,hue=top_cities.index, palette="magma", dodge=False, legend=False)
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.tight_layout()
plt.show()



cuisine_split = df['Cuisines'].dropna().str.split(', ').explode()
top_cuisines = cuisine_split.value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cuisines.values, y=top_cuisines.index)
plt.title("Top 10 Most Common Cuisines")
plt.xlabel("Frequency")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.show()



online_delivery = df['Has Online delivery'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(online_delivery, labels=online_delivery.index, autopct='%1.1f%%', colors=sns.color_palette("cool"))
plt.title("Online Delivery Availability")
plt.tight_layout()
plt.show()



table_booking = df['Has Table booking'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(table_booking, labels=table_booking.index, autopct='%1.1f%%', colors=sns.color_palette("Set2"))
plt.title("Table Booking Availability")
plt.tight_layout()
plt.show()



plt.figure(figsize=(8, 5))
sns.histplot(df['Aggregate rating'], bins=20, kde=True, color='skyblue')
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()



plt.figure(figsize=(8, 5))
sns.boxplot(x='Price range', y='Aggregate rating', data=df)
plt.title("Price Range vs Aggregate Rating")
plt.tight_layout()
plt.show()



plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Average Cost for two'])
plt.title("Boxplot of Average Cost for Two")
plt.tight_layout()
plt.show()



plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
