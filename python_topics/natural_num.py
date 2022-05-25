# sum of natural numbers 
def natural_num(number):
    if number <= 1:
        return number
    natural = number + natural_num(number - 1)
    print(natural)
    return natural


if __name__ == "__main__":
    num = int(input("enter number:"))
    n = natural_num(num)
    print("Sum of natural numbers of ", num, "=", n)
