def find_smallest_factor():
    def smallest_factor(n):
        for i in range(2, n):
            if n % i == 0:
                return i
        return n

    while True:
        try:
            print("________________________________________________")
            n = int(input("Enter a number that isn't a negative number: "))
            if n > 0:
                print(f"The smallest factor of {n} is {smallest_factor(n)}")
                print("________________________________________________")
            else:
                print("Invalid input. Enter a number greater than 0.")
                print()
                continue
        except ValueError:
            print()
            print("________________________________________________")
            print("Invalid input. Please enter a number.")
            continue

        while True:
            print()
            want_to_continue = input("Do you want to try another number? (yes/no): ").strip().lower()

            if want_to_continue in ('yes', 'y'):
                break
            elif want_to_continue in ('no', 'n'):
                print()
                print("________________________________________________")
                print("Thank you for using the smallest factor finder!")
                print("________________________________________________")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

def find_prime_numbers():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    while True:
        print()
        start = int(input("Enter the start number: "))

        if start == 0:
            print()
            print("Program terminated.")
            print("___________________")
            return

        if start < 0:
            print()
            print("Enter a non-negative number.")
            print("____________________________")
            continue

        end = int(input("Enter the end number: "))

        if end <= start:
            print()
            print("Enter a number greater than", start)
            print("_____________________________")
            continue

        print("Prime numbers between", start, "to", end, "are:")
        for num in range(start, end + 1):
            if is_prime(num):
                print(num, end=' ')
                print()
        print("__________________________________")

while True:
    print("Selects 1, the code for  finding the smallest factor of n and Selects 2, the code for  finding the prime numbers of range: ")
    start1 = int(input())
    if start1 == 1:
        find_smallest_factor()
    elif start1 == 2:
        find_prime_numbers()
    else:
        print("Invalid input. Please enter 1 or 2.")