import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_ratio=0.0
    tip_ratio=(tip_percent/100)*meal_cost
    tax_ratio=0.0
    tax_ratio=(tax_percent/100)*meal_cost
    total=meal_cost+tip_ratio+tax_ratio
    print(round(total))
    
    

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)