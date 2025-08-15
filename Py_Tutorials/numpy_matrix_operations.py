import numpy as np
#Sales for quarter 1 (matrix 1)
#Rows represent products, columns regions

q1 = np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])

#Sales for quarter 2 (matrix 2)
q2 = np.array([[150, 250, 350], [450, 550, 650], [750, 850, 950]])

#Total sales for both quarters
total_sales = q1 + q2
print(total_sales)

#Total growth from Q1 to Q2
growth = q2 - q1
print(growth)

# Percentage growth from Q1 to Q2
percentage_growth = (growth / q1) * 100
print(percentage_growth)

# Revenue per product (assuming fixed prices)
# Prices for products in rows, regions in columns
prices = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
revenue_q1 = q1 * prices
print(revenue_q1)

# Total discounts for Q1 (20% discount)
discounted_sales_q1 = revenue_q1 * 0.2
print(discounted_sales_q1)

# Total revenue after discount
total_revenue_after_discount_q1 = revenue_q1 - discounted_sales_q1
print(total_revenue_after_discount_q1)

# Total discounts
total_discounts_q1 = np.sum(discounted_sales_q1)
print(total_discounts_q1)

#total revenue after discount
total_revenue_after_discount = np.sum(total_revenue_after_discount_q1)
print(total_revenue_after_discount)

# House Prices determination
features = np.array([[2000, 3], #House 1: 2000 sqft, 3 bedrooms
                    [1800,2]]) #House 2: 1800 sqft, 2 bedrooms

weights = np.array([150, 10000]) #Price per sqft and per bedroom

#Total price calculation
prices = np.dot(features, weights) #Dot product to calculate prices like 2000*150 +3*10000
print(prices)

# cross product of two vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
cross_product = np.cross(vector1, vector2)
print(cross_product)
