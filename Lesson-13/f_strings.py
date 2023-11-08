person = "Dave"
coin = 3

message = "\n %s has %s coins left." % (person, coin)
print(message)

message = "\n {} has {} coins left." .format(person, coin)
print(message)

message = "\n {1} has {0} coins left." .format(coin, person)
print(message)

message = "\n {person} has {coins} coins left." .format(
    person=person, coins=coin)
print(message)

player = {'person': 'Dave', 'coins': 3}

message = "\n {person} has {coins} coins left." .format(
    **player)
print(message)

# F string

message = f"\n{person} has {coin} coins left."
print(message)

message = f"\n{person.lower()} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {2*5} coins left."
print(message)

message = f"\n{player['person']} has {2*5} coins left."
print(message)


num = 10

print(f"\n2.25 Times {num} is {2.25*num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 Times {num} is {2.25*num:.2f}")

for num in range(1, 11):
    print(f"{num} divided 4.52 is {num/4.52:.2%}")


print(f"{5:.2f}")
