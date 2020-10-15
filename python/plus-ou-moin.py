# on apporte une librairie pour choisir un nombre aleatoire
import random 

# on cree une vaiable nombre_cache
#on y stock un nombre aleatoire entre 0 et 100
# on fait appel a la fonction randint qui se trouve dans random
nombre_cache = random.randint(0,100)

print("tape un nombre entre 0 et 100")
entree_joueur = int( input(">>") )

print(entree_joueur)
if  entree_joueur < nombre_cache :
    print("ton nombre est trop petit")
elif entree_joueur > nombre_cache:
    print("ton nombre est trop grand")
else : 
    print("bravo!")
