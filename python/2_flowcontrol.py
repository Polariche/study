"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
input("")					: User input
if, elif, else
for x in [list]			    : x = item from the list
for i in range(a,b,c)		: i = the loop number. loop lasts while a <= [_] < b
							  c is added to i after a loop. the default value is 1

continue, break (+ else)	: continue ends the current loop before attempting to enter another loop
							  break completely ends the loop
							  the else clause after the break statement runs after a break occurs

len(sequence) 				: length of a string or a list.
							  ex) len('ab') returns 2

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

###user input
"""
You know, having to enter a number whenever I try to run the script can be quite... annoying.

print ("---------User Input---------")
x = int(input("Enter an Integer: "))


###if
print ("---------If---------")
if x < 0:
	print("Negative")
elif x == 0:
	print("Zero")
elif x > 0:
	print("Positive")
else:
	print("What?")

"""

###for
print ("---------For---------")
words = ['Apple','Banana','Chocolate']	#'Iteration' in Java
for w in words: 							
   print(w, len(w))

print("Fibonacci")                      #Fibonacci fun
fibonacci = [0, 1]						 
print(fibonacci[1])

for i in range (2,10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(fibonacci[i])

###for -- flow control keywords

print("Break Test")
numbers = [1,2,3,4,5,6,7,8]
for x in numbers:
    if x == 6:
        print("break")
        break
    print(x)

print("Continue Test")
numbers = [1,2,3,4,5,6,7,8]
for x in numbers:
    if x == 6:
		print("continue")
		continue
	print(x)

print("looking for prime numbers")
for n in range(2,10):                    #looking for prime numbers between 2 and 10
	for x in range(2,n):
		if n % x == 0:
			break
	else:                                #when no break occurs == else 
		print(n)

###press enter to stop
print ("---------------------")
#input("Press Enter to exit")
