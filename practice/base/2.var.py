#############################################################################################
# Given a list of numbers, find the sum and average
#############################################################################################
def aversum(lnum: list[float]):
    # sumr: float = sum(lnum)
    # avg: float = sumr / len(lnum)
    # print(f"Sum = {sumr}")
    # print("Average = {:.2f}".format(avg)) 

    return sum(lnum), sum(lnum) / len(lnum)

#print(aversum([1,3,-7,4.4,9,2,0,8,7.5]))

#############################################################################################
# Create a function to reverse a given string
#############################################################################################
def reverseStr(string: str):
    return string[::-1]
#print(reverseStr("ogN gnurT niT"))

#############################################################################################
# Given a list of names, concatenate them into a single string separated by spaces
#############################################################################################
def concat(name: list):
    # res: str = ''
    # for i in name:
    #     if i == name[len(name)-1]:
    #         res = res + i
    #     else:
    #         res = res + i + ' '
    # print(f"===={res}===")
    return ' '.join(name)
print(concat(["tem", "ca", "rem"]))

#############################################################################################
# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)
#############################################################################################


#############################################################################################
# Calculate the area and circumference of a circle given its radius
#############################################################################################


#############################################################################################
# Implement a program that converts a given number of minutes into hours and minutes
#############################################################################################


#############################################################################################
# Create a function to count the number of vowels in a given string
#############################################################################################


#############################################################################################
# Write a program to check if a number is prime.
#############################################################################################




