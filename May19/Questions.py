'''
######
######Question 1
######

I'm in the Black Blockchain Consultants group with Cheree Warrick. I was on the tutoring session on Saturday but I'm still having trouble with my Coursera assignment. A snapshot of the assignment is attached which includes the second attempt of code that will be submitted. I get as far as the dialogue box opening to input a number, which I do, but the box does not close after I hit "ok." I'm not sure if this second attempt of code is correct?

Additionally, below is the initial code I submitted from Saturday's tutoring session. Oddly, my colleague submitted the exact same code (below) and hers was accepted and mine was not. When I asked for assistance from the Coursera teacher's aid I received the below email response.

Can you kindly assist me with the correct code? I'm feeling really challenged by this assignment. :-(

This is the code that I initially submitted:

data_entry = None
largest_number = None
smallest_number = None
input_num = None
while data_entry  != "done":
    try:
            data_entry = raw_input("Enter a number:")
            input_number = int( data_entry)
            if smallest_number == None or input_number < smallest_number
                 smallest_number = input_number
            elif largest_number == None or input_number > largest_number
                    largest_number = input_number
    except:
            if data_entry == "done":
                break
            print("Invalid input")
print("Maximum is {}" .format(largest_number))
print("Minimum is {}" .format(smallest_number))

raw_input() is a Python 2 function which has been deprecated in Python 3 and replaced by function input(). I don't understand why you have 4 variables that you are initializing to None.

Ideally you should not place the conditionals that produce the maximum and the minimum in the try section. try/except is used to handle what's called an exception (see the pinned thread on proper use of try/except), you should place as little as possible there. All you need in the try section is the integer conversion attempt.

You need to take into consideration that elif statements are only run if the preceding condition is False. if statements are all run regardless of whether the preceding condition is either True or False.

You should view lecture video 5.4. You could also refer to section 5.7.2 in the Textbook, maximum and minimum in a loop (except we don't need either a list or a for loop here).

The test for 'done' needs to occur right after you prompt the user to enter an integer.

# global variables:
largest_number = None # reset to original, blank value
smallest_number = None
while True: #and not False
    input_number = raw_input("Enter a number: ")#since I will be evaluating not just integers or numbers, but strings as well (also using Python 2 so I can't just use "input")
    if input_number == "done": #if the user inputs 'done':
        break # get out of the code block
    try: #go through this first
        input_number = int(input_number) # make sure that the input_number is an integer
    except ValueError: # place this error if user does not use an integer value
        print "That's so wrong." # this will be your error message to display to the user
    else: # if the user does NOT type "done", run the code below
        if smallest_number is None: # if this variable is reset to blank
            smallest_number = input_number #variable assignment
            largest_number = input_number
        elif input_number < smallest_number:
            smallest_number = input_number
        elif input_number > largest_number:
            largest_number = input_number
print("Maximum is {}".format(largest_number))
print("Minimum is {}".format(smallest_number))


#######
#######Question 2 #####
#######

salad = 'carrots, lettuce, and cheese'
count = 0
for letter in salad:
    if letter == 'a':
        count = count + 1
print(count)



see attached

Can you explain what "for" and "in" do in your words?

list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]] # array of arrays
#regular array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#array of arrays = [[1,2,3],[4,5,6],[7,8,9]

#nested loop
for list in list_of_lists:
    for number in list:
        print number

for x in xrange(3):
    print x
else:
    print 'Final x = %d' % (x)

collection = ['hey', 'mom', 'wow']
for word in collection:
    for letter in word:
        print letter

collection2 = [322, 321, 123]
for x in collection2:
    for y in str(x):
        print y

string = "Hello World"
for letter in string:
    print letter


######
######Question 3
#######

see attached

What will be the output?

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

#####
#####Question 4
######

How would you use string slicing [:] to print out uct from the following string?
'''
x = 'From marquard@uct.ac.za'
print x[14:17]
'''




slice = x[14:17]
print(slice)
'''
