this_list = ["apple", "banana", "cherry", "orange", "mango"]

# Change item values
this_list[1] = "blackberry"
print(this_list)

# change range of items
this_list[1:3] = ["blackberry", "watermelon"]
print(this_list)

    ## sort() method ##
# sorts list alphabetically ascending
# sorts capital before lowercase
this_list.sort()
print(this_list)
this_list.sort(reverse= True) # for decending order
print(this_list)

    ## insert() method ##
# inserts an item at the sepcified index
this_list.insert(2, "watermelon")
print(this_list)

    ## append() method ##
# to add an item at the end of list
this_list.append("kiwi")
print(this_list)

    ## extend() method ##
# to append elements from another list to current list
another_list = ["strawberry", "pineapple"]
this_list.extend(another_list)
print(this_list)

# it can add sets, tuple and dictionaries too
this_tuple = ("tuple", "tuples")
this_list.extend(this_tuple)
print(this_list)

    ## remove() method ##
# removes the specified item; if mutiple removes the first occurance
this_list.remove("kiwi")
print(this_list)

    ## pop() method ##
# removes the specified index
this_list.pop(1)
print(this_list)

del this_list[0] # also works 

    ## clear() method ##
# empties the list
this_list.clear()
print(this_list)

