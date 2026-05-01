def check_odd_even(num):
    '''Check if a number is odd or even.'''
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Test the function
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = check_odd_even(number)
    print(f"{number} is {result}")
