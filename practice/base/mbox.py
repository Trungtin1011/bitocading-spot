# Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
############ From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# Also look at the last line of the sample output to see how to print the count.

fh = open("./misc/mbox-short.txt")
count = 0
lin: list = []
for line in fh:
    if line.startswith("From"):
        li: list = line.split()
        if li[0] != "From:":
            lin.append(li[1])
            count += 1
for n in lin:
    print(n)

print("There were", count, "lines in the file with From as the first word")
fh.close()

# Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as
# the person who sent the mail. The program creates a Python dictionary that maps the sender's
# mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop
# to find the most prolific committer.

handle = open("./misc/mbox-short.txt")
count: int = 0
nums: dict = {}

for line in handle:
    if line.startswith("From"):
        ln: list = line.rstrip().split()
        if (ln[0] != "From:") and (ln[1] not in nums):
            nums[ln[1]] = 1
        elif (ln[0] != "From:") and (ln[1] in nums):
            nums[ln[1]] = nums[ln[1]] + 1

for k in nums:
    if int(nums[k]) > count:
        count = int(nums[k])
for k in nums:
    if int(nums[k]) == count:
        print(k, count)
handle.close()

# Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour
handle2 = open("./misc/mbox-short.txt")
count: int = 0
nums: dict = {}
new: list = []

for line in handle2:
    if line.startswith("From"):
        ln: list = line.rstrip().split()
        if (ln[0] != "From:") and (ln[5] not in nums):
            nums[ln[5]] = 1
        elif (ln[0] != "From:") and (ln[5] in nums):
            nums[ln[5]] = nums[ln[5]] + 1
nn: dict = {}
new_nums = list(nums.keys())
new_nums.sort()
for k in new_nums:
    l: list = k.split(":")
    if l[0] not in nn:
        nn[l[0]] = 0
    nn[l[0]] = nn[l[0]] + 1
# print(nn)

for k in nn:
    print(k, nn[k])

handle2.close()
