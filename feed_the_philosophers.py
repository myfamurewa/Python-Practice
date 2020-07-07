"""
Polya Method
1. Understand the problem
2. Devise a plan
3. implement it
4. look for ways to improve what you created
"""

def feed_philosophers():
    eating = [True, False, True, False, False ]
    i = 0
    while i < len(eating):
        if i == 0:
            if eating[4]:
                eating[4] = False
                eating[i] = True
        else: 
            if eating[i - 1]:
                eating[i -1] = False
                eating[i] = True
        i = (i + 1) % 5
# this is a solution to the philosopeher problem but it will run infinitely
# we need a way to have it stop after a certain number of iterations
# after creating a first pass soslution go back and see what you can change to imporve the efficiency of the program yoou've just written

def feed_philosophersV2():
    pass