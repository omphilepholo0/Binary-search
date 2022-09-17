# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:07:21 2022

@author: ELPEE
"""

def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) -1
    mid_index = 0

    while left_index <= right_index :
        mid_index = (left_index + right_index)//2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_index < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1
    
if __name__ == '__main__':
    numbers_list = [12, 21, 23, 28, 35, 42, 92, 94]
    number_to_find = 12

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")
