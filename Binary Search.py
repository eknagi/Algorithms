#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 02:39:49 2020

@author: ekantanagi
"""


def traditional_search(lst, num):
  for i in range(len(lst)):
    if lst[i] == num:
      return True 
  return False

def binary_search(lst, num):
  # => O(logn), only works if the list is already sorted (ascending order)
  start_index = 0 #4
  end_index = len(lst)-1 #56
  middle_index = end_index // 2 #9
  
  while start_index <= end_index:
    middle_index = (start_index+end_index)//2
    
    if lst[middle_index] == num:
      return (True, middle_index)
    
    elif lst[middle_index] > num:
      end_index = middle_index - 1
    
    else:
      start_index = middle_index + 1
      
  return (False, -1)
  
print(binary_search([4, 5, 7, 9, 10, 24, 56], 59))
  