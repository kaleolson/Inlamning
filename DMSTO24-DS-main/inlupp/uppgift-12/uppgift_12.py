# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students):
    #loopa igenom listan med namn som nyckel och ålder som värde.
    return {name: age for name, age in students}