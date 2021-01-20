#!/bin/python3

import math
import os
import random
import re
import sys

def func(num):
    return num[2:]

num=int(input())
num=max(func(bin(num)).split('0')).count('1')
print(num)