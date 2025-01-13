# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(string):
    # gör om till små bokstäver
    cleaned_string = string.lower()
    
    # Jämför om strängen är lika med sin omvända version
    return cleaned_string == cleaned_string[::-1]