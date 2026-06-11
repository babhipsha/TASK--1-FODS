# 6. Fibonacci Sequence: Write a program to display the Fibonacci sequence up to a
# user-defined number of terms. The program should also output the sum of the
# sequence generated.

terms = int(input("Enter number of terms: "))

a = 0
b = 1
sum_series = 0

print("Fibonacci Sequence:")

for i in range(terms):
    print(a, end=" ")
    sum_series += a
    c = a + b
    a = b
    b = c

print("\nSum of sequence =", sum_series)
