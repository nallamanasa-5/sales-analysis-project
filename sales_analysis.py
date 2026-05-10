import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# LOAD DATASET
# -----------------------------------

df = pd.read_csv("sales.csv",encoding='latin1')

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# -----------------------------------
# DISPLAY BASIC INFORMATION
# -----------------------------------

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATASET INFO")
print(df.info())

# -----------------------------------
# CHECK MISSING VALUES
# -----------------------------------

print("\nMISSING VALUES")
print(df.isnull().sum())

# Fill missing values
df.fillna(0, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# -----------------------------------
# STATISTICAL SUMMARY
# -----------------------------------

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# -----------------------------------
# TOTAL SALES & PROFIT
# -----------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTOTAL SALES:", total_sales)
print("TOTAL PROFIT:", total_profit)

# -----------------------------------
# REGION-WISE SALES
# -----------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

print("\nREGION WISE SALES")
print(region_sales)

# -----------------------------------
# CATEGORY-WISE SALES
# -----------------------------------

category_sales = df.groupby("Category")["Sales"].sum()

print("\nCATEGORY WISE SALES")
print(category_sales)

# -----------------------------------
# TOP 5 SUB-CATEGORIES BY SALES
# -----------------------------------

top_products = df.groupby("Sub-Category")["Sales"].sum() \
                 .sort_values(ascending=False) \
                 .head(5)

print("\nTOP 5 SUB-CATEGORIES")
print(top_products)

# -----------------------------------
# TOP 5 PROFITABLE SUB-CATEGORIES
# -----------------------------------

top_profit_products = df.groupby("Sub-Category")["Profit"].sum() \
                        .sort_values(ascending=False) \
                        .head(5)

print("\nTOP 5 PROFITABLE SUB-CATEGORIES")
print(top_profit_products)

# -----------------------------------
# SAVE CLEANED DATASET
# -----------------------------------

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCLEANED DATASET SAVED SUCCESSFULLY")

# ===================================
# VISUALIZATIONS
# ===================================

# -----------------------------------
# BAR CHART - REGION SALES
# -----------------------------------

plt.figure(figsize=(8,5))

region_sales.plot(kind="bar")

plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()

# -----------------------------------
# BAR CHART - CATEGORY SALES
# -----------------------------------

plt.figure(figsize=(8,5))

category_sales.plot(kind="bar")

plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# -----------------------------------
# PIE CHART - TOP SUB-CATEGORIES
# -----------------------------------

plt.figure(figsize=(7,7))

top_products.plot(kind="pie", autopct='%1.1f%%')

plt.title("Top 5 Sub-Categories Sales Share")
plt.ylabel("")

plt.show()

# -----------------------------------
# HISTOGRAM - SALES DISTRIBUTION
# -----------------------------------

plt.figure(figsize=(8,5))

df["Sales"].plot(kind="hist", bins=10)

plt.title("Sales Distribution")
plt.xlabel("Sales")

plt.show()

# ===================================
# BUSINESS INSIGHTS
# ===================================

print("\nBUSINESS INSIGHTS")

print("\n1. Highest Sales Region:")
print(region_sales.idxmax())

print("\n2. Best Selling Sub-Category:")
print(top_products.idxmax())

print("\n3. Most Profitable Sub-Category:")
print(top_profit_products.idxmax())

print("\n4. Total Revenue Generated:")
print(total_sales)

print("\n5. Total Profit Generated:")
print(total_profit)