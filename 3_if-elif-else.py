
'''
#job 1

valeur1 = "égal"
valeur2 = "non égal"
valeur1 = int(input("Entrez valeur1 :"))
valeur2 = int(input("Entrez valeur2 :"))
if valeur1==valeur2:
    print("Oui, ils sont égaux")
else:
    print("Non, ils ne sont pas égaux.")


#job 2

age = int(input("Entrez votre age"))
if age >= 18:
    print("Vous pouvez voter.")
else:
    print("Vous ne pouvez pas voter.")


#job 3

for i in range(0, 101):
    if i not in [26, 37, 88]:
        print(i)


#job 4

for i in range(1, 101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0 :
        print("Buzz")
    else:
        print(i)



#job 5

def les_nombres_premiers(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5+1)):
        if n%i == 0:
            return False
    return True

for num in range(2, 1001):
    if les_nombres_premiers(num):
        print(num)


#job 6

nombre = int(input("Entrez un numero : "))
if nombre%2==0:
    print(f"Le nombre {nombre} est pair.")
else:
    print(f"le nombre {nombre} est impair.")
    

#job 7

chaine = "abcdefghijklmnopqrstuvxwyz"
ind = 0
haut = 1
while ind+haut <= len(chaine):
    print(chaine[ind:ind+haut])
    haut += 1

'''
#job 8

a = int(input("Entrez la première longueur : "))
b = int(input("Entrez la deuxième longueur : "))
c = int(input("Entrez la troisième longueur : "))

if a + b > c and a + c > b and b + c > a:
    print("Il est possible de construire un triangle.")
    if a == b == c:
        print("C'est un triangle équilatéral.")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("C'est un triangle isocèle et rectangle.")
        else:
            print("C'est un triangle isocèle.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("C'est un triangle rectangle.")
    else:
        print("C'est un triangle quelconque.")
else:
    print("Il n'est pas possible de construire un triangle avec ces longueurs.")





