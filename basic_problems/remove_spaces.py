# remove white spaces from string
def remove_spaces(word):
    word = "".join(word.split(' '))
    return word


if __name__ == "__main__":
    w = input("enter the word:")

    print("After removing spaces :", remove_spaces(w))
