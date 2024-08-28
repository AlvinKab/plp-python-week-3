# Challenge 1
def large_power(base, exponent):
    return base ** exponent > 5000

base_num = float(input("Enter the base number: "))
exp_num = float(input("Enter the exponent number: "))
print(f"Result larger than 5000: {large_power(base_num, exp_num)}")
    
# Challenge 2
def divisible_by_ten(num):
    return num % 10 == 0

number  =int(input("Enter a number: "))
print(f"Divisible by 10: {divisible_by_ten(number)}")