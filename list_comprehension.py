# list Comprehension = A concise way to create list in python 
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]



# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)


# doubles = [expression for value in iterables if condition]

# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)


# fruits = ["apple", "banana", "orange", "tomato"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# fruits = [fruit[0] for fruit in fruits]
# print(fruits)


numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
positive_nums = [num for num in numbers if num > 0]
negative_nums = [num for num in numbers if num < 0]
print(positive_nums)
print(negative_nums)