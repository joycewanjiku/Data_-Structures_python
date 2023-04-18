#  craeting a list in python
my_list=[]
print(my_list)
my_list=[1,2,3,3.132]
print(my_list)
# Adding Elements in the list method can be append()
# extend() and insert() functions
# append() adds all elements passed to it as a single element
# extend()adds the elements one by one into list
# insert() adds the element passed to the index value and increase the sixe of the list too

my_list=[10,20,30]
print(my_list)
my_list.append([546,67])
print(my_list)
my_list.extend([675])
print(my_list)
my_list.insert(34)
print(my_list)
# Deleting elements in python method
# del keyword wich is built-in into python but this does not return anything back 
#tif you want the element back we use pop() it takes the index value
# remove()it is used to remove an element
# clear()is used to empty

my_list=[67,89,3.132]
del my_list[5]
print(my_list)
my_list.remove(89)
a=my_list.loop(67)
print('popped Element')
my_list.clear()
print(my_list)

# Accessing Elements
# accessing elements is the same as accessing strings in python.
# you pass the index values and hence can obtain the values as needed
 
my_list=[78,98,90]
for element in my_list:
    print(element)
    print(my_list)
    print(my_list[90])
    print(my_list[0:78])
    print(my_list[::-1])

# len()returns the length of the list
# index()finds the index value of value passed where it has been encountered the first time
# count()finds the count of the value passed to it
# sorted() and sort()do the same thing that is to sort the values of the list
# the sorted()has a return type whereas the sort()modifies the original list

my_list=[2,3,4,90,76,45,89,67]
print(len(my_list))
print(my_list.index(67))
print(my_list.count(67))
print(sorted(my_list))
my_list.sort(reverse=True)
print(my_list)

# Dictionary they are used to store keyvalue pairs
# creatind a Dictionary
my_dict ={}
print(my_dict)
my_dict ={1: 'python',2: 'javascript'}
print(my_dict)

# changing and adding key,value pairs
# to change values in dictionary you first access the key and then change the value accordingly

my_dict ={'First':'python'}
print(my_dict)
my_dict['first']='kotlin'
print(my_dict)
my_dict['second']='Javascript'
print(my_dict)

# Tupleone data enter into tuple cannot be changed no matter what
# when the data inside the tuple is mutable only then the tuple data can changed 
my_tuple =(1,2,3,4,5)
print(my_tuple)

# set are colletion of unordered elements that are uniquie meaning that even if the data is repeated more than one time
#  it would be entered into the set only once 
# creating a set
my_set={1,3,6,7,8,3}
print(my_set)

# adding elements

my_set={6,8,9}
my_set.add(4)
print(my_set)
# add element to set

# oparation in sets
my_set={56,87,90,23,54}
my_set_2={67,7,8,9}
print(my_set.union(my_set_2))
print(my_set.intersectins(my_set_2))
print(my_set.difference(my_set_2))
print(my_set.symmetric_difference(my_set.clear))
print(my_set)

# union()combines the data present in both sets.
# intersection()finds the data present in both sets only
# difference()deletes the data present in bot outputs data present only in the set passed
# symmetric_difference()doese the same as the difference()
# but outputs the data wich is remaining in both sets

