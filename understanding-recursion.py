import os
import math
import sys
import re
import random



n=int(input("Enter the number here: "))
total_sum=0

if n<=1:
    print(n)
else:
    for i in range(1,n):
        n = n * i
        
    print(n)

