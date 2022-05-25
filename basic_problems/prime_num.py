def prime_num(num):
    if num <= 1:
        return "Number is not Prime number"
    else:
        for n in range(2, num):
            if num % n == 0:
                return "it is not Prime number"
            return "It is Prime Number"


if __name__ == "__main__":
    p = int(input("enter the number:"))
    print(prime_num(p))
