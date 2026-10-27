# Program to check whether a number is a Prime Number

# Taking input from the user
num = int(input("Enter a number to check: "))

# Prime numbers must be greater than 1
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    # Assume the number is prime initially
    is_prime = True
    
    # Check for factors from 2 up to the square root of the number (or num - 1)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break # Found a factor, no need to check further

    # Displaying the result based on the flag
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
