# en python , il existe 2 type de boucle
# while = tant que ...
# for = pour chaque ...
# le resultat de la condition d'une boucle est soit :
# True (vrai)
# False (faux)

nombre = 10
flag = True

while nombre >= 0: 
    print(nombre)
    nombre = nombre -1

print("----------------")

while flag == True:
    print("ok")
    flag = False

print("----------------")

for lettre in "maison a moi":
    print(lettre)

print("----------------")

phrase ="bientot la pause"
for lettre in phrase :
    if lettre in "aeiouy":
        print(lettre)
