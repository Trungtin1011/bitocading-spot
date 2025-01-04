#########################################################################################################
# #
# #
#########################################################################################################
import random
import string


def lowRand(N):
    re = -1
    if N in range(1, 200001):
        res = ""
        for n in reversed(range(1, 27)):
            if N % n == 0:
                letter = n
                break
        time = int(N / letter)
        str = "".join(random.sample(string.ascii_lowercase, letter))
        for letter in [*str]:
            res += letter * time

    return res


print("Random lowercase string...")
print(lowRand(30))


#########################################################################################################
# #
# #
#########################################################################################################
def roomPick(A):
    result = -1
    if len(A) in range(1, 100001):
        for item in A:
            if item not in range(1, 100001):
                return -1

        A.sort(reverse=True)
        print(A)
        result = 0
        temp_room = 0
        for item in A:
            temp_room += 1
            if item <= temp_room:
                # print(item)
                result += 1
                temp_room = 1

        return result


print("Room pick...")
print(roomPick([1, 1, 1, 1]))
print(roomPick([4, 2, 1, 3]))


#########################################################################################################
# #
# #
#########################################################################################################
def solution(A):
    res = -1
    if (
        all(isinstance(ele, list) for ele in A)
        and len(A) in range(1, 1001)
        and len(A[0]) in range(1, 1001)
        and min(map(min, A)) >= 1
        and max(map(max, A)) <= len(A) * len(A[0])
    ):
        res = 0
        arr = []
        for item in A:
            arr.extend(list(set(item)))
        _arr = list(set(arr))

        for item in _arr:
            if arr.count(item) > 1:
                res += 1

    return res


print("...")


#########################################################################################################
# You are given a string S consisting of N lowercase English letters. In how many ways can we split	#
# 	S into 2 non-empty parts, such that in at least one part the letter 'x' and the letter 'y' occur	#
# 	the same number of times? Write a function that given a string S of length N, returns the number of	#
# 	splits S satisfying the condition above?															#
# 																										#
# Examples:																							#
# 1. Given S = "ayxbx", the function should return 3. There are four possible splits of S: "a/yxbx", 	#
# "ay/xbx", "ayx/bx", "ayxb/x". Only "ay/xbx" does not fulfill the condition => ans = 3			#
# 2. Given S = "xzzzy": The function should return 0													#
# 3. Given S = "toyxmy": The function should return 5													#
# 4. Given S = "apple": The function should return 4													#
# #
# Requirement:																						#
# N is an integer within the range [2..200000]													#
# String S is made only of lowercase letters (a-z)												#
#########################################################################################################
def splitWay(S):
    result = -1
    if len(S) in range(2, 2 * int(1e5) + 1) and S.islower():
        result = 0
        for i in range(1, len(S)):
            if S[0:i].count("x") == S[0:i].count("y") or S[i:].count("x") == S[
                i:
            ].count("y"):
                # print(i)
                result += 1
    return result


print("Split string...")
print(splitWay("toyxmy"))


#########################################################################################################
# You are given a string S of length N consisting only of letters 'A' and/or 'B'. Our goal is to 		#
# obtain a string in the format "A..AB..B" (all letters 'A' occur before all letter 'B') by deleting 	#
# some letters from S. In particular, strings consisting only of letters 'A' or only of letters 'B'	#
# fit this format. Write a function that, given a string S, returns the minimum number of letters		#
# that need to be deleted from S in order to obtain a string in the above format.						#
# #
# Examples:																							#
# 1. Given S = "BAAABAB", the function should return 2. We can obtain "AAABB" by deleting the first	#
# occurrences of 'B' and the last occurrences of 'A'												#
# 2. Given S = "BBABAA", the function should return 3. We can delete all occurences of 'A' or all 	#
# occurrences of 'B'																				#
# 3. Given S = "AABBBB", the function should return 0. We do not have to delete any letters, because	#
# the given string is already in the expected format.												#
# #
# Requirements:																						#
# N is an integer within the range [1..100000]													#
# String S is made only of the characters 'A' and/or 'B'											#
#########################################################################################################
def delWay(S):
    if (
        ((S.count("A") + S.count("B")) == len(S))
        and 1 <= len(S)
        and len(S) <= int(1e5) + 1
    ):
        nA = S.count("A")
        nB = S.count("B")
        if nA == len(S) or nB == len(S):
            return 0
        else:
            count = 0
            while S[0] == "B":
                S = S[1:]
                count += 1

            count += min(
                [S[S.find("B") :].count("A"), S[S.find("B") : S.rfind("A")].count("B")]
            )
            return min([nA, nB, count])
    else:
        return -1


print("Delete characters ...")
print(delWay("BBABAA"))


#########################################################################################################
# #
# #
#########################################################################################################
import sys


def solution(A, K):
    if (
        len(A) in range(1, 201)
        and K in range(0, int(1e9) + 1)
        and min(A) >= 0
        and max(A) <= int(1e9)
    ):
        n = len(A) // K
        B = []
        for i in range(n):
            B.append(A[K * i : K * (i + 1)])
        if len(A) % K > 0:
            B.append(A[K * n :])

        dash_len = len(str(max(A)))
        table = "+" + (("-" * dash_len) + "+") * len(B[0]) + "\n"

        for item in B:
            line = "|"
            for number in item:
                line += " " * (dash_len - len(str(number))) + str(number) + "|"
            line += "\n"
            end_row = "+" + (("-" * dash_len) + "+") * len(item) + "\n"
            table += line + end_row

        print(table)
        sys.stdout.write(table)
    else:
        return -1


#########################################################################################################
# 	There are two wooden sticks of lengths A and B respectively. Each of them can be cut into shorter	#
# sticks of INTEGER lengths. Our goal is to construct the largest possible square. In oeder to do 	#
# 	this, we want to cut the sticks in such a way as to achieve four sticks of the same length (note 	#
# 	that there can be some leftover pieces). What is the longest side of square that we can achieve?	#
# 	Write a function that, given two integers A,B, returns the side length of the largest square that 	#
# 	we can obtain. If it is not possible to create any square, the function should return 0				#
# 																										#
# 	Examples:																							#
# 	1. Given A = 10, B = 21, the function should return 7. We can split the second stick into 3 sticks 	#
# 		of length 7 and shorten the first stick by 3													#
# 	2. Given A = 13, B = 11, the function should return 5. We can cut 2 sticks of lenth 5 from each 	#
# 	3. Given A = 2, B = 1, the function should return 0. It is not possible to make any square 			#
# #
# 	Requirement: A and B are integers with the range [1..1,000,000,000] 								#																	#
#########################################################################################################
def solution(A, B):
    result = -1
    if A in range(1, int(1e9) + 1) and B in range(1, int(1e9) + 1):
        result = 0
        result_arr = [A // 4, B // 4]
        if A // 3 <= B:
            result_arr.append(A // 3)
        if B // 3 <= A:
            result_arr.append(B // 3)
        if A // 2 <= B // 2:
            result_arr.append(A // 2)
        if A // 2 > B // 2:
            result_arr.append(B // 2)
        result = max(result_arr)
    return result


#########################################################################################################
# A technology company announced that a new supply of P monitors would soon be available at their 	#
# 	store. There were N orders (numbered from 0 to N-1) placed by customers who wanted to buy those 	#
# 	monitors. The K-th order has to be delivered to a location at distance D[K] from the store and is 	#
# 	for exactly C[K] monitors. Now the time has come for the monitors to be delivered. The orders will 	#
# 	be fulfilled one by one. To minimize the shipping time, it has been decided that the deliveries 	#
# 	will be made in order of increasing distance from the store. If there are many customers at the 	#
# 	same distance, they can be processed in any order. Monitors to more distant customers will be 		#
# 	delivered only once all orders to customers closer to the store have already been fulfilled.What is	#
# 	the maximum total number of orders that can be fulfilled? Write a function that, given two arrays 	#
# 	of integers D and C, and an integer P, returns the maximum total number of orders that can be 		#
# 	fulfilled.																							#
# 																										#
# Examples:																							#
# 1. Given D = [5, 11, 1, 3], C = [6, 1, 3, 2] and P = 7, the function should return 2. The customers #
# 		at distances 1 and 3 will have their orders fulfilled and 3 + 2 = 5 monitors will be delivered.	#
# 2. Given D = [10, 15, 1], C = [10, 1, 2] and P = 3, the function should return 1. Only the order 	#
# 		for the customer at distance 1 will be fulfilled. There will not be enough monitors in the 		#
# 		store for the customer at distance 10. Therefore, orders for customers at distances 10 and 15 	#
# 		will not be fulfilled.																			#
# 3. Given D = [11, 18, 1], C = [9, 18, 8] and P = 7, the function should return 0.					#
# 4. Given D = [1, 4, 2, 5], C= [4, 9, 2, 3] and P = 19, the function should return 4.				#
# #
# Requirements:																						#
# 		N is an integer within the range [1..100,000];													#
# Each element of arrays D and C is an integer within the range [1..1,000,000,000]; 				#
# 		P is an integer within the range [0..1,000,000,000].											#																								#
#########################################################################################################
def solution(D, C, P):
    result = -1
    if (
        len(D) == len(C)
        and len(C) in range(1, int(1e5) + 1)
        and P in range(0, int(1e9) + 1)
    ):
        for n in range(len(D)):
            if D[n] not in range(1, int(1e9) + 1) or C[n] not in range(1, int(1e9) + 1):
                return -1

        result = 0
        if min(C) > P:
            return result
        if len(set(D)) == 1:
            C.sort()
        else:
            DC_map = dict(zip(D, C))
            D.sort()
            C = [DC_map[x] for x in D]

        t_cost = 0
        for i in range(len(C)):
            t_cost += C[i]
            if t_cost > P:
                break
            result += 1

    return result
