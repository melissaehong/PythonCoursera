'''
///////
/////////Question 1///////
///////

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

///////
///////Answer 1 ///////
//////

Let's first plug in your code.

'''
hrs = input("Enter Hours:")
h = float(hrs)
rph= input ("Rate per Hour:")
r= float (rph)
if h<=40:
    pay = (h*r)
elif h>40:
    pay = (40*r) + (h-40)*(1.5*r)
print (pay)
'''
When I run it in the terminal, it seems to be working correctly.  So, now we know the code is not the problem.
It must be the way you are loading your problem.

Here are the steps:
1. Open your terminal
2. Navigate into the folder that has your file
-You can do this by typing 'ls' to see which folder you are in
-You can then type 'cd whatevermyfilenameis'
  For example, if you look in a directory, and you need to get to desktop/myproject, I would type 'cd desktop'
  to get into desktop, then 'cd myproject' to get into that folder.  You can also type 'cd desktop/myproject'
  to get there faster
-Once you are in your project folder and your filename is called, for example, 'test_file.py', type in the Terminal
'python test_file.py' to run your file.  Make sure your file ends in '.py' to make sure Python knows it's a python file.

You can also run it in Atom via the PlatformIO-ide-terminal plugin.  If you are using Mac, go to your terminal
and type 'apm install platformio-ide-terminal'

There are better instructions to install the IDE (integrated development environment) here:
https://atom.io/packages/platformio-ide-terminal

Then, you can press Cmd + Shift + T to open up a Terminal window within Atom!  Cool huh?

/////
//////Question 2 //////
/////

Question 2 Having trouble transferring from text editor to python
Go to the instructors explanation for 3.1 (I believe he is actually working a different assignment vs. the one we are given but the question is less about his answer but more about the process of transferring from text editor to python to run)
I am not clear how you save in Atom and then transfer to Python to run (though I have spent more time in the early chapters and will go back)
Can you show a simple example of that?

////
////Answer 2 /////
////

This question is more or less like the first one, so please check out Question 1's answer.


/////
/////Question 3//////
/////
I have been trying to figure this out for several days now. I have zero coding experience.

This is what I am trying to achieve:

5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num
    except ValueError:
        print("Invalid input")
print ("Maximum is"), largest
print ("Minimum is"), smallest


/////
/////Answer 3/////
/////
I've refactored your code for it to run correctly:
'''
#when using more than one word to define a variable or function.  you can look at the pep8
#reference for more info on naming convenions: PEP8 (python enhancement proposals) https://www.python.org/dev/peps/pep-0008/

#changed the variables to be more specific to the task.  make sure to be using underscores _
data_entry = None
largest_number = None
smallest_number = None
while data_entry != 'done':
#specified the while loop to stop when the user types 'done'
    try:
        #raw_input() returns a string, and input() tries to run the input as a Python expression
        data_entry = raw_input("Enter a number: ")
        input_number = int(data_entry) #let's you know that input_number is of int type
        if smallest_number == None or input_number < smallest_number:
            smallest_number = input_number # if there is no smallest_number, let smallest_number = input_number OR
            #if input_number is less than the smallest number, let smallest_number = input_number
        elif largest_number == None or input_number > largest_number:# if there is no largest_number, let largest_number = input_number OR
        #if input_number is greater than the largest number, let largest_number = input_number
            largest_number = input_number
    except:
        if data_entry == 'done': # if user types 'done':
            print "Exiting Program..." #print out "Exiting Program..."
            break # stop the program, do not run code under this
        print 'Invalid entry!' # if user types in something other than an int or 'done', this line will run
print("Maximum is {}".format(largest_number)) # after all the code is done, run this line
print("Minimum is {}".format(smallest_number)) # and this line
'''

/////
////Question 4 /////
////
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input


/////
/////Answer 4
/////
'''
# I borrowed code from Question 1, then made it into a function
def work_hours(): # using the word 'def' makes whatever follows into a function.  please end your function name with '()' to make it a function.  do not use '[]'
    try: #placed it into a try, except statement since this is what the question asked for
        hrs = float(raw_input("Enter Hours:"))
        #h = float(hrs) <-- took this out since it was easier to make 'hrs' into a more condensed variable name
        rph= float(raw_input ("Rate per Hour:"))
        #r= float (rph) <-- same reason as reason above
        if hrs<=40:
            pay = (hrs*rph)
        elif hrs>40:
            pay = (40*rph) + (hrs-40)*(1.5*rph)
        print (pay)
    except: # run this if the user inputs anything other than 'float' values
        print("Error, please enter numeric input")

work_hours() #type in function_name() to run your function
