# Strings: ordered, immutable, text representation
def func_strings():
    my_string = "oooooo"
    my_string = 'oooooo'
    my_string = """Multiple\
    Lines \
    Of Code"""
    print(my_string)
    # my_string[0] = 'f' !ERROR!

    # remove whitespace
    my_string = my_string.strip()
    print(my_string)

    # searching stuff
    my_string.startswith("substring")
    my_string.endswith("substring")
    print(my_string.find('f'))
    print(my_string.find('llo'))  # outputs the start_index of the substring
    my_string.count('substr')  # returns the number of time substr exists

    # other
    my_string.replace('Code', 'something')

    # from list to string
    my_list = list()
    my_string = ''.join(my_list)
