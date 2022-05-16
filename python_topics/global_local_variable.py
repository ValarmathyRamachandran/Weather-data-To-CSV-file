import random

num1 = 4  # global variable


def func_multiply():
    num2 = 5  # local variable
    multiply = num1 * num2
    return multiply


if __name__ == "__main__":
    m = func_multiply()
    print(m)
    print(random.random())
