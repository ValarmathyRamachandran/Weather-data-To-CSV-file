# reverse a given word
def reverse_fn(string):
    s = " "
    for letter in string:
        s = letter + s
        # print(letter)
        # print(s)
    return s


if __name__ == "__main__":
    word = input("enter the word you want to reverse")
    r = reverse_fn(word)
    print(r)
