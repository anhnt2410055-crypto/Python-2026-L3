import math
r = float (input("Enter circle radius? "))
area = math.pi * (r ** 2)
print(f"Circle area ={area}")
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius * 9/5) + 32
c_display = int(celsius) if celsius.is_integer() else celsius
print(f"{c_display} (C) = {fahrenheit:.1f} (F)")
number = int(input("Enter a number? "))
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) +1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"(number) is a NOT prime number")
number = int(input("Enter a number? "))
divisors_sum = sum(i for i in range(1, number) if number % i == 0)
if number > 1 and divisors_sum == number:
    print(f"(number) is a perfect number")
else:
    print(f"(number) is a NOT perfect number")
colors = ["Blue", "Green", "Red", "Yellow", "Orange"]
favorite_color = input("What is your favorite colors? ").strip()
if favorite_color in colors:
    index = colors.index(favorite_color)
    print(f"Your color is at index {index} in the list")
else:
    print("Sorry, I could not find your color")
range1 = list(range(0, 7))
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -3, -2))

print("range1:", ", ".join(map(str, range1)))
print("range2:", ", ".join(map(str, range2)))
print("range3:", ", ".join(map(str, range3)))
print("range4:", ", ".join(map(str, range4)))
def remove_dollar_sign(s):
    return s.replace("$", "")

text = input("Enter a string: ")
result = remove_dollar_sign(text)

print(f"Result: {result}")
def extract_even(l):
    return [x for x in l if x % 2 == 0]

numbers = [1, 4, 5, -1, 10]
even_numbers = extract_even(numbers)

print(f"Even numbers: {even_numbers}")
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a non-negative integer: "))

print(f"The factorial of {num} is {factorial(num)}")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"Distance between two points: {distance:.2f}")
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

m = int(input("Enter m (rows): "))
n = int(input("Enter n (columns): "))
print_pattern(m, n)
