################Lists

# Assign a list to an variable named my_list
my_list = [1,2,3]

my_list = ['A string',23,100.232,'o']

# Length of object
len(my_list)

# Indexing and Slicing

my_list = ['one','two','three',4,5]

# Grab element at index 0
my_list[0]

# Grab index 1 and everything past it
my_list[1:]

# Grab everything UP TO index 3
my_list[:3]


# Reassign
my_list = my_list + ['add new item permanently']

my_list

# Make the list double
my_list=my_list * 2

my_list

# Append
list1 = [1,2,3]

list1.append('append me!')

list1

# Pop off the 0 indexed item
list1.pop(0)

list1

# Use reverse to reverse order (this is permanent!)
list1.reverse()

list1

# Sorting
new_list=[3, 2, 5, 1, 7]

new_list.sort()

new_list

################Dictionaries

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

# Call values by their key
my_dict['key2']


my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Let's call items from the dictionary
my_dict['key3']

# Can call an index on that value
my_dict['key3'][0]

# Create a new dictionary
d = {}

# Create a new key through assignment
d['animal'] = 'Dog'

# Can do this with any object
d['answer'] = 42

d

# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}

# Method to return a list of all keys 
d.keys()

# Method to grab all values
d.values()

# Method to return tuples of all items  
d.items()


################Set and Booleans
#Sets are an unordered collection of unique elements.

x = set()

# We add to sets with the add() method
x.add(1)

x

# Add a different element
x.add(2)

x

# Try to add the same element
x.add(1)

x
#Notice how it won't place another 1 there.

#We can use set to distinct values
# Create a list with repeats
list1 = [1,1,2,2,3,4,5,6,1,1]

set(list1)
