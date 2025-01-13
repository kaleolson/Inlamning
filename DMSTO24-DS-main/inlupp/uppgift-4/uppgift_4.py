# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: int) -> list[int]:
    mylist =[]
    x = 0
    y = 0
    i = 0
    if x == 0 and n >0:
        mylist.append(x)
        x += 1
        i += 1
    while i < n:
        mylist.append(x)
        x = x + y
        y = x - y
        i += 1    
    return mylist
#print(fibonacci(7))

