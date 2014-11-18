###################################################################
### Projet 5 : Convertisseur nombre à virgule en nombre binaire ###
###################################################################

# Convertion de str en int
ch= str(input("Nombre à virgule à transposer :"))
ch1= ","
ch2= ch.find(ch1) #Cherche le rang de la virgule donc "ch1" dans la chaîne "ch"
ch3= (ch[:ch2]) #Ne garde que les caractère avant la virgule
ch4= (ch[ch2+1:]) #Ne garde que les caractère après la virgule
nb_av= int(ch3) #Convertit la chaîne ch3 en nombre entier
nb_ap= int(ch4) #Convertit la chaîne ch4 en nombre entier
a=len(ch4)      #nombre de chiffre après la virgule


# Partie entière
nb_1= bin(nb_av)[2:]

# Partie fractionnaire
nb_2= (nb_ap/(10**a)) 
bits= int(input("Précision souhaiter :"))
k=0
nb_4=''
while k<bits:
    nb_3=(nb_2*2)
    if nb_3 <1:
        nb_4=nb_4 +'0'
        nb_2=nb_3
    elif nb_3 >1:
        nb_4=nb_4 +'1'
        nb_2=nb_3-1
    k=k+1

# Fin du programme
print(ch,"en base 10 =",nb_1,",",nb_4,"en base 2")

