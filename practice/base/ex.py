# import time

# t1 = time.perf_counter()
# t2 = time.perf_counter()
# elapsed = t2 - t1
# print(f"Elaped time between t2 and t1: {elapsed}")

# print("Epoch time: ", end='')
# print(time.gmtime(0))

# print("Current tme since the epoch: ", end='')
# print(time.time())

# print("UTC time: ", end='')
# print(time.gmtime(time.time()))

# print("Human readable time: ", end='')
# print(time.strftime("%B %d, %Y", time.gmtime(time.time())))

# print("Change to time.struct format: ", end='')
# t = "08/06/2023 11:20:02 AM"
# print(time.strptime(t, "%m/%d/%Y %I:%M:%S %p"))

# num = (1, 2, 3, 4, 5)
# sq = [n ** 2 for n in num]
# even = [n for n in num if n % 2 == 0]
# print(sq)
# print(even)

# import math
# vectors = [(0,0), (0,1), (1,1), (1,2), (2,3)]
# res = [math.sqrt(vector[0] ** 2 + vector[1] ** 2) for vector in vectors]
# # for vector in vectors:
# #     magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
# #     res.append(magnitude)

# print(res)

# widgets = ['widget 1', 'widget 2', 'widget 3', 'widget 4']
# sales = [10, 5, 15, 0]
# d = {widgets[i]: sales[i] for i in range(len(widgets)) if sales[i] > 0}
# # for i in range(len(widgets)):
# #     if sales[i] > 0:
# #         d[widgets[i]] = sales[i]
# print(d)

# nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
# res = set()
# #res = {n ** 2 for n in nums if n % 2 == 0}
# for n in set(nums):
#     if n % 2 == 0:
#         res.add(n ** 2)
# print(res)
# ex = ValueError("Name must be at least 5 charactes in length")
# raise ex

# a:int = 1
# b:int = 0
# try:
#     res:int = a / b
# except ZeroDivisionError as e:
#     print(f"Exception occurred: {e}")
#     res = 0
# print (res)

# try:
#     open_database_connection()
#     start_transaction()
#     write_data()
#     commit_transaction()
# except WriteException as ex:
#     rollback_transaction()
#     raise
# finally:
#     close_database_connection()


# iter_list = iter(['Tin', 'Trung', 'Ngo'])
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))

# def sq_numbers(n):
#     for i in range(1, n+1):
#         yield i*i

# a = sq_numbers(3)

# print("The square of numbers are : ")
# print(next(a))
# print(next(a))
# print(next(a))


# filter()

# with open_database_connection() as conn:
#     # Work with open conn

# # once the with block is exited,
# #   the connection is automatically closed

# f = open('file_path', 'w')
# try:
#     # Write to file
#     for row in f:
#         print(row)
# finally:
#     f.close()

# with open('file_path', 'w') as f:
#     # write to file

# f.write("some string")
# f.writelines("iterable of strings")

# f = open('test.csv', 'w')
# f.write('abc')
# f.write('123445')
# f.close()

# with open('test.csv', 'w') as f:
#     f.write('abc \n')
#     f.write('1234566 \n')

# with open('test.csv') as f:
#     print(f.readlines())

# import math
# help(math.factorial)

# import datetime as dt
# dt1 = dt.datetime.utcnow()
# dt2 = dt.datetime.fromisoformat("2023-01-01T00:00:00")
# tdel = dt1 - dt2
# print(tdel)
# print(tdel.days * 24 * 60 * 60 + tdel.seconds + tdel.microseconds / (10 ** 6))
# print(tdel.total_seconds())
# tdel1 = dt.timedelta(days=2, hours=11, minutes=32, seconds=4)
# print(tdel1)
# # Output = 2 days, 11:32:04

# import datetime as dt
# date1 = dt.datetime.fromisoformat('2023-08-14T12:30:00-05:00')
# timezone_EDT = dt.timezone(dt.timedelta(hours=-4), 'EDT')
# print(date1.astimezone(timezone_EDT))
# # Output = 2023-08-14 13:30:00-04:00
# print(date1.astimezone(dt.timezone.utc))
# # Output = 2023-08-14 17:30:00+00:00
# date2 = dt.datetime(year=2023, month=8, day=14, hour=12, minute=30, second=0, tzinfo=timezone_EDT)

# print(date1)
# print(date2)

# import csv
# with open('test.csv') as f:
#     reader = csv.reader(
#         f,
#         delimiter='|',
#         quotechar='"',
#         escapechar="\\",
#         skipinitialspace=True
#     )
#     for row in reader:
#         print(row)
# # print(csv.list_dialects())
# # # Output = ['excel', 'excel-tab', 'unix']
# csv.register_dialtect("custom_dialect", delimiter=',', quotechar'"')
# csv.reader(f, dialect='custom_dialect')

import csv
# def parse_data(filename):
#     res = []

#     with open(filename) as f:
#         reader = csv.reader(f)
#         header = next(reader)
#         res.append(header)

#         for row in reader:
#             area = row[0]
#             data = row[1:]
#             data = [area] + [int(field.replace(',', '')) for field in data]

#             res.append(data)
#     return res

# print(parse_data('test.csv'))

# data = [
#     ['First_Name', 'Last_Name', 'DOB', 'Note'],
#     ['John', 'Cleese', '10/27/99', "It's the art!"],
#     ['Henry', 'Chinsu', '10/27/98', 'Oh "Spamming"'],
#     ['Phil', 'Clinton', '10/27/97', 'Dump'],
#     ['Nick', "O'Jones", '10/27/89', 'hihi']
# ]

# with open('test.csv', 'w') as f:
#     writer = csv.writer(f)
#     for row in data:
#         writer.writerow(row)

# with open('test.csv') as f:
#     for row in f:
#         print(row, end='')

# # Output =  First_Name,Last_Name,DOB,Note
# #           John,Cleese,10/27/99,It's the art!
# #           Henry,Chinsu,10/27/98,"Oh ""Spamming"""
# #           Phil,Clinton,10/27/97,Dump
# #           Nick,O'Jones,10/27/89,hihi

# csv.register_dialect('tem', delimiter='-', quotechar="*", escapechar="\\")
# with open('test.csv', 'w') as f:
#     writer = csv.writer(f, dialect='tem')
#     for row in data:
#         writer.writerow(row)

# with open('test.csv') as f:
#     for row in f:
#         print(row, end='')

# # Output =  First_Name-Last_Name-DOB-Note
# #           John-Cleese-10/27/99-'It''s the art!'
# #           Henry-Chinsu-10/27/98-Oh "Spamming"
# #           Phil-Clinton-10/27/97-Dump
# #           Nick-'O''Jones'-10/27/89-hihi

# import random as r
# system_seed = r.random()
# r.seed(4)
# custom_seed = r.random()
# print(f'System seed = {system_seed} \nCustom seed = {custom_seed}')
# Output =  System seed = 0.4904882088596284
#           Custom seed = 0.23604808973743452

# rr1 = r.randrange(1,16,2)
# rr2 = r.randrange(8)
# ri = r.randint(2,11)
# rf1 = r.random()
# rf2 = r.uniform(2, 10)
# print(f'Randrange1() = {rr1}, Randrange2() = {rr2}, Randint() = {ri}')
# print(f'Random() = {rf1}, Uniform() = {rf2}')
# # Output =  Randrange1() = 11, Randrange2() = 2, Randint() = 10
# #           Random() = 0.2174514771120024, Uniform() = 6.93810522123773

# import random
# l = [1, 2, 3, 4, 5, 7, 9, 12]
# w = [1, 1, 1, 1, 1, 1, 1, 4]
# for _ in range(6):
#     print(random.choices(l, weights=w, k=3))
# # Output =  [9, 4, 12]
# #           [12, 5, 7]
# #           [12, 7, 12]
# #           [5, 2, 5]
# #           [12, 12, 5]
# #           [1, 12, 1]


# print(f"Pick 2 element from {l}: {random.sample(l, 2)}")
# # Output: Pick 2 element from [1, 2, 3, 4, 5, 7, 9]: [2, 7]

# print(f"Single choice: {random.choice(l)}")
# print(f"Multiple choice: {random.choices(l, k=3)}")
# # Output =  Single choice: 5
# #           Multiple choice: [2, 5, 9]

# random.shuffle(l)
# print(l)
# # Output = [2, 4, 3, 5, 1]

# class RecursiveFunction:
#     def __init__(self, n):
#         self.n = n
#         print("Recursive function initialized with n =", n)

#     def run(self, n=None):
#         if n is None:
#             n = self.n
#         if n <= 0:
#             return
#         print("Running recursive function with n =", n)
#         self.run(n-1)

#     def __del__(self):
#         print("Recursive function object destroyed")

# # Create an object of the class
# obj = RecursiveFunction(7)

# # Call the recursive function
# obj.run()

# # Destroy the object
# del obj

# class Example:
#     # Initializing
#     def __init__(self):
#         print("Example Instance.")

#     # Calling destructor
#     def __del__(self):
#         print("Destructor called, Example deleted.")

# obj = Example()

# class Experiment(object):
#     # Constructor method
#     def __init__(self, eType, point, status='ongoing'):
#         self.expType = eType
#         self.points = point
#         self.expStatus = status

#     def increaseN(self, num):
#         self.dataCount += num

#     def changeExpStatus(self, status):
#         self.expStatus = status

#     def __str__(self):
#         return 'Experiment type: ' + self.expType + ' has ' + str(self.dataCount) + ' data points.'

# test = Experiment('Brain', 1450)
# print(test)
# print(test.dataCount)
# test.increaseN(10)
# print(test.dataCount)

# import matplotlib.pyplot as plt
# print(plt.plot(3,4,'o'))


# import csv

# # Convert employee data to dictionary
# def read_employees(csv_file_location):
#   csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#   employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
#   employee_list = []
#   for data in employee_file:
#     employee_list.append(data)
#   return employee_list

# employee_list = read_employees('/home/student-03-4173d4c42a42/data/employees.csv')
# print("=== Convert data to dictionary ===")
# print(employee_list)

# # Process employee data
# def process_data(employee_list):
#   department_list = []
#   for employee_data in employee_list:
#     department_list.append(employee_data['Department'])
#   department_data = {}
#   for department_name in set(department_list):
#     department_data[department_name] = department_list.count(department_name)
#   return department_data

# dictionary = process_data(employee_list)
# print("=== Process Data ===")
# print(dictionary)

# # Generate a report
# def write_report(dictionary, report_file):
#   with open(report_file, "w+") as f:
#     for k in sorted(dictionary):
#       f.write(str(k)+':'+str(dictionary[k])+'\n')
#     f.close()
# print("=== Generate Report ===")
# write_report(dictionary, '/home/student-03-4173d4c42a42/test_report.txt')

# num_char:int = 0
# with open("olympics.txt", "r") as f:
#     contents = f.read()
#     num_char = len(contents)
#     print(contents,num_char)
#     print("====================")

# with open("olympics.txt", "r") as f:
#     lines = f.readlines()
#     num_line = len(lines)
#     for line in lines:
#         print(line.strip())
#     print(num_line)

# def test(a:int, b:bool=True, dict1:dict={2:3, 4:5, 6:8}):
#     if b == True:
#         new:list = list(dict1.keys())
#         print(new)
#         if a in new:
#             return a
#     else:
#         return False

# test(4)
# test(2)
# test(4,False)
# test(5,dict1={5:4, 2:1})

######################
# # Given the same dictionary, medals, now sort by the medal count.
# # Save the three countries with the highest medal count to the list, top_three.
# ######################
# def get_key(val, my_dict:dict):
#     for key, value in my_dict.items():
#         if val == value:
#             return key
# medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
# top_three:list = []
# top = sorted(medals.values())[::-1][:3]
# print(top)
# for i in top:
#     key = get_key(i,medals)
#     top_three.append(key)
#     #print(key)
# print(top_three)

# ######################
# # We have provided the dictionary groceries.
# # You should return a list of its keys,
# # but they should be sorted by their values, from highest to lowest.
# #  Save the new list as most_needed.
# ######################
# groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
# def g(k,d):
#     return d[k]
# ks = groceries.keys()
# most_needed = sorted(ks, key=lambda x:g(x,groceries), reverse = True)

# #Create a function called last_four that takes in an ID number
# # and returns the last four digits.
# # For example, the number 17573005 should return 3005.
# # Then, use this function to sort the list of ids stored in
# # the variable, ids, from lowest to highest. Save this sorted list in
# # the variable, sorted_ids. Hint: Remember that only strings can be indexed,
# # so conversions may be needed.
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# def last_four(x):
#     return (str(x)[-4:])
# last_four(ids)
# sorted_ids = sorted(ids, key=last_four )
# print(sorted_ids)

# #$Sort the list ids by the last four digits of each id.
# # Do this using lambda and not using a defined function.
# # Save this sorted list in the variable sorted_id.
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# sorted_id = sorted(ids, key=lambda x: str(x)[-4:])

# #Sort the following list by each element’s second letter a to z.
# #Do so by using lambda.
# #Assign the resulting value to the variable lambda_sort.
# ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
# lambda_sort = sorted(ex_lst, key = lambda x: x[1])
# print(lambda_sort)
# ln = ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
# nums:dict = {}
# if ln[1] in nums:
#     nums[ln[1]] = nums[ln[1]] + 1
# nums[ln[1]] = 0
# print(nums)

# import re
# x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

# y = re.search('\S+?@\S+', x)
# z = re.search('F.+:', x)
# print(y)
# print(z)
import re

x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y)
