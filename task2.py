"""
===================   TASK 2   ====================
* Name: Product Of Digits
*
* Write a script that will take an input from user
* as integer number and display product of digits
* for a given number. Consider that user will always
* provide integer number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

# Write your code here


def product_digits(number):

    # Provjeravamo da li je intiger
    if not isinstance(number, int):
        return False

    # Initialize product value
    product_sum = 1


    # NOTE: Napravimo je da radi za negativne brojeve

    number = abs(number)


    while number > 0:
        digit = number % 10
        number = number // 10
        product_sum *= digit

    return product_sum


def main():

    int_number = 1234
    product_sum = product_digits(int_number)
    print("Proizvod cifara je : ", product_sum)

main()


