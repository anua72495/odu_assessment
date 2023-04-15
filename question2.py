#You can use Pandas library to read the csv file and create a DataFrame object.
# a.Calculate Average Price
#To calculate the average price of autos, you can use the mean() function of the pandas library.

#b.Print Different Possible Vehicle Types
#To print the list of different possible types of VehicleType found in the dataset, you can use the unique() function of the pandas library.

#c.Calculate Lowest and Highest Year of Registration
#To calculate the lowest and highest year of registration, you can use the min() and max() functions of the pandas library.

#d.Calculate Standard Deviation of Column Kilometer
#To calculate the standard deviation of column kilometer, you can use the std() function of the pandas library.

#e.Draw a Bar Graph to Represent Count of Different Types of Column Brand
#To draw a bar graph to represent the count of different types of column brand, you can use the value_counts() function of the pandas library and then plot the resulting data using the plot.bar() function.

#f.Find and Print Which VehicleType is Sold Minimum and Maximum
#To find which VehicleType is sold minimum and maximum, you can use the value_counts() function of the pandas library and then find the minimum and maximum values using the min() and max() functions.

#The code below explains all the above steps

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("autos.csv", encoding="latin-1")

# Find the average price of autos
average_price = df["price"].mean()
print("Average price of autos: ", average_price)

# Print the list of different possible types of VehicleType found in dataset
vehicle_types = df["vehicleType"].unique()
print("Vehicle types: ", vehicle_types)

# Calculate and print lowest yearOfRegistration and highest yearOfRegistration
min_year = df["yearOfRegistration"].min()
max_year = df["yearOfRegistration"].max()
print("Lowest year of registration: ", min_year)
print("Highest year of registration: ", max_year)

# Find and print standard deviation of column kilometer
std_kilometer = df["kilometer"].std()
print("Standard deviation of kilometer: ", std_kilometer)

# Draw a bar graph to represent count of different type of column brand
brand_count = df["brand"].value_counts()
brand_count.plot(kind="bar")
plt.title("Count of different brands")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.show()

# Find out which VehicleType is sold minimum and maximum
min_vehicle_type = df["vehicleType"].value_counts().idxmin()
max_vehicle_type = df["vehicleType"].value_counts().idxmax()
print("Vehicle type sold minimum: ", min_vehicle_type)
print("Vehicle type sold maximum: ", max_vehicle_type)

# Create a pie chart to represent different types of gearbox count
gearbox_count = df["gearbox"].value_counts()
gearbox_count.plot(kind="pie")
plt.title("Gearbox count")
plt.show()







