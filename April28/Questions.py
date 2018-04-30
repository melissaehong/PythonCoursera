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


Question 1:
-https://atom.io/packages/platformio-ide-terminal
Type cmd + shift + T


/////
//////Question 2 //////
/////

Question 2 Having trouble transferring from text editor to python
Go to the instructors explanation for 3.1 (I believe he is actually working a different assignment vs. the one we are given but the question is less about his answer but more about the process of transferring from text editor to python to run)
I am not clear how you save in Atom and then transfer to Python to run (though I have spent more time in the early chapters and will go back)
Can you show a simple example of that?

Question 2:
-Terminal or Script(Atom) or PlatformIO IDE(Atom)


////////
//////Question 3////////
///////

5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

I have tried it several ways, but it is not working. This is my latest try:
largest_number = None

smallest_number = None

data_entry = None

first_name = None

while data_entry != 'done':

    try:
        data_entry = raw_input("Enter a number: ")

        input_number = int(data_entry)

        if smallest_number is None or smallest_number > input_number:

            smallest_number = input_number

        elif largest_number is None or largest_number < input_number:

            largest_number = input_number

    except:

        if data_entry == 'done':

            print("Exiting Program...")

            break

        print("That's not what I thought it was going to be.")

print ("Maximum is {}").format(largest_number)
print ("Minimum is {}").format(smallest_number)

Question 3:
-Double spacing
-Command + d for multiple changes at once
-Naming convention for variables: PEP8 (python enhancement proposals) https://www.python.org/dev/peps/pep-0008/


/////
/////Question 4 //////
/////

Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input

def work_hours():
    try:
        hrs = float(raw_input("Enter Hours:"))
        #h = float(hrs)
        rph= float(raw_input ("Rate per Hour:"))
        #r= float (rph)
        if hrs<=40:
            pay = (hrs*rph)
        elif hrs>40:
            pay = (40*rph) + (hrs-40)*(1.5*rph)
        print (pay)
    except:
        print("Error, please enter numeric input")

work_hours()
'''
