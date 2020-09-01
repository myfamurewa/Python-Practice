import itertools
# UNDERSTAND
"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00 and the largest is 23:59. Starting from 00:00, a time is larger if more time
has elapsed since midnight.

Return the answer as a string of length 5. If no valid time can be 
made, return an empty string

"""

# PLAN
"""
set a max value of 2,359
loop through the array and find all the numbers that can be made
return the highest number less than 2,359
if no number lower than 2,359 is found return an empty string

"""


#Execute
test1 = [1, 2, 3, 4]

def largest_time_for_given_digits(A) -> str:
   result = ""
   for i in range(4):
       for j in range(4):
           for k in range(4):
               if i == j or j == k  or k == i : continue
               hh = str(A[i]) + str(A[j])
               mm = str(A[k]) + str(A[6-i-j-k])
               _time = hh + ":" + mm
               if hh < "24" and mm < "60" and _time > result: result = _time
   return result

print(largest_time_for_given_digits(test1))