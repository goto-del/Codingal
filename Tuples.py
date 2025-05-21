tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

tuplex = (4, 6, 2, 8, 3, 1, 7, 2, 2)
print(tuplex)

tuplex = tuplex + (9,)
print(tuplex)

print(tuplex.count(2))
print(tuplex[3:6])

# use tuple[start:stop]
# the start index is incusive and the stop index is exclusive
# If there is no star index it will start from 0

print(tuplex[:4])