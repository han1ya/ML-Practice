import numpy as np
import pandas as pd
from sklearn import linear_model

#read the data file into filename
filename = "house.csv"
#create a dataframe and read the house data file into it
df = pd.read_csv(filename)

df.head()
#extract these 2 columns from the df and store them in respective new arrays
#resize the arrays to be a single column which is the shape taken by LinearRegression()
size=np.array(df['LOT_SQFT']).reshape(-1, 1)
price=np.array(df['TOTAL_VALUE']).reshape(-1,1)

#create a linear regression model and train it using fit()
#where size array is the input and price array is the output
model = linear_model.LinearRegression()
#fit() finds the best-fitting line that minimizes residual sum of squares (RSS)
model.fit(size, price)

#prints the df in descending order by TOTAL_VALUE
print("HOME PRICES")
print(df.sort_values('TOTAL_VALUE', ascending=False))

#prompt user for input, if input is a negative number, exit
#if not, predicted hosue price is calculated, converted to a float,
#multiplied by 1000, rounded to 2 dec places, and printed to the console.
while True:
  sqr_ft =  float(input("please enter the square foot home you are looking for: "))
  if sqr_ft < 0:
    print("exiting now... \n\n")
    break
  else:
    HousePrice = model.predict(np.array(sqr_ft).reshape(-1,1))
    HousePrice = float(HousePrice)
    HousePrice *= 1000
    HousePrice = round(HousePrice, 2)
    print("\n For a home that is {} square foot, should sell for ${}".format(sqr_ft, HousePrice))
    print("\n\n")
