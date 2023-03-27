print("Test if taking the power of one number to another number is > 5000")
def  large_power(base, exponent):
    result = base ** exponent

    if(result > 5000):
        return True
    return False
print(large_power(19, 4))

print("Check if number is divisible by 10")

number = int(input("Please enter a number: "))
def divisible_by_ten(num):
    num = number
    if num % 10 == 0:
        return True
    else:
        return False
print(divisible_by_ten(number))
