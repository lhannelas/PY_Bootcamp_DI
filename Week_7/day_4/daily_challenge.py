print("hello world!")


def div(a, b):

    try:
        print(a / b)
    except ZeroDivisionError:
        # this code will be running if we get an exception zero division error
        print("you cannot divide by zero")


div(5, 0)
