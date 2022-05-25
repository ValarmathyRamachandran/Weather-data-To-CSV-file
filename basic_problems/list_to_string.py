# convert a list into a string
def week():
    weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    list_as_string = ' '.join(weekdays)
    # we can use the <”.join()> method which joins all the elements
    # into one and returns as a string.
    return list_as_string


# convert a list into a tuple
def tuple_week():
    weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    list_as_tuple = tuple(weekdays)
    # By using Python <tuple()> function we can convert a list into a tuple.
    # But we can’t change the list after turning it into tuple, because it becomes immutable.
    return list_as_tuple


# list into Set
def set_week():
    weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'tue']
    list_as_set = set(weekdays)
    # converting  list into set by using <set()> function
    return list_as_set


# count the occurrences of a particular element in the list
def count_week():
    weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
    return weekdays.count('mon')


# count the occurrences of  all elements in the list
def count_each():
    weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
    return [[day, weekdays.count(day)] for day in set(weekdays)]


if __name__ == "__main__":
    w = week()
    print("List to string", w)
    t = tuple_week()
    print("List to Tuple", t)
    s = set_week()
    print("List to Set", s)
    c = count_week()
    print("Count of element", c)
    e = count_each()
    print("Count of each element", e)
