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

For the question you answered on 5.5 when I run the answer you gave in the tool I am getting a error message of "You must use a return statement to pass the computed pay back to the main code"

This is the question.   4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a num


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
    print pay

computepay()


def computepay():
    hours = input('Enter Hours:')
    rate = input('Enter Rate:')

    if int(hours) <= 40:
        pay = float(hours) * float(rate)
        #place return after everything in the code is done
        return pay
        #Won't run any code after this
        print ("I am after the return!")
    else:
        OT_hours = int(hours) - 40
        base_pay = 40 * float(rate)
        OT_pay = OT_hours * (float(rate) * 1.5)
        pay = base_pay + OT_pay
        int(pay)
        return pay
        # won't run the code below
        print ("After the return")

print(computepay())
#place print to print out your return value, since
#return doesn't print anything out

dog = 'dog'
hotdog = 'hotdog' # <--- this is also a String
# set variable hotdog = 'hotdog'
def bigFunction(item):
    #parameter of bigFunction is 'item'
    item = 'true'
    #parameter is set to 'false'
    if item == 'true':
        #if parameter is 'true', run the next line of code
        return 'i am a dog'
        #return a String
    else:
        #if the parameter is set to 'false'
        return 'i am not a dog'

print(bigFunction(dog))

cat = True

def is_it_a_cat():
    if cat == False:
        print "I am not a cat"
    else:
        print "I am a cat"

is_it_a_cat()





#####
#####Question 4
#####

####see attached

I'm trying to complete this assignment but keep getting parse error message for line 2. Would you please let me know what I'm doing wrong?


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

score = float(input("Enter Score: "))
if score < 0.0 or score > 1.0:
    print("Enter a number between 0.0 and 1.0")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")

#####
#####Question 5
#####

####see attached

Look at Question5.jpg

largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num
    except ValueError:
        print("Invalid input")
print ("Maximum is", largest)
print ("Minimum is", smallest)

largest = None
smallest = None
num = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == 'done':
            break
        elif smallest is None or smallest > num:
            smallest = num
        elif largest is None or largest < num:
            largest = num
    except ValueError:
        print("Invalid input")
print ("Maximum is", largest)
print ("Minimum is", smallest)

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


#####
#####Question 6
#####

####see attached

Part1:
In the attached example,where  "Hello There" and "Finished"  and "done" and "Done"  come from?  What does "line" translate to? Is that just a variable name? What does Input ('>') translate to?

while True:
    line = input("> ")
    if line == 'done' :
        break
    print(line)
print ('Done!')

while True:
#while this loop is true:
    line = raw_input("> ")
    # line = the user's input after the "> " sign
    if line == 'done' :
    # if the user inputs 'done', run the next line of code
        break
        #stop the code
    print(line)
    #print out the user input
print ('Done!')
#when the while loop ends, print done



Part 2:
Can you please translate the below lines of code-in particular I am not clear on lines 4 and 5

largest_so_far = -1
print("Before", largest_so_far)

for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

largest_so_far        the_num
-1                        -
9                         9
41                        41
41                        12
41                         3
74                        74
74                        15

print("After", largest_so_far)




Part 3:
Boolean Variable-In the below, can you explain why once it finds 3, all the following are True.  Can you # explain each of the lines of code

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print (found, value)
print('After', found)

found   value
False     9
False     41
False     12
True      3
True      74
True      15

Part 4:
In the below, why is the correct answer 5?


tot = 0
for i in [5,4,3,2,1]:
    tot = tot + 1
print tot

## go over next week more ####

   tot = tot + 1

i      tot
0      tot = 0(tot) + 1 = 1 --> tot = 1
1      tot = 1(tot) + 1 = 2 --> tot = 2
2      tot = tot + 1 --> 2 + 1 = 3
3      tot = 3 + 1 = 4
4      tot = 4 + 1 = 5

#######
##### how to print values in list
sum = 0
tot = [5,4,3,2,1] #i=0,1,2,3,4 (index values)
for i in range(len(tot)): # (actual values)
    sum += tot[i]
print sum
#####
####

array1 = ['apple', 'banana', 'carrot']
print array1[0]
print array1[1]
print array1[2]
print array1
#if in a for loop, i is the index value

tot      i
         0

#####
#####Question 7
#####

####see attached

I have reviewed and reworked  assignment 4.6 a few times and have a few more questions:

Why is it necessary to put this code in a function?  Is it becasue there could be so many answers (ie if you actually had several different employees input their hours? and/or a single individuals hours could vary from week to week)
Does it make a difference where you place the variable names in the code-ie-could I place them above where I define the option or at the very bottom?
hours = float(input("Enter hours: "))
 rate = float(input("Rate per hour: "))

why put in a function?

name = 'Melissa'
print("hello, my name is " + name)
print("how are you?")
print("I like cats")
print("I also like dogs if they don't bite")
print("I enjoy long walks on the beach")
print("Can you repeat that?")
name = "Katie"
print("hello, my name is " + name)
print("how are you?")
print("I like cats")
print("I also like dogs if they don't bite")
print("I enjoy long walks on the beach")
print("Can you repeat that?")
name = "Tom"
print("hello, my name is " + name)
print("how are you?")
print("I like cats")
print("I also like dogs if they don't bite")
print("I enjoy long walks on the beach")
print("Can you repeat that?")

def chatting(name):
    print("hello, my name is " + name)
    print("how are you?")
    print("I like cats")
    print("I also like dogs if they don't bite")
    print("I enjoy long walks on the beach")
    print("Can you repeat that?")
chatting("Melissa")
chatting("Katie")
chatting("Tom")

def chatting(name, animal, animal2):
    print("hello, my name is " + name)
    print("how are you?")
    print("I like " + animal)
    print("I also like " + animal2 + " if they don't bite")
    print("I enjoy long walks on the beach")
    print("Can you repeat that?")

chatting("Jessica", "foxes", "bears")
chatting("Sky", "pandas", "snakes")


variable names

cat = "cat" # global variable

def myCatName():
    cat = "dog" # local variable (inside a function)
    print cat

print cat
myCatName()
'''
