# Prime Number Checker and Generator

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


print("Prime Number Program")
print("1. Check single number")
print("2. Generate primes in range")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(number, "is a Prime Number")
    else:
        print(number, "is NOT a Prime Number")

elif choice == '2':
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    print("Prime numbers between", start, "and", end, "are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

else:
    print("Invalid choice")