print("Hello World!")


'''
    Zakladne konvencie zapisu

    Triedy: nazov triedy sa zacina velkym pismenoa 
    a ostatne su male pricom sa pozostava z viacerych slov
    kazde nove slove sa zacina velkym pismeno.
->  class VypocetRychlosti:


    Konstanty: zapisuju sa velkymi pismenami, ak pozostava z viacerych slov, 
    pouzijime podrtrznik.
->  MAX_HODNOTA = 5


    Premenne: zapisuju sa malymi pismenami, pricom ak pozostava z viacerych slov, 
    kazde nove slovo zacina z velkeho pismena.
->  rychlostEfekotra = 10

    Baliky: zapisuju sa iba malymi pismenami, bez ohladu na 
    z kolkich slov pozostavaju.
->  vypocetrychlosti

'''

# Implicitne definovanie datoveho typu
i = 25
meno = "Mykhailo"
PI = 3.1415926

# Explicitne definovanie datoveho typu
i: int = 25
meno: str = "Mykhailo"
PI: float = 3.1415926

# Komplexne cislo
c = 2 + 3j

tlacidlo = True
stav = False

number = [1, 2, 3]  # <list> - zoznam (menitelny)
point = (10, 20)    # <tuple> nemenitelny

r = range(5)        # range - postupove cisla: 0, 1, 2, 3, 4

fruits = {"apple", "banana", "orange"} # set - mnozine


# Matematicke operatory
# + - * / **
a = 10
b = 20
c = a + b
