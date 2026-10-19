feild1=120
feild2=85
feild3=150
feild4=95
feild5=110
total =feild1 + feild2 + feild3 + feild4 + feild5
average = total / 5
print("Total harvest :", total, "kg")
print("Average per feild :", total, "kg")
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings : Rs.", earnings)
bags =total//25
leftover = total % 25
print("Full bags packed  :",bags)
print("Laftover grain :", leftover, "kg")
last_year = 500
print("Better than last year?  :", total > last_year)
print("Same as last year?  :", total == last_year)
print("At least as good?  :", total >= last_year)
total += 30
print("After bonus crop :", total, "kg")
total -= 15
print("After seed reserve :", total, "kg")
bags = total // 25
print(" Final bags paacked :", bags)