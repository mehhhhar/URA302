
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")



first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(last_name + " " + first_name)




import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area}")




color_list = ["Red", "Green", "White", "Black"]

print(f"First color: {color_list[0]}, Last color: {color_list[-1]}")




n = input("Enter a number: ")

nn = n + n
nnn = n + n + n

result = int(n) + int(nn) + int(nnn)
print(f"The result of n + nn + nnn is: {result}")




numbers = input("Enter comma-separated numbers: ")

num_list = numbers.split(",")
num_tuple = tuple(num_list)
print(f"List: {num_list}")
print(f"Tuple: {num_tuple}")




celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a

a += 1
print(f"After swapping and incrementing, first number: {a}, second number: {b}")





a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

a += 1

print(f"After swapping and incrementing, first number: {a}, second number: {b}")


num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")



year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")




import math

x1, y1 = map(float, input("Enter coordinates of the first point (x1, y1): ").split())
x2, y2 = map(float, input("Enter coordinates of the second point (x2, y2): ").split())


distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidean distance between the points is: {distance}")




angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))


if angle1 + angle2 + angle3 == 180:
    print("The angles can form a triangle")
else:
    print("The angles cannot form a triangle")




P = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time (in years): "))
n = float(input("Enter the number of times interest is compounded per year: "))


A = P * (1 + r / (100 * n)) ** (n * t)
compound_interest = A - P
print(f"The compound interest is: {compound_interest}")




n = int(input("Enter a number: "))


if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")




N = int(input("Enter a positive integer N: "))


sum_of_squares = sum(i**2 for i in range(1, N+1))
print(f"The sum of squares from 1 to {N} is: {sum_of_squares}")
