amount = float(input("Enter your amount: "))
number_of_years = int(input("Enter the years: "))
interest_rate = float(input("enter your interest rate: "))

#count = 1

print("Year \t Rate \t ROI")
for count in range(0,number_of_years) :

    rate_on_roi = (interest_rate / 100) * amount
    roi = rate_on_roi + amount
    amount = roi
    print(f"{count + 1}\t {interest_rate}\t{amount}")
  
   
