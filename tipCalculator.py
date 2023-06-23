#1-Welcome to the tip calculator.
print("Welcome to the tip calculator")

#2-What was the total bill?
bill = float(input("What was the total bill? : "))

#3-What percentage tip would you like to give ? 10, 12, 15?
tipPercentage = int(input("What percentage tip would you like to give? \n10, 12, 15 ? \n"))

#4-How many people to split the bill ?
payPeople = int(input("How many people to split the bill? \n"))

#5-Bill and percentage
totalBill = bill + ((bill * tipPercentage) / 100 )

#6-Each person should pay: 
perPerson = round(totalBill / payPeople, 2)
print(f"Each person should pay : {perPerson} TL")
