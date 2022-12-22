
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
split = float(input("How many people to split the bill?"))

math = ( bill / 5 ) * (1+ tip * 0.1)
math = round(math,2)
print(f"Each person should pay: {math}" )