'''

///question 1

Here's the question I have. We're learning about defining functions. WE're asked to write a program to prompt the user for hours and rate per hour using input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

'''
'''
# defining my function "computepay"
def computepay():

    enter_hours = float(input("Enter hours: "))
    # enter_hours is the variable name
    # float is the data type (decimal number)
    # input is a function that lets the user input into the terminal
    # "Enter hours: " is the prompt that will show up for the user
    # The entry of the user will be saved into enter_hours
    rate_per_hour = float(input("Rate per hour: "))
    # rate_per_hour is the variable name
    # float is the data type (decimal) that is required or else it will give an error
    # input is the function that allows the user to type in the terminal
    # "Rate per hour: " is what will be on the terminal for the user to see
    # The entry of input will be saved as rate_per_hour
    if enter_hours < 40:
    # if the user inputs a value that is less than 40
    # run this next line of code
        total = enter_hours*rate_per_hour
        #total = whatever i put here on the other side of equals ==> enter_hours * rate_per_hour
        #enter_hours is the value of the input from the user as above
        #rate_per hour is the value "                               "
        #multiply enter_hours * rate_per_hour to get the total

    else:
    #run this line if the above is not true (enter_hours > 40)
        total = (40*rate_per_hour) + (enter_hours-40)*(1.5*rate_per_hour)
        # total = the equation above
        # 40 * rate_per_hour is the first 40 hours multiplied
        # after the first 40 hours, run 1.5 times the rate (overtime rate)
        # i.e. (enter_hours-40) <--- hours after 40 hours, (ex: 45 hours = 5 hours over 40 hours)
        # (1.5*rate_per_hour) <--- overtime rate of 1.5 x the rate you placed earlier

    print(total)
    # this line is run when the program ends (runs through the if statement, else statement and then is done)

def computepay():
    #indent after you define your function ALWAYS
    enter_hours = float(input("Enter hours: "))
    rate_per_hour = float(input("Rate per hour: "))
    if enter_hours < 40:
        total = enter_hours*rate_per_hour
        # indent after the if/else statement ALWAYS
    if enter_hours == 40:
        print("I'm forty!")
        total = "nothing"
    else:
        total = (40*rate_per_hour) + (enter_hours-40)*(1.5*rate_per_hour)
        # indent after the if/else statement ALWAYS
    print(total)

computepay() # <---- calling the computerpay function by using '()'

#invoke/call computepay function by typing "computerpay()"
#when you enter 40, it will be considered 'less than 40'

# 2 is considered < 2 in the statement is 2 < 2?





///question 2

What is the purpose of functions and when/why do you use them?

Can you please explain the max function?  Not clear of the use and do not understand whey it says w is the largest letter.  Why is a space the smallest thing?   This is what is part of the course.

Do not understand the Max function and  arguments. Can you explain
'''
#function purpose
#A function is a block of reusable code that is organized


# this is a line comment
'''
this is a multi line comment
i can even comment one line down
and more
more
more
'''






'''def do_you_like_cats(name):
    if name == 'Melissa':
        print('I like cats!')
    else:
        print('I do not like cats')

#do_you_like_cats('Melissa')
#do_you_like_cats('CatHater')
#do_you_like_cats('Sydney')
print("Hi, my name is Melissa")
print('Hi, my name is Melissa')
print('Hi, my name is Melissa')
def name(first_name): #parameter
    print("Hi, my name is " + first_name)

name('Melissa')#argument
name('Sydney')
name('Cheree')
print('Hi, my name is Melissa')
print('Hi, my name is Sydney')
print('Hi, my name is Cheree')


def greet():
    print('Hello, so nice to meet you!')

greet()

#Max Function Explanation
#https://www.asciitable.com/
'''
'''
print ('Max of hello world is ' + max('hello world')) # w

print ('Min of hello world is ' + min('hello world')) #

print ('Min of hello world is ' + min('helloworld')) # d
print ('Max of abcdefghijklmnopqrstuvwxyz ' + max('abcdefghijklmnopqrstuvwxyz')) # z
print ('Min of abcdefghijklmnopqrstuvwxyz ' + min('abcdefghijklmnopqrstuvwxyz')) # a
print ('Max of 0123456789 is ' + max('0123456789')) # 9
print ('Min of 0123456789 is ' + min('0123456789')) # 0
print('Max of 2 and 3 is ' + max(str(2), str(3))) # Returns 3 as 3 is the largest of the two values



///question 3
Sorry one other question. As i look at the attached question 6 from our quiz, my answer would be that it would not print anything as there is no line of code that invokes or calls the function "func"  But apparently the answer is 10 and 20.   Wouldn't you have to have a line of code that says print "func (x)"" to call/invoke?   The other question is why is the "x" in () on line 1.  In the lecture, when you define a function, the () were always left empty.
Thank you!










#definition of function "func"
def func(x):
    print(x)

# x is the parameter (placeholder)


func(10) # calling or invoking my function

# 10 as an argument (actual value you're going to test)



func(500) # calling or invoking the function






func(10) # argument
print('******')
print('******')
func(20)
print('******')
print('******')
def greet():
    print("hi there!")

greet() # call or invoke my function

'''

def i_am_hungry():
# def is saying that it's a function that we're going to define next
# i_am_hungry is my function name
# () this parenthesis is confirming that this is a function, and that it will be invoked/called
# when I run the program
# : is the syntax of a function at the end.  For example, "This is a sentence." the . is the end of the sentence
    print("I'm hungry!")
    #print is a function built in to Python that allows you to print out into the terminal
    #() inside is what is going to be used as an argument
    # "I'm hungry" is the string that will be used as an argument for the print function


#i_am_hungry()
#invoke or call i_am_hungry with the parenthesis after the function
i_am_hungry() #this is function is not called or invoked
