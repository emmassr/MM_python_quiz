# For this exercise you will need the Pandas package. You can import this using:

#Q1: Create a Pandas dataframe with 3 columns: User, Fruit and Quantity.
#Insert Junaid, Tom, Dick, Harry as Users.
#Insert Apple, Oranges, Bananas, Mango as Fruit
#Insert 4, 3, 11, 7 as Quantity
#Each user should have their own row, this table should have 4 rows, you may name this dataframe what you like.
import pandas as pd
data = [['Junaid', 'Apple',4 ], ['Tom', 'Oranges', 3], ['Dick', 'Bananas', 11], ['Harry', 'Mango', 7]]
df = pd.DataFrame(data, columns=['User', 'Fruit', 'Quantity'])
#df = pd.DataFrame({'Users': ['Junaid', 'Tom', 'Dick', 'Harry'], 'Fruit' : ['Apple', 'Oranges', 'Bananas', 'Mango'], 'Quantity': [4,3,11,7]})
#print(df)

#Q2: Read in the transactions CSV file into Python, call this df and print the first 5 rows
csv_file = pd.read_csv("transactions.csv")
#print(csv_file.head(5))

#Q3: List the column names in the df dataframe. Express the answer as a list
#new_df_list = list(df)
#print(new_df_list)

#Q4: Count the number of rows in the dataframe
total_rows = len(csv_file)
print(total_rows)

#Q5: How many unique customer ids do we have?
print(len(csv_file.customer_id.unique()))

## Q6: What is the minimum value, maximum value, mean value and median value for the price column
print(csv_file.price.describe())

# Q7: Filter the dataframe so that only the transactions for customer_id 'ABC' are returned. Call this ABC_df
ABC_df = csv_file[csv_file.customer_id == 'ABC']
print(ABC_df)

# Q8: Filter the dataframe so that only the transactions with quantity more than 10 are returned and occurred later than the 1st of January
new_filter = csv_file[(csv_file.quantity > 10) & (csv_file.date >= '02/01/2020')]
print(new_filter)

# Q9: How many rows are there in df where the price more than £10? Note: Pounds only, ignore the pence
print(len(csv_file[csv_file.price >10]))

# Q10: Add a new column to df where you multiply price and quantity - call this revenue
csv_file['revenue'] = csv_file['price'] * csv_file['quantity']
print(csv_file)

# Q11: Add a new column to df where you report the price in pounds only E.g. 12.05 becomes 12. Round up to the nearest pound - call this price_pounds. Hint: look up ceiling function
import numpy as np
csv_file['price in pounds'] = np.ceil(csv_file['price'])
print(csv_file)

#Q12: Create an indicator column where True marks if the quantity is a multiple of 2
# and False otherwise - call this quantity_indicator Hint: Look at Numpy Select and or Lambda functions