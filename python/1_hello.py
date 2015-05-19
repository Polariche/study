"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print() 					: print a message to the console
sequence --▷ 	string      : implement of sequence. immutable.
				list 		: implement of sequence. mutable. 
				
				
		 --▶	sequence[a:b] - returns a sequence
			    				which includes from sequence[a] (included) to sequence[b] (excluded)
			    				* sequence[:] is a deep copy of sequence
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#printing
print ("Hello World!")

#String
print ("-----------String---------") 
word = "Python"
print(word[0],word[3],word[:],word [4:6])

#String
print ("-----------List---------") 
squares = [1,4,9,16,25]
print(squares[0])			#returns integer
print(squares[1:3])			#returns list
squares + [36,49]
squares.append(64)
print(squares)

nested = ['a', 'b', [1,2], 'd', 'e', 'f', [1, 2, ['Z', 'Y', 'X'], 3]]
print(nested)

#press enter to stop
print ("---------------------")
#input("Press Enter to exit")
