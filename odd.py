def even_odd_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(even_odd_number(number))
