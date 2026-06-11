#1. Logic Design: Create a flowchart that illustrates the logic for a Leap Year Checker. The diagram must clearly show the input of a year, the conditional processing steps, and the final output.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
