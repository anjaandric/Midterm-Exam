"""
===================   TASK 3   ====================
* Name: Negative and Non-Negative Elements
*
* Write a script that will populate a list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that
* user will always provide integer numbers. At the
* end, the script should print how many negative
* and non-negative numbers there were present in
* the list.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

def negativan(broj):

    if broj < 0:
        return True
    else:
        return False



duzina_lista = int(input("Koliko brojeva ima lista? "))



lista = []


for i in range(duzina_lista):
    novi_broj = int(input("Unesi novi broj #" + str(i+1) + ": "))
    lista.append(novi_broj)


negativni = nenegativni = 0

for broj in lista:


    if negativan(broj):
        negativni += 1
    else:
        nenegativni += 1
print("Lista brojeva je: ",lista)
print("Negativnih je: ",negativni)
print("Nenegativnih je: ",nenegativni)