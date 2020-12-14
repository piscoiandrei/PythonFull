import secrets


def count_occurences():
    iteration = 0
    while True:  # or when you remain without data in dataset\

        print(f"This is iteration no. {iteration}")
        iteration += 1
        # equivalent of extracting data from database
        s = secrets.token_hex(128)  # generate a hex sequence of 8bytes

        # process data
        data = dict()
        for c in s:
            if c in data.keys():
                data[c] += 1
            else:
                data[c] = 0

        yield data


def exec_counter(x):
    cnt = count_occurences()

    print(cnt)

    while x:
        print(next(cnt))
        x -= 1


exec_counter(2)
