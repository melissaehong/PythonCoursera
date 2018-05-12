''''
Question 1

This question may be too basic for everyone  but I need help.  Right now i am currently doing all  coursera work and assignments in the tool but I would prefer to learn it live in atom and terminal. I have a file on my desktop which is saved for all my py files. I have a Mac.  Hoping you can help with the step by step ( i know you did it at the end of April but still need more assistance ):

Can you show a step by step of how you:
 write in a quick program atom
save on desk top (or in a py file)
transfer/pull up from atom to terminal
run the program in terminal


#####
####Question 2
####

For the question you answered on 5.5 when I run the answer you gave in the tool I am getting a error message of “You must use a return statement to pass the computed pay back to the main code”

This is the question.   4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a num

#### look at next question (both are related)


#####
####Question 3
#####
i was in the tutoring session this morning.  i believe cheree asked you the question regarding doing the hours * rate (overtime)
in a function.  i think it was the last question of the session.

at the time, i hadn't completed the assignment.  now after reviewing the material and working on the assignment myself,
i noticed that you missed something on the question.  it stated to add a RETURN.

i had updated my program by adding a function.  it ran fine.  however, i received an error that i did not include RETURN.

i understand the return for words, but not numeric values (such as this).  it is driving me CRAZY.

if you can, please advise.  thanks.

def computepay():

    hours = input('Enter Hours:')
    rate = input('Enter Rate:')

    if int(hours) <= 40:
        pay = float(hours) * float(rate)
    else:
        OT_hours = int(hours) - 40
        base_pay = 40 * float(rate)
        OT_pay = OT_hours * (float(rate) * 1.5)
        pay = base_pay + OT_pay
        int(pay)

    print(pay)

computepay()

#####
#####Question 4
#####

####see attached

Im trying to complete this assignment but keep getting parse error message for line 2. Would you please let me know what I’m doing wrong?

Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:
Score Grade
3.11. EXERCISES 39
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly as shown above to test the various different values for
input.

Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
4.14. EXERCISES 53
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input.


#####
#####Question 5
#####

####see attached

Look at Question5.jpg

#####
#####Question 6
#####

####see attached

Part1:
In the attached example,where  “Hello There” and “Finished”  and “done” and “Done”  come from?  What does “line” translate to? Is that just a variable name? What does Input (‘>’) translate to?

Part 2:
Can you please translate the below lines of code-in particular I am not clear on lines 4 and 5

Part 3:
Boolean Variable-In the below, can you explain why once it finds 3, all the following are True.  Can you # explain each of the lines of code

Part 4:
In the below, why is the correct  answer 5?

#####
#####Question 7
#####

####see attached


I have reviewed and reworked  assignment 4.6 a few times and have a few more questions:

Why is it necessary to put this code in a function?  Is it becasue there could be so many answers (ie if you actually had several different employees input their hours? and/or a single individuals hours could vary from week to week)
Does it make a difference where you place the variable names in the code-ie-could I place them above where I define the option or at the very bottom?
hours = float(input("Enter hours: "))
 rate = float(input("Rate per hour: "))

'''
