#!/bin/python3


import math
import os
import random
import re
import sys


# from numpy import dot


#
# Complete the 'cosine_similarity' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a_keys
#  2. DOUBLE_ARRAY a_values
#  3. INTEGER_ARRAY b_keys
#  4. DOUBLE_ARRAY b_values

# Assumptions
# 1. Each vector's keys are sorted
# 2. Every key is unique within each vector

# Solution
# cosine similarity is calculated as (A.B)/(||A||.||B||)

# Helper function to calculate cosine
def get_cosine(vector1, vector2):
    # 1. Find intersection of the two vectors
    intersection = set(vector1.keys()) & set(vector2.keys())
    # 2. Find the numerator (A.B)
    numerator = sum([vector1[x] * vector2[x] for x in intersection])

    # 3. Find the sums
    sum1 = sum([vector1[x] ** 2 for x in vector1.keys()])
    sum2 = sum([vector2[x] ** 2 for x in vector2.keys()])

    # 4. Find the denominator (||A||.||B||)
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    # Return computation
    return float(numerator) / denominator


def cosine_similarity(a_keys, a_values, b_keys, b_values):
    get_cosine(a_values, b_values)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_keys_count = int(input().strip())

    a_keys = []

    for _ in range(a_keys_count):
        a_keys_item = int(input().strip())
        a_keys.append(a_keys_item)

    a_values_count = int(input().strip())

    a_values = []

    for _ in range(a_values_count):
        a_values_item = float(input().strip())
        a_values.append(a_values_item)

    b_keys_count = int(input().strip())

    b_keys = []

    for _ in range(b_keys_count):
        b_keys_item = int(input().strip())
        b_keys.append(b_keys_item)

    b_values_count = int(input().strip())

    b_values = []

    for _ in range(b_values_count):
        b_values_item = float(input().strip())
        b_values.append(b_values_item)

    result = cosine_similarity(a_keys, a_values, b_keys, b_values)

    fptr.write(str(result) + '\n')

    fptr.close()
