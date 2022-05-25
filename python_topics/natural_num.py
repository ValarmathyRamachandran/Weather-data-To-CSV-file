def natural_num(number):
    num = 1
    for num in range(1, number + 1):
        print(num, end=' ')


def natural_num_while(n):
    while n >= 1:
        print(n, end='  ')
        n = n - 1


if __name__ == "__main__":
    numbers = int(input("Please Enter any Number: "))
    natural_num(numbers)
    print("|")
    natural_num_while(numbers)
