# create an empty list called my_list

my_list =[]

#Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert the value 15 at the secong position of the list
my_list.insert(1,15)

#extend my list with another list:{50,60,70}

my_list.extend([50,60,70])

#remove the last element from my_list
my_list.pop()

##sort my_list in ascending order
my_list.sort()

#Find and print the index of the value 30 in my_list
my_list.sort()

#Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)

#print my_list
print("Final my_list:", my_list)

