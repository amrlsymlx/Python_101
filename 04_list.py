friends = ["Ali", "Abu" , "Bakar" , "John" , "Emma", "Amin"]

print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[1:3]) #grab up to 1 not including 3

friends[1] = "Jane"
print(friends)

random_numbers = [11,13,25,47,56,12,1,]
friends.extend(random_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Creed")
print(friends)

friends.pop()
print(friends)

friends.pop()
print(friends)

print(friends.index("Jane"))

friends.clear()
print(friends)

friends = ["Ali", "Abu" , "Bakar" , "John" , "Emma", "Amin", "Jim", "Jim","Jim",]
print(friends.count("Jim"))

random_numbers.sort()
print(random_numbers)

random_numbers = [11,13,25,47,56,12,1,]
random_numbers.reverse()
print(random_numbers)

friends2 = friends.copy()
print(friends2)

# this is tuples, tuples cannot be modified
coordinate = (4,5)
# coordinate[1] = 10
# print(coordinate)
#error
