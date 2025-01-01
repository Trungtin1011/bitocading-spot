#############################################################################################
# Write a Python program to calculate the area of a rectangle given its length and width
#############################################################################################
def area():
    while True:
        try:
            a: float = float(input("Input number A >> "))
            if a <=0:
                raise ValueError
            b: float = float(input("Input number B >> "))
            if b <= 0:
                raise ValueError
            break
        except ValueError as e:
            print("Please input a valid number!")
            continue
    res = a*b
    print("Area = {:.2f}".format(res)) 

#############################################################################################
# Create a program that takes a user's name and age as input and prints a greeting message
#############################################################################################
def greet():
    name:str = input("Enter your name >> ")   
    while True:
        try:
            age:int = int(input("Please enter your age >> "))
            if age <= 0:
                raise ValueError
            break
        except ValueError as e:
            print("Please input a valid age!")
            continue
    print(f"Greeting {name} {age} years old")

#############################################################################################
# Write a program to check if a number is even or odd
#############################################################################################
def iseven():
    while True:
        try:
            n: int = int(input("Enter a number >> "))
            if n <= 0:
                raise ValueError
            elif n % 2 == 0:
                print("The number is even number!")
            else:
                print("The number is odd number!")
            break
        except ValueError as e:
            print("Please enter the valid number!")
            continue

#############################################################################################
# Given a list of numbers, find the maximum and minimum values
#############################################################################################
def minmax(nums: list):
    llen: int = len(nums)
    max: int = 0
    for i in range(0,llen):
        if nums[i] > max:
            max = nums[i]  
    min: int = max
    for i in range(0,llen):
        if nums[i] <= min:
            min = nums[i]
    print(f"Max = {max}, Min = {min}")
#num: list = [2,4,3,-7,6,5,9,3,4]
#minmax(num)

############################################################################################
# Create a Python function to check if a given string is a palindrome
############################################################################################
def isPalin():
    while True:
        try:
            st: str = input("Input the string >> ")
            break
        except ValueError as e:
            print("Please enter the valid string!")
            continue
    if st == st[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

############################################################################################
# Given a list of integers, find the sum of all positive numbers
############################################################################################
def sum(lint: list):
    res: float = 0
    for i in lint:
        if i > 0:
            res += float(i)
    print("Sum of all positive numbers is >> {:.2f}".format(res)) 

#sum([2,1,4,-5,0,7,-3,6,-8])

############################################################################################
# Create a program that takes a sentence as input and counts the number of words in it
############################################################################################
def wordCount(st: str):
    slen: int = len(st)
    res: int = 0
    if st[0].isalpha() == True or st[0].isalnum() == True: 
        res = 1
    for i in range(0,slen):
        if (st[i].isalpha() == True and st[i-1] == ' ') or (st[i].isalnum() == True and st[i-1] == ' '):
            res += 1
    print(f"Number of words: {res}")

#wordCount("   2   Trung Tin Ngo   1011    2000      ___ hihi    ")

############################################################################################
#Implement a program that swaps the values of two variables
############################################################################################
def swap(a, b):
    c = a
    a = b
    b = c
    return a, b

print(swap(7,9))








