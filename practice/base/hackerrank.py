# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#
# Example: arr = [1,3,5,7,9]
# The minimum sum is `1+3+5+7=16` and the maximum sum is `3+5+7+9=24` => The function prints: `16 24`


#!/bin/python3
import math, os, random, re, sys


def getMax(arr):
    max = 0
    for i in arr:
        max = i if i > max else max
    return max


def getMin(arr):
    min = getMax(arr)
    for i in arr:
        min = i if i < min else min
    return min


def miniMaxSum(arr):
    # Write your code here
    sum = 0
    for i in arr:
        sum += i
    minNum = getMin(arr)
    maxNum = getMax(arr)

    print(f"{sum - maxNum} {sum - minNum}")


# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
def isEven(n: int):
    return True if n % 2 == 0 else False


def conditionCheck(n: int):
    if n >= 1 and n <= 100:
        try:
            if not isEven(n):
                print("Weird")
            elif isEven(n) and (n in range(2, 6)):
                print("Not Weird")
            elif isEven(n) and (n in range(6, 21)):
                print("Weird")
            elif isEven(n) and (n > 20):
                print("Not Weird")

        except Exception as e:
            print(e)
    else:
        print("Input number out of allowed range")


# Given three integers x, y and z
# Print a list of all possible coordinates given by (i,j,k) where `i+j+k != n`
# Here, (0 <= i <= x), (o <= j <= y), (0 <= k <= z)
# Please use list comprehensions rather than multiple loops, as a learning exercise.
def print_coordinate(x: int, y: int, z: int, n: int):
    print(
        [
            [i, j, k]
            for i in range(x + 1)
            for j in range(y + 1)
            for k in range(z + 1)
            if i + j + k != n
        ]
    )
