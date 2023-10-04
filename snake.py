print('Hello Rangers!')#this is a comment after the print statement
#This is a comment


#TO-Do I need to add some functionally right here later

#Let's talk about variables real quick

x = 5
print(x)
print(type(x))

#Data types:
#integers
num1 = 5

#float
num2 = 5.0

print(num1)
print(num2)
print(type(num1))
print(type(num2))

print('\nMATH OPERATIONS:')
#Math operations


#Order of operations is automatically sorted out by python BUT we can group with parenthesis

#add     +
add1 = 5 + 5
print(add1)

#subtract    - 
sub1 = 10 - 5
print(sub1)

#multiply   *
prod1 = 5 * 5
print(prod1)

#power    **

#divide    /
div1 = 25 / 5
print(div1)
print(type(div1))

#floor division    //
div2 = 25 // 5
print(div2)
div3 = 26 // 5
print(div3)

#modulo   %
mod1 = 25 % 5
print(mod1)
mod2 = 26 % 5
print(mod2)

# odd or even? ANYTHING % 2 ==0 is even, otherwise it's odd
print(65 % 2 != 0)

# type and value equality

#   = this symbol represents assigning a value
#   == this is an equality check
#   != this is NOT equal
#       a note on the double equals- we're checking TYPE and VALUE equality

print(int('5') == 5)

#Another side-note: 'protected' terms:-- WATCH your variable names
print(int('5'))

int = 56
print(int)

# Let's talk about strings!
print('\n\nSTRINGS:')

#Strings: single or double quotes are fine:
st1 = 'this is a string'
st2 = "So is this lk0982@#$^h@436@111"
# watch your single and double quotes!
# str3 = 'so's this!
st3 = "So's this!"
st4 = 'that is so "last year"  !' 
st5 = 'so\'s this' #the escape character is telling python to ignore the special behavior of the character
print(st5)

# some things about strings
#string are IMMUTEABLE!   Also ordered
print(st1[5])
print(st1.upper())
print(st1.lower())

# Another sidebar:
# Functions vs Methods
#Functions (should) work on anything where a method only works on a specific class

#Manipulating strings
# 2 main pieces:
# concatenation
st7 = st1 + st2 
print(st7)

st8 = st1 + '  ' + st2 + '  ' + st5 + ' /and why not more?/ ' + st4
print(st8)

#interpolation
# we'll just call it f-strings here! 
interp = f"This is also just a string except i can throw it python stuff like this --> {mod1} <-- yay the integeger prints!!!!"
print(interp)

interp2 = f"This is also just {num2} a string except {num1} i can throw it pyth{num2}on stuff like this --> {mod1} <-- yay the integeger prints!!!!"
print(interp2)

# Lists!
print('\nLISTS:')
# lists are:
#   ordered (indexed), dynamic, muteable, iterable

a_list = []
print(a_list, type(a_list))
nums_list = [1, 2, 3, 4, 5]
print(nums_list)
r_list = ['a', 1, 5.0, None, True, []]
print(r_list)

print(r_list[3])
print(len(r_list))

#Function vs methods syntax
#   function call and inputs/arguments
#myfunction(myargument)     datatype.method(myargument)
#METHODS:

#append
# adds on to the END of the list
a_list.append(5)
print(a_list)
a_list.append(10)
print(a_list)
a_list.append(50)
print(a_list)
a_list.append(2)
print(a_list)
r_list.append(False)
print(r_list)

#pop()
# takes out the last item of the list
r_list.pop()
print(r_list)
# but there's more for pop!
# we can store it to a variable, and also there's an OPTIONAL parameter to specify which position to pop from
print('CRAZY POP EXAMPLE')
a = r_list.pop(0)
print(a)

r_list.append(None)
print(r_list)

#remove()
# removes the FIRST occurence of the specified value
r_list.remove(None)
print(r_list)

#Looping     - aka iterating
print('\nLOOPING:')

print(a_list, r_list)

print('The standard for loop-->')
#for loop
#syntax     for item in items:
#               this is the code block to execute on each step
for r in r_list:
    print(r)

for a in a_list:
    print(a**2)
    print(a)

#range function --> range(start, stop, step)
for x in range(0, 5, 1):
    print(x)
print('\n')
for x in range(5):
    print(x)
print('\n')
for x in range(10, 4, -1):
    print(x)
print('\n')
for x in range(5):
    print('this is 5 steps')

#the index loop
#  syntax  -->  for i in range(len(iterable)):
                            #code block
print('\nINDEX LOOP:')
for i in range(len(a_list)):
        print(i, a_list[i])

# the while loop
# syntax    while condition:
                #code block

while True:
     print(x)
     #DOn't DO INFINITE LOOPS!
     break

l = 0
while l < len(a_list):
     print(a_list[l])
     l += 1

#incrementing and decrementing
# saying 1 + 1 is not actually saving a value; it's just referencing a number without changing the variable
# we have to 1 = 1 + 1 OR the shorthand 1 += 1
# This can also be used with all the other math operators:
# -=   *=  /=

print('conditionals:')
# if, elif, else
age = 12


if age < 18 :
     print('kid')
elif age > 64 :
     print('senior')
else:
     print('adult')

if age > 17 and age < 65:
     print('adult')

# if age > 17 and < 65: not complete!

# Truth tree:
# T and T == True
# T and F == False
# F and F == False

# T or T == True
# T or F == True
# F or F == False

#functions:
#syntax     def  funcname(parameters):
                    #codeblock

def hello(name):
    st = f"Welcome to Rangers {name.title()}!"
    print(st)

hello('Miguel')


a_name = 'Kymbat'
#membership checks --> the "in"
if 'b' in a_name:
     print('YEP it\'s in there!')

print(567 in a_list)