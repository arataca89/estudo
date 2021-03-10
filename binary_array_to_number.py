#!/usr/bin/env python

# arataca89@gmail.com

# CodeWars exercise:

# Given an array of ones and zeroes, convert the equivalent binary
# value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary
# representation of 1.

#Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11

# However, the arrays can have varying lengths, not just limited to 4


def binary_array_to_number(arr):
    dec = 0
    arr.reverse()
    for i in range(len(arr)):
        dec += arr[i]*(2**i)
    print(dec)


binary_array_to_number([0,0,0,1])
binary_array_to_number([0,0,1,0])
binary_array_to_number([0,1,0,1])
binary_array_to_number([1,0,0,1])
binary_array_to_number([0,0,1,0])
binary_array_to_number([0,1,1,0])
binary_array_to_number([1,1,1,1])
binary_array_to_number([1,0,1,1])
