# yield can be used as an expression


# if you use yield like so, you create a coroutine
# now it generate and consume values sent to it
def finder(x):
    while True:
        input_text = yield
        if x in input_text:
            print(input_text)
        else:
            print("Couldn't find any matches")


f = finder("python")
print(f)

# PRIMING the coroutine, in order to start it
# 1st way
f.send(None)

# 2nd way
# next(coroutine_name)

#
f.send("this is a dtewfd")
f.send("a python string lmao")

# close a coroutine
f.close()

# raise an exception inside a coroutine
# f.throw(AttributeError)
