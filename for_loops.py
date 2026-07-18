# for x in reversed(range(1, 11)):
#     print(x)

# for x in (range(1, 11, 3)):
#     print(x)

for x in (range(10, 21)):
    if x == 13:
        break
    print(x)
print(" ")
for x in (range(10, 21)):
    if x == 13:
        continue
    print(x)
