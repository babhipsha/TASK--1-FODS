# 5. Salary &amp; Tax System: Create a program to input an employee&#39;s gross salary.
# Calculate the net salary after applying the following tax rules:
#  Tax-Free: Below £12,500
#  20% Tax: £12,501 – £50,000
#  40% Tax: £50,001 – £125,000
#  45% Tax: Above £125,000

salary = float(input("Enter gross salary: "))

if salary < 12500:
    tax = 0
elif salary <= 50000:
    tax = salary * 0.20
elif salary <= 125000:
    tax = salary * 0.40
else:
    tax = salary * 0.45

net_salary = salary - tax

print("\nSalary Details")
print("--------------------")
print("Gross Salary =", salary)
print("Tax Amount =", tax)
print("Net Salary =", net_salary)
