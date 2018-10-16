# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:30:24 2018

@author: admin
"""

s1="All "
s2="work "
s3="and "
s4="no "
s5="play "
s6="makes "
s7="Jack "
s8="a dull boy."
print(s1+s2+s3+s4+s5+s6+s7+s8)
##############Q2
6 * (1 - 2)
###########Q3
bruce=6
bruce + 4
#################Q4
p=10000
r=0.08
n=12
t=float(input("No. of years"))
t
a=float(p*(1+r/n)**(n*t))
round(a,2)
########Q5
0 % 7
0
#########q6
curr_time=int(input("What is time now : "))
wait_time=int(input("How long you will wait : "))
stg=wait_time%24
print("Alarm goes off after ",wait_time//24,"days","at ",(curr_time+stg)%12)

#################
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                # This is new
size = 20
for i in range(30):
   tess.stamp()             # Leave an impression on the canvas
   size = size + 2          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(24)           #  ...  and turn her

wn.mainloop()

for l_var in range(10):
    print("We like Python's turtles!")
    
##############Functions
def final_amt(p,r,n,t):
    return(float(p*(1+r/n)**(n*t)))
    
print(final_amt(1000,0.05,10,5))   

##############control flow
x=int(input("Enter interger :"))
if x<0:
    print('VAlue is negative')
elif x>0:
    print('Greater than 0')
else:
    print('value is zero')    
    
words = ['cat', 'window', 'defenestrate']    

for wrd in words:
    print(wrd,len(wrd))
   
a = ['Mary', 'had', 'a', 'little', 'lamb']    

for i in range(len(a)):
    print(i,a[i])
    
list(enumerate(a))   

#######
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
 
#######
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    result=[]
    result1=[]
    a, b = 0, 1
    while a < n:
        result.append(a)
        result1=result1+[a]
#        print(a, end=' ')
        a, b = b, a+b
    print(result1)
    return result   

 
        
        
fib(2000)        
#############
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

##########
def function(a):
    pass

function(0, a=0)

########

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
    
write_multiple_items('test',",","test1","test2")    

def bad_absolute_value(x):
    if x <= 0:
        return -x
    elif x > 0:
        return x

###############

	
def absolute_value(x):
    if x < 0:
        return -x
    return x        

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

test_suite()        # Here is the call to run the tests    


def absolute_value(n):   # Buggy version
    """ Compute the absolute value of n """
    if n < 0:
        return 1
    elif n > 0:
        return n
    
#####################
import sys
  # Get the caller's line number.


def test1(pass_flag,inpt):
    linenum = sys._getframe(1).f_lineno 
    if pass_flag:
        print('Test Pass for', inpt,"line at {0}".format(linenum))
    else:
        print('Test Fail for ', inpt,"line at {0}".format(linenum))


def test_suite1():
    """ Run the suite of tests for code in this module (this file).
    """
    test1(absolute_value(17) == 17,17)
    test1(absolute_value(-17) == 17,-17)
    test1(absolute_value(0) == 0,0)
    test1(absolute_value(3.14) == 3.14,3.14)
    test1(absolute_value(-3.14) == 3.14,-3.14)

test_suite1()        # Here is the call to run the tests    


def mysum(xs):
    """ Sum all the numbers in the list xs, and return the total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

# Add tests like these to your test suite ...
test(mysum([1, 2, 3, 4]) == 10)
test(mysum([1.25, 2.5, 1.75]) == 5.5)
test(mysum([1, -2, 3]) == 2)
test(mysum([ ]) == 0)
test(mysum(range(11)) == 55)  # 11 is not included in the list.


def summation(ls_item):
    total_sum=0
    for item in ls_item:
        total_sum=total_sum + item
    return total_sum        
        
summation([1,2,3,4,5,6])       
    
    
def sum_to(n):
    """ Return the sum of 1+2+3 ... n """
    ss  = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss

# For your test suite
test(sum_to(4) == 10)
test(sum_to(1000) == 500500)

def num_digits(n):
    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
        print(n)
    return count

num_digits(710)

######
for x in range(13):   # Generate numbers 0 to 12
    print(x, "\t", 2**x)
    

###
for i in range(1, 7):
    print(2 * i, end="   ")
print()    



##########Tuple
name_yr=("Prashant",1999)

name_yrs=[("sdasd21",2321),("sdasd21",2322),("sdasd13",2323),("sdasd41",2324)]
name_yrs

for(name,year) in name_yrs:
    if year==2321:
        print("name is" ,name, "and year is" ,year)
        continue
    print("name is" ,name, "and year is" ,year," False ")

######nested loop
    students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]
    
# Print all students with a count of their courses.
for (name, subjects) in students:
    print(name, "takes", len(subjects), "courses")

#Now we’d like to ask how many students are taking CompSci. This needs a counter, and for each student we need a second loop that tests each of the subjects in turn:

# Count how many students are taking CompSci
counter = 0
for (name, subjects) in students:
    for s in subjects:                 # A nested loop!
        if s == "CompSci":
           counter += 1

print("The number of students taking CompSci is", counter)
# Count how many students are taking CompSci
counter = 0
for (name, subjects) in students:
    for s in subjects:                 # A nested loop!
        if s == "CompSci":
           counter += 1

print("The number of students taking CompSci is", counter)

#The number of students taking CompSci is 3       

##Write a function to count how many odd numbers are in a list.

s = input("Enter list item seperated by space:")
numbers = list(map(int, s.split()))

def get_odd(no):
    if no%2==0:
        return True
    else: 
        return False

for item in numbers:
#    print(item, " ",item%2)
    if(not get_odd(item)):
        print(item, " ",get_odd(item))
    
##Sum up all the even numbers in a list
    
total_even=0    
for item in numbers:
    if( get_odd(item)):
        total_even+=item
        
        
print(total_even)   

###     

word="zebra"   
        
if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")
    
##############tuple
Julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")    

Julia[:3]
a = [1, 2, 3]
b = a[:]
a is b
b=a
a is b
xs = [1, 2, 3, 4, 5]
xs
for (i, val) in enumerate(xs):
    xs[i] = val**2

song = "The rain in Spain..."
wrds=song.split("n")
wrds
glue=";"
join_word=glue.join(wrds)
join_word
######
xs = list("Crunchy Frog")
xs
"".join(xs)
nested = ["hello", 2.0, 5, [10, 20]]
temp=nested[3]
temp[1]

import random

rng = random.Random()

rng.randrange(1,7)
range(52)
all_cards=list(range(52))

tst=rng.shuffle(all_cards)
tst
type(tst)

rng.shuffle(xs)         # Shuffle the list
result = xs[:5] 

all_cards[:10]

import time
time.clock()

ff=open("voter_name4.csv")
voter_name4

myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()
