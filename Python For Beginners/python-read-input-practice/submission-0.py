def add_two_numbers() -> int:
    user_input = input ()
    string_list = user_input.split(",")
    integer_list = []
    for number in string_list:
        integer_list.append(int(number))
    return sum(integer_list)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())