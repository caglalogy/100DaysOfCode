print("Welcome to the tip calculator.") 
total_bill = float(input("What was the total bill? "))
people_count = int(input("How many people to split the bill? "))
percentage_by_person = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

splitted_bill = float(total_bill/people_count)
tip = float(splitted_bill * percentage_by_person/100)
result = round(splitted_bill + tip,2)

print(f"Each person should pay: ${result}")