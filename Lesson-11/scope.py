name = "Dave"
count = 1


def another():
    color = "blue"
    global count
    count = 2
    print(count)

    def greeting(firstname):
        # nonlocal color
        color = "red"
        print(color)

        print(name)
        print(firstname)
    greeting("Dave")


another()
print(count)
