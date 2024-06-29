""" L05 sumar ab > a + b """
two_digit_number = input() #input = XX
num = int(two_digit_number) # force int / two_digit_number(39) = str not int
a = num // 10 # decenas
b = num % 10 # unidades
print(a + b)
"""L05 ver 2"""
two_digit_number = input()
first_digit = int(two_digit_number[0]) #access 1st
second_digit = int(two_digit_number[1]) #access 12nd
two_digit_number = first_digit + second_digit
print(two_digit_number)
