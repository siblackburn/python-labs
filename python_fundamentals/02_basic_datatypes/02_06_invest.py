'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment = int(input("Enter the amount to invest "))
interest_rate = int(input("what is the interest rate? "))
rate = interest_rate / 100
years = int(input("how many full years do you want to invest? "))

final_value = investment*((1+rate)**years)

print("The future value of your investment is $", round(final_value,0))