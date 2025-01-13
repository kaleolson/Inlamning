# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.

def multiplication_table(n: int, limit: int) -> list:
    i = 1
    x = 0
    mylist = []
    while i <= limit:
        x = n * i
        mylist.append(x)
        i += 1
    return mylist
#print(multiplication_table(2,4))