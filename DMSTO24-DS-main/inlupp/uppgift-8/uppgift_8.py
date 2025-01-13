# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(string):
    letter_count = {}
    
    # Loopa genom varje tecken i strängen
    for char in string.lower():
        # Vi räknar endast med bokstäver
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                # Om bokstaven inte finns, lägg till den med värdet 1
                letter_count[char] = 1
    
    return letter_count
