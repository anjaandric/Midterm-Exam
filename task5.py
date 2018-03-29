"""
===================   TASK 5   ====================
* Name: Del Boy Millionaire
*
* Help Del Boy become a millionaire. Del Boy is
* trading bitcoins on crypto-exchanges with simple
* algorithm. He is buying where the price of bitcoin
* is the lowest and selling where the bitcoin is
* the most expensive. Write a function `get_profit`
* which will take a list of bitcoin prices in USD as
* argument. The function should return what is the
* maximum possible profit for given bitcoin prices
* on different exchanges.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
# Write your function here


niz = ['12','16','177','34']




max_niza = niz [0]

for i in range(len(niz)-1):
    if max_niza < niz [i+1]:

        max_niza = niz[i+1]

    return max_niza

for i in range(len(niz)-1):
    if min_niza > niz [i+1]:
        min_niza = niz [i+1]

    return min_niza





print("Maksimum niza je: ",max_niza)
print("Minimum niza je, ",min_niza)
print("Razlika maksimalnog i minimalnog niza je: ",max_niza1)