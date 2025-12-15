p = float(input("Enter principal amount: "))
t = float(input("Enter time in years: "))
r = float(input("Enter rate of interest: "))

amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest =", ci)
