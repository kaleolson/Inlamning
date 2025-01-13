# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(numbers: list[int]) -> list[int]:
    i = 0
    mylist = []
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            mylist.append(numbers[i])   
        i += 1
    return mylist
#print(filter_odd([14,15,15,18]))
