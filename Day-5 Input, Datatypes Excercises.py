#1)Program Creating list of n integer values
n=int(input("Enter number of elements in a list: "))
L=[]
i=0
while(i<n):
    L.append(i)
    i=i+1
print("L=",L)

#a)Adding an item into the list
d=int(input("Enter an item to be added to the list :"))

L.append(d)
print("List after adding an element",L)

L.insert(5,6)
print("List after adding an element2",L)

#b)deleting
f=int(input("Enter an index of an item to be deleted from the list :"))

del L[f]
print("List after deleteing an element",L)

g=int(input("Enter an index of an item to be deleted from the list :"))
L.pop(g)
print("List after deleteing an element2",L)

L.remove(6)
print("List after deleteing an element-6",L)

#C)Storing largest number from a list to a variable
l=max(L)
print('Largest number from the list is:',l)

#d)Storing the smallest number from the list to a variable
s=min(L)
print("Smallest number from the list is:",s)


#2)Creating a tuple
T=(5,9,3,5,3,2,8)

#Printing the reverse of a tuple
print(T[::-1])
    

#3)Creating a tuple
H=(6,8,3,'h','u','f')

#Converting tuple into list
print("Convrted list is:",list(H))







    
