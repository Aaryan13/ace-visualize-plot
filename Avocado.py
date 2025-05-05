import pandas as pd
a = pd.read_csv("/home/aaryan/Documents/avocado.csv")

# Printing the Database contents Normally
# print(a)

# Printing out just the first 4 columns from the Database
# print(a.head())

# Printing out just the last 4 columns from the Database
# print(a.tail())

# Calling out a column from the Database, by this method only that particular column will show on screen
# print(a.AveragePrice)

# Don't use this as it is confusing between column name and variable name
# print(a.AveragePrice.head())

# Always use this method to call out specific columns from the Database
# avg_price = a["AveragePrice"].head()

# Specifying a column to print, we'll now try to print avocados which are only sold in the Albany Region
# albany_a=a[a['region'] == "Albany"]
# print(albany_a.head())

# Removing an Extra column of index in our Database and setting 'DATE' as an Index instead of a sole Index column
# print(a.set_index("Date"))
# More Coder Way to do the Above Statement
# avo_date=a.set_index("Date")
# print(avo_date.head())

# Plotting our data on a graph. This particular database has incorrect order of entries so it's not the accurate plot
# avo_plot = a['AveragePrice'].plot()
# print(avo_plot)
