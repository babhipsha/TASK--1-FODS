# 8. Input Validation (Palindrome): Write a program that asks the user to enter a 5-digit
# positive integer. Validate the input to ensure it is exactly 5 digits and positive. If
# valid, determine if the number is a palindrome (reads the same forwards and
# backwards).

number = input("Enter a 5-digit positive integer: ")

if number.isdigit() and len(number) == 5:
    if number == number[::-1]:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
else:
    print("Invalid input. Enter exactly 5 digits.")
