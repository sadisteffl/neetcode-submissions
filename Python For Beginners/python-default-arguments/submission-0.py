def greet(name, punctuation) -> None:
    print("Hello, " + name + punctuation)


def greet(name, punctuation="!") -> None:
    print("Hello, " + name + punctuation)

greet("World", "!")
greet("World")


