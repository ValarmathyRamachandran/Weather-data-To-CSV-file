# def is_balanced(equation):
#     while len(equation) != 0:
#         equation = equation.replace('()', "")
#         equation = equation.replace('[]', "")
#         equation = equation.replace('{}', "")
#     if len(equation) == 0:
#         return True
#
#     return False


def check(expression):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []

    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"


def is_balance(s):
    if len(s) % 2 != 0:
        return False
    dict_elements = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for i in s:
        if i in dict_elements.keys():
            stack.append(i)
        else:
            if not stack:
                return False
            a = stack.pop()
            if i != dict_elements[a]:
                return False
    return stack == []


if __name__ == "__main__":
    # eq = "({{}})"
    # print("given equation is balanced ", is_balanced(eq))

    string = "{[a+b]{(c)}}"
    print(string, "-", check(string))

    string = "(((d)"
    print(string, "-", check(string))

    strs = "{[a+b]{(c)}"
    print(strs, "-", is_balance(strs))
