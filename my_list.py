# 1. Creating an empty list (my_list)
my_list = []

# 2. Appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Inserting the value 15 at the second position in the list
my_list.insert(1, 15)  # Index 1 is the second position

# 4. Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Remove the last element from my_list
my_list.pop()  

# 6. Sort my_list in ascending order
my_list.sort()

# 7. Finding and printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(index_of_30)
