Currently, we are asked to do our assignments from Cousera in a "tool" right in the assignment.   What I have just discovered doing the chapter 3 exercises is that I get the correct outcome, however when I go to do text editor Atom (which is what is suggested by the course teacher) and then transfer to python, that same programming results in multiple errors

Question 1 As an example, this is how I programmed exercise 3.1 in the tool and got the correct ouput, however, when I put in python got many errors and still can't get it correct
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
The desired output is 498.75
My programming/code that got me the desired output when put in the tool:
hrs = input("Enter Hours:")
h = float(hrs)
rph= input ("Rate per Hour:")
r= float (rph)
if h<=40:
pay = (h*r)
elif h>40:
pay = (40*r) + (h-40)*(1.5*r)
print (pay)
However, when I put in python it does not work

Question 2 Having trouble transferring from text editor to python
Go to the instructors explanation for 3.1 (I believe he is actually working a different assignment vs. the one we are given but the question is less about his answer but more about the process of transferring from text editor to python to run)
I am not clear how you save in Atom and then transfer to Python to run (though I have spent more time in the early chapters and will go back)
Can you show a simple example of that?
