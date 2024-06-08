#!/usr/bin/env python3
#Author: Ishtiak Islam
#Author Id: 118051200
#Date Created: 2024/06/07

# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    # Returns the first five characters of the given string
    return s[:5]

def last_seven(s):
    # Returns the last seven characters of the given string
    return s[-7:]

def middle_number(n):
    # Converts the number to a string and returns the second and third characters
    str_n = str(n)
    return str_n[1:3]

def first_three_last_three(s1, s2):
    # Returns a string that starts with the first three characters of s1
    # and ends with the last three characters of s2
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))