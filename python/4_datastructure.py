"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
x: value
i: integer

Sequence                                 : an ordered collection

		--▷List                         : represented by []. mutable. homogeneous.
		                                   can be accessed via iteration

				 - append(x)             : adds x to the list
				 - extend(list)          : appends all items in the given list to the list
				 - del list[a:b]         : removes item from a(included) to b(excluded)
				 - insert(i, x)          : inserts x at i
				 - pop()                 : removes the last item and returns it 
				   ... or pop(i)         : removes the item at i and returns it
				   ... or popleft()      : removes the first item and returns it (DEQUE)
				 - clear()               : removes all items
				 - index(x)              : returns the index of the first item whose value is x
				 - sort()                : ??
				 - reverse()             : self-explanatory
				 - copy()                : a[:]
		
				 --▶ list comprehension


		--▷Tuple                        : represented by (). immutable. heterogeneous. 
		                                   can be accessed via unpacking or indexing

		         - unpack                : assign its elements to variables on left (the quantity must match)

		--▷Range



Sets                                     : An unordered collection without duplicate elements
                                           represented by {}
                                           (Yeah, we learned these at Math class)

                 * To create a set, use set(), not {}

                 - union                 : A U B
                 - intersection          : A ∩ B
                 - difference            : A - B
                 - symmetric difference  : A △ B, or (A-B)U(B-A)



Mapping

		--▷Dictionary  

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

### List
print("---------List----------")
a = [1,2,3,4,5,6,'a']

a.append(7)
print(a)

a.extend([8,9,10,11])
print(a)

print(a.pop())
print(a)

a.reverse()
print(a)
print(a.index(3))

b = a.copy()
b.clear()
c = a[:]
del c[:]       #same expression
print (a,b,c)

### List Comprehension
print("---------List Comprehension----------")
squares = []
for x in range(10) :
	squares.append(x**2)
print(squares)
squares = [x**2 for x in range(10)]
print(squares)
squares = list(map(lambda x: x**2, range(10)))   #same expression
print(squares)

a = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x!= y:
		    a.append((x,y))
print(a)
a = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]   #same expression
print(a)

### Stack
print("---------Stack----------")
stack = [1,2,3,4,5]
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

### Queue
print("---------Queue----------")
from collections import deque       #Important! 

queue = deque(["a","b","c"])
print(queue)

queue.append("d")
print(queue)

print(queue.popleft())
print(queue)

### Tuple
print("---------Tuple----------")
a = 3, 1, 4
b = a, 6, 7, 8

print(a)
print(b)

x, y, z = a
print(x,y,z)
p,q,r,s = b
print(p,q,r,s)

