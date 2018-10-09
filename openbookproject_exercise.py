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
    