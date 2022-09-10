# print("========1. Implement palindrome using iterator(for loop) and generator mechanism=======")
# #Example 1:-  By using for loop (Iterator)
# a=input("Enter any number :")
# for i in a:
#     pass
# if a == a[::-1]:
#     print("The number is palindrome")
# else:
#     print("The given number is not palindrome")
#
# #Example 2:- By using Generator
# a=input("Enter any number :")
# for i in range(len(a)):
#     if a == a[::-1]:
#         print("The number is palindrome")
#     else:
#         print("The given number is not palindrome")
#
#=====================================================================================
#
#print("===================2. Sum of two digits ==================================")
#Given input is: n1 = 1234 # int(input('Enter number1 : "))
                 # n2 = 9999 # int(input('Enter number1 : "))
                 # Output: 9+1 2+9 3+9 4+9
		         #         10 + 11 + 12 + 13
#Example1:-
# n1 = 1234
# n2 = 9999
# num1 = str(n1)
# num2 = str(n2)
# num3 = len(num1)
# sum = 0
# for i in range(num3):
#     add = int(num1[i]) + int(num2[i])
#     sum = sum + add
# print("Sum of two numbers are: ", sum)
#
#Example2:-
# n1 = 1234
# n2 = 9999
# def sum(n):
#     s1 = 0
#     d = 0
#     for i in range(len(str(n))):
#         d = n % 10
#         s1 += d
#         n = n // 10
#     return int(s1)
# d_n1 = sum(n1)
# d_n2 = sum(n2)
# print(d_n1 + d_n2)
#
#=====================================================================================
#
# print("==============3. Reverse String ===========================")
# Input: st = "ab@#cd!ef"
# Output: fe@#dc!ba
# st = "ab@#cd!ef"
# str1 = list(st)
# i = 0
# j = len(st)-1
# while i<j:
#     if not str1[i].isalpha():
#         i+=1
#     elif not str1[j].isalpha():
#         j-=1
#     else:
#         str1[i], str1[j] = str1[j], str1[i]
#         i+=1
#         j-=1
# new_str = ''.join(str1)
# print("After reversing the String is: ", new_str)
#
#=====================================================================================
#
# print("============= 4. Findout Elements duplicate count output in dict format========")

# Example 1:-
# some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# dict={}
# for i in some_list:
#     if some_list.count(i)>1:
#         dict[i]=some_list.count(i)
# print(dict)
#
# Example 2:-
# some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# l1 = []
# for item in some_list:
#     if some_list.count(item)>1:
#         l1.append([item, some_list.count(item)])
# print(l1)
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)
#
# =====================================================================================
#
# print("==========5. Solve the program=======================")
# t1 = (1, 2, 3, "a", "c")
# t2 = ("b", "d", 9, 8, 7)
# Output: (10,10,10,"ab","cd")
# t1 = (1, 2, 3, "a", "c")
# t2 = ("b", "d", 9, 8, 7)
# t3 = tup(set(t2))
# print(t3)
# for i in range(len(t1)):
#     t4.append(t1[i]+t2[i])
#     print(t4)
#
#======================================================================================
#
# print("===========6. Remove Zeros from IP Address============")
#Example1:-
#import re # re means Regular Expression
# ip = "216.08.094.196" # Input
# string = re.sub('\.[0]*', '.', ip) #'\'Escaping characters
# print(string)
#
#Example2:-
# ip = "216.08.094.196"
# new_ip = ''
# for i in ip:
#     if i == '0':
#         continue
#     else:
#         new_ip += i
# print("After remove zeros from IP is:", new_ip)
#
#=======================================================================================================================
# print("==============7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] #output= [1,2,3,4,5,6,7,8,9,10]======= ")
#
# l1 = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# l2 = []
# [l2.extend(x) if type(x) is list else l2.append(x) for x in l2]
# print(l2)

# print("==========8. Read the data and find lines, words, characters, vowels and Special chars============")
#
# file = open("", "r")
#
# number_of_lines = 0
# number_of_words = 0
# number_of_characters = 0
# for line in file:
#   line = line.strip("\n")
# won't count \n as character
#
#   words = line.split()
#   number_of_lines += 1
#   number_of_words += len(words)
#   number_of_characters += len(line)
#
# file.close()
#
# print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characte