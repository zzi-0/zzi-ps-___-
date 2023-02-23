import sys
import math

input = sys.stdin.readline
n = 3
post_offices = [[1, 3],
[2, 5],
[3, 3]]

people = 0
for [village, num] in post_offices:
    people+=num

post_offices.sort(key = lambda x : x[0])

half = math.ceil(people / 2)
count = 0
for [village, num] in post_offices:
    count += num
    if half <= count:
        print(village)
        break