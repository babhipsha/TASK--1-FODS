# 7. Pattern Filtering: Write a program to find all numbers between 500 and 1500
# (inclusive) that are multiples of 7 but not multiples of 5. Allow the user to define
# their own custom range for this search.

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Numbers divisible by 7 but not by 5:")

for number in range(start, end + 1):
    if number % 7 == 0 and number % 5 != 0:
        print(number, end=" ")
