# Lists: ordered, mutable, allows duplicate items
def func_lists():
    # creating a empty list
    my_list = list()

    # creating a list, interesting way
    # my_list = a_list * number_of_repetitons
    my_list = [0, "123", 21] * 5
    print(my_list)

    # init a list
    my_list = ["string", 102, 0.132, "yes", False]
    print(my_list)

    # accessing last item
    item = my_list[-1]  # -2 = penultimul si etc

    # traversal
    for i, x in enumerate(my_list):
        print(i, ' ', x)
    # for(int i = my_list.size() - 1; i >= 0; i--)
    #     out<<my_list[i]<<'\n'
    for i in range(len(my_list) - 1, -1, -1):  # backwards
        print(my_list[i])

    # list1 = another_list[start_index, stop_index], stop_index excluded
    l2 = my_list[1:3]  # = list[1], list[2]
    l3 = my_list[:4]  # start_index = 0
    l4 = my_list[2:]  # stop_index = end of list
    # this is the step_index aka how many steps it takes on each iteration
    l5 = my_list[::1]

    # reverse a list
    my_list.reverse()
    another_list = my_list[::-1]

    # add items
    my_list.append("fwef")  # adds element at the end
    my_list.append(["f182", "wfhei", "1023k", 239])  # appends list at the end

    # lists can be concatenated with the + operator
    my_list = [0, 123, 19, "fwef"] + [0, 1, 1, 1, 214, "l"]

    # inserts at position i, and shifts all the elements from i to i+1
    my_list.insert(1, "blueberry")

    # delete element
    my_list.pop()  # returns last item and removes it
    my_list.remove("blueberry")
    my_list.clear()  # deletes all elements

    # sorting
    my_list.sort(reverse=False)  # implicit reverse=False
    new_list = sorted(my_list, reverse=False)  # or True

    # copying
    # NOT GOOD, BOTH LISTS WILL REFER TO THE SAME LOCATION IN MEMORY
    # AKA u modify one, its going to modify the other aswell
    my_list = another_list  # BAD METHOD!!!!!!

    # todo GOOD METHOD OF COPYING
    my_list = another_list.copy()
    my_list = list(another_list)
    my_list = another_list[:]

    # trick

    my_list = [1, 2, 3, 4, 5]
    # expression then for
    sq_list = [x*x for x in my_list]
    print(sq_list)
