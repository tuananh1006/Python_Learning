users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-3])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(users))

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])

print(users)

# users.extend(data)
# users += data
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)


users[1:3] = ['Robert', 'JPJ']

users.remove('Bob')
print(users)

users.pop()
print(users)

# del users[0:]
# print(users)

# del data
data.clear()
print(data)

users[1:2] = ['dave']
# users.sort(key='str.lowwer')
print(users)

users.sort()
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# Descending
# nums.sort(reverse=True)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)

mylist = list([1, 2, 3])

# Tuple

mytuple = tuple(('Daves', 42, True))

anothertuple = (1, 4, 2, 8)

print(mytuple)
print(type(mytuple))
print(anothertuple)
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
