import math 

# Display a menu of options for the user to choose from
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
print ()

calculation_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Convert to lowercase so any capitalization will not affect the input
calculation_type = calculation_type.lower()

# Investment option
  # Ask the user to input the deposit amount, interest rate (number only), and number of years they plan
if calculation_type == "investment":
    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a number only): "))
    years = int(input("Enter the number of years you plan on investing for: "))
    interest = input("Enter either 'simple' or 'compound' interest: ")
    r = interest_rate / 100

    # Calculate simple interest and compound interest.
    # Simple interest formula: A = P(1 + r X t); Compound interest formula: A = P(1 + r) ** t
    if interest == "simple":
        total_amount = deposit * (1 + r * years)
        print(f"The total amount after {years} years with simple interest will be: {total_amount:.2f}")
    elif interest == "compound":
        total_amount = deposit * math.pow(1 + r, years)
        print(f"The total amount after {years} years with compound interest will be: {total_amount:.2f}")
    
elif calculation_type == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (as a number only): "))
    months = int(input("Enter the number of months you plan on repaying the bond: "))
    # Converting annual interest rate to monthly interest rate
    r = interest_rate / 100 / 12  

    # Calculate bond repayment
    # Bond repayment formula: repayment = (i * P) / (1 - (1 + i) ** (-n))
    repayment = (r * present_value) / (1 - math.pow(1 + r, -months))
    print(f"The monthly repayment for the bond will be: {repayment:.2f}")

else:
    # If the user enters an invalid calculation type, display an error message
    print("Invalid calculation type. Please enter either 'investment' or 'bond'.")
