cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]

#partie1
#1.1
N = 15
def init_bonus():
    grille = []
    for i in range(N):
        ligne = []
        for j in range(N):
            ligne.append("")
        grille.append(ligne)

    for coords in cases_MT:
        i,j = coords
        grille[i][j] = "MT"
    for coords in cases_MD:
        i,j = coords
        grille[i][j] = "MD"
    for coords in cases_LT:
        i,j = coords
        grille[i][j] = "LT"
    for coords in cases_LD:
        i,j = coords
        grille[i][j] = "LD"
    return grille

#1.2
def init_jetons():
    grille = []
    for i in range(N):
        ligne = []
        for j in range(N):
            ligne.append("")
        grille.append(ligne)
    return grille

#1.3
def affichage_jetons(J):
    for ligne in J:
        l = ""
        for jeton in ligne:
            l += "-" + str(jeton) + "-"
        print(l)
    return l
J = init_jetons()
for coords in cases_MT:
        i,j = coords
        J[i][j] = "MT"
for coords in cases_MD:
        i,j = coords
        J[i][j] = "MD"
for coords in cases_LT:
        i,j = coords
        J[i][j] = "LT"
for coords in cases_LD:
        i,j = coords
        J[i][j] = "LD"

# program principal de partie 1
print('Bienvenue à Scrabble')
init_bonus()
init_jetons()
affichage_jetons(J)


#partie 2
#2.1
def init_dico():
  madict = dict()
  madict['A'] = {'occ' : 9, 'val' : 1}
  madict['B'] = {'occ' : 2, 'val' : 3}
  madict['C'] = {'occ' : 2, 'val' : 3}
  madict['D'] = {'occ' : 3, 'val' : 2}
  madict['E'] = {'occ' : 15, 'val' : 1}
  madict['F'] = {'occ' : 2, 'val' : 4}
  madict['G'] = {'occ' : 2, 'val' : 2}
  madict['H'] = {'occ' : 2, 'val' : 4}
  madict['I'] = {'occ' : 8, 'val' : 1}
  madict['J'] = {'occ' : 1, 'val' : 8}
  madict['K'] = {'occ' : 1, 'val' : 10}
  madict['L'] = {'occ' : 5, 'val' : 1}
  madict['M'] = {'occ' : 3, 'val' : 2}
  madict['N'] = {'occ' : 6, 'val' : 1}
  madict['O'] = {'occ' : 6, 'val' : 1}
  madict['P'] = {'occ' : 2, 'val' : 3}
  madict['Q'] = {'occ' : 1, 'val' : 8}
  madict['R'] = {'occ' : 6, 'val' : 1}
  madict['S'] = {'occ' : 6, 'val' : 1}
  madict['T'] = {'occ' : 6, 'val' : 1}
  madict['U'] = {'occ' : 6, 'val' : 1}
  madict['V'] = {'occ' : 2, 'val' : 4}
  madict['W'] = {'occ' : 1, 'val' : 10}
  madict['X'] = {'occ' : 1, 'val' : 10}
  madict['Y'] = {'occ' : 1, 'val' : 10}
  madict['Z'] = {'occ' : 1, 'val' : 10}
  madict['?'] = {'occ' : 2, 'val' : 0}
  return madict
  
#2.2
def init_pioche(dico):
  L = []
  for i in dico:
    occ = dico[i]['occ']
    for j in range(occ):
      L.append(i)
  return L

#2.3
import random
def piocher(x, sac):
  for i in range(x):
    v = random.choice(init_pioche(dico))
    sac.append(v)
  if len(sac) != x:
    t = len(sac)
    sac.clear()
    for i in range(t-x):
      k = random.choice(init_pioche(dico))
      sac.append(k)
  return sac

#2.4
import random
def completer_main(main,sac):
  c = 7 - len(main)
  if (len(sac) - c) < 0:
    for i in range(len(sac)):
      random.shuffle(sac)
      v = sac.pop()
      main.append(v)
    
  else:
    for i in range(c):
      random.shuffle(sac)
      v = sac.pop()
      main.append(v)

#2.5
def echanger(jetons, main, sac):
  if len(sac) < len(main):
    return 'échoué'
  else:
    for i in range(len(main)):
      random.shuffle(sac)
      v = sac.pop()
      jetons.append(v)
    for j in range(len(main)):
      v = main[j]
      sac.append(v)
    main.clear()
    main.append(jetons)
    
    return 'réussi'


# programme principal partie 2
init_dico()
dico = init_dico()
init_pioche(dico)
x = 7
sac = []
piocher(x, sac)
main = [1,2,3,4]
sac = piocher(x, sac)
completer_main(main,sac)
echanger([], main, sac)


#partie 3
#3.1
def generer_dico(nf):
  mots = list(nf)
  return mots

#3.3
def mot_jouable(mot, ll):
  def compte_carac(l, c):
      n = 0
      for i in l:
          if i == c:
              n+=1
      return n
  compte_carac(ll, 'A')

  def compte_alphab(l):
      counts = []
      for o in range(ord("A"), ord("Z")+1):
          c = chr(o)
          counts.append(compte_carac(ll, c))
      return counts
  compte_alphab(ll)

  countt = compte_alphab(ll)
  for i in range(len(mot)):
    t = ord(mot[i]) - 65
    y = countt[t]
    if y > 0:
      countt[t] -= 1
    else:
      return False
  return True
  
#3.4
def mots_jouables(motsfr, ll):
  nouvelle_liste = []
  for i in range(len(motsfr)):
    if mot_jouable(motsfr[i], ll) == True:
      nouvelle_liste.append(motsfr[i])
    else: continue
  return nouvelle_liste

#3.6
def mots_jouables_manquant(motsfr, ll,lettremanquante):
  liste2 = ll
  nouvelle_liste_2 = []
  n = lettremanquante
  while (n > 0):
    liste2.append('?')
    n = n - 1
  for mot in motsfr:
    if mot_jouable(mot, liste2) == True:
      nouvelle_liste_2.append(mot)
  return nouvelle_liste_2


# programme principal partie 3
nf = open("V:\motscrabble.txt")
generer_dico(nf)
ll = ['P','I','D','E','T','A','R']
mot_jouable("COURIR",ll)
motsfr = ['COURIR', 'PIED', 'DEPIT', 'TAPIR', 'MARCHER']
mots_jouables(motsfr, ll)
lettremanquante = 5
mots_jouables_manquant(motsfr, ll,lettremanquante)

#partie 4
#4.1
def valeur_mot(mot, dico):
  length = len(mot)
  somme = 0
  if length == 7:
    for i in range(length):
      somme = 50 
      somme = somme + dico[mot[i]]['val']
  else:
    for i in range(length):
      somme = somme + dico[mot[i]]['val']
  return somme

#4.2
def meilleur_mot(motsfr, ll, dico):
  meilleur_mot = ''
  plusgrand_mot = ''
  liste_mots = mots_jouables(motsfr, ll)
  if len(liste_mots) != 0:
    meilleure_valeur = valeur_mot(liste_mots[0] ,dico)
    plusgrand_mot = liste_mots[0]  
    for i in range(1,len(liste_mots)):
      valeur = valeur_mot(liste_mots[i] ,dico)
      if meilleure_valeur < valeur:
        meilleure_valeur = valeur
        plusgrand_mot = liste_mots[i]  
      else:
        continue
    meilleur_mot = plusgrand_mot
    
  return meilleur_mot

#4.3
def meilleur_mots():
  liste_meilleur_mots = []
  meilleurs_mots = meilleur_mot(motsfr, ll, dico)
  liste_meilleur_mots.append(meilleurs_mots)

  liste_mots = mots_jouables(motsfr, ll)
  liste_mots.remove(meilleurs_mots)
  for i in range(len(liste_mots)):
    if valeur_mot(liste_mots[i], dico) == len(meilleurs_mots):
      liste_meilleur_mots.append(liste_mots[i])
    else:
      continue 
  return liste_meilleur_mots


#programme principal partie 4
dico = init_dico()
valeur_mot('PYTHON',dico)
meilleur_mot(['COURIR', 'PIED', 'DEPIT', 'TAPIR', 'MARCHER'], ['P','I','D','E','T','A','R'], dico)
meilleur_mots()

#partie 5
#5.1
def lire_coords():
  lignes = list(input('Entrez des lignes sans des espaces: '))
  colonnes = list(input('Entrez des colonnes sans des espace: '))
  for m in lignes:
    a = int(m)
    lignes.remove(m)
    lignes.append(a)
  for n in colonnes:
    b = int(n)
    colonnes.remove(n)
    colonnes.append(b)
  for i in lignes:
      for j in colonnes:
          x = [i, j]
          if a not in cases_MT and not cases_MD and not cases_LT and not cases_LD:
            return x
          else:
            continue
  return x

def tester_placement(plateau,i,j,dir,mot):
  liste = []
  if len(mot) <= 7:
    if dir == 'horizontal':
      for a in range(len(mot)):
        if plateau[i][j+a] == '':
          liste.append(mot[a])
        if mot[a] != plateau[i][j+a]:
          break
        else:
          continue
      return liste
    else:
      for b in range(len(mot)):
        if plateau[i+b][j] == '':
          liste.append(mot[b])
        if mot[b] != plateau[i+b][j]:
          break
        else:
          continue
      return liste
  else:
    return liste

def placer_mot(plateau,lm,mot,i,j,dir):
  liste_necessaire = tester_placement(plateau,i,j,dir,mot)
  mot_necessaire = ''
  for i in range(len(liste_necessaire)):
    mot_necessaire = mot_necessaire + liste_necessaire[i]
  if mot_jouable(mot_necessaire, lm) == True:
    if dir == 'horizontal':
      for a in range(len(liste_necessaire)):
        plateau[i][j+a] = liste_necessaire[a]
        lm.remove(liste_necessaire[a])
    else:
      for b in range(len(liste_necessaire)):
        plateau[i+b][j] = liste_necessaire[b]
        lm.remove(liste_necessaire[a]) 
    return True
  else:
    return False

#5.4
def calcul_valeur(plateau,i,j,dir,mot,dico,main):
  valeur = valeur_mot(mot,dico)
  valeur2 = 1
  ligne = i
  colonne = j
  for l in mot:
    if plateau[ligne][colonne] == 'LT':
      valeur = valeur + dico[1]['val']*2
    elif plateau[ligne][colonne] == 'LD':
      valeur = valeur + dico[1]['val']
    elif plateau[ligne][colonne] == 'MT':
      valeur2 = 3
    elif plateau[ligne][colonne] == 'MD':
      valeur2 = 2

    plateau[ligne][colonne] = ''
    if plateau[ligne][colonne] == '2':
      valeur = valeur - dico[1]['val']
    if dir == 'horizontal':
      colonne = colonne + 1
  return valeur * valeur2

#principal 5
lire_coords()
plateau = init_jetons()
[i,j] = [0,0]
dir = 'horizontal'
mot = 'COURIR'
tester_placement(plateau,i,j,dir,mot)
lm = ['C','B','O','U','T','O']
placer_mot(plateau,lm,mot,i,j,dir)
calcul_valeur(plateau,i,j,dir,mot,dico,main)



#partie 6
#6.1.1
def tour_joueur(joueur,pm):
    print(joueur,"C'est votre tour !")
    print("Voici votre main : ", dico_joueurs[joueur]['main_joueur'])
    print("Votre nombre de jetons dans le sac est de ",len(sac))
    print("Vous avez un score de : ", dico_joueurs[joueur]['point'])
    affichage_jetons(J)
    x=''
    while x != 'a' and x != 'b' and x != 'c':
        texte = joueur + " Que voulez vous faire (choississez la lettre) ? a.passer b.echanger c. placer  "
        x=input(texte)
    if x=='b':
        liste_echange = []
        echange = input("Quel jeton voulez vous échanger ? ")
        rejouer = input("Encore un jeton ? (oui /non)")
        liste_echange.append(echange)
        while (rejouer == 'oui'):
            echange = input("Quel jeton voulez vous échanger ? ")
            rejouer = input("Voulez_vous échanger d'autres jetons (oui/non)? ")            
            liste_echange.append(echange)  
        echange_ok=echanger(liste_echange,dico_joueurs[joueur]['main_joueur'],sac)
        if echange_ok==True:
            print(" Votre nouvelle main est : ",dico_joueurs[joueur]['main_joueur'])
            return True
        else:
            print("Impossible !")
            return False
    elif x=='c':
        mot_joueur = input("Veuillez saisir le mot que vous voulez jouer ? ")
        ligne = int(input("Dans quelle ligne voulez-vous placer votre mot (entre 0 et 14) ? "))
        colonne = int(input("Dans quelle colonne voulez-vous placer votre mot (entre 0 et 14) ? "))
        dir = input(" Dans quelle direction voulez vous jouer (h / v) ? ")
        if pm == True and (ligne!=7 or colonne!=7):
            print("Attention ! Le premier mot doit être joué en [7,7]")
            return False
        if len(dic2)>0:
            if mot_joueur not in dic2:
                print("Vous ne pouvez pas jouer ce mot!")
                return False 
        mot_place=placer_mot(plateau,dico_joueurs[joueur]['main_joueur'],mot_joueur,ligne,colonne,dir)
        if mot_place == False:
            print("Vous ne pouvez pas placer ce mot à cette place !")
            return False
        else:
            valeur=calcul_valeur(plateau,ligne,colonne,dir,mot_joueur,dico,dico_joueurs[joueur]['main_joueur'])
            dico_joueurs[joueur]['point']=dico_joueurs[joueur]['point']+valeur
            print("Votre mot vaut ", valeur," points. Maintenant votre score est de ",dico_joueurs[joueur]['point']," points.")
            return True
    else:
        print(joueur," Vous passez votre tour !")
        return True






#6.1.2
def fin_partie(sac,main,joueur):
    if 7-len(main)>len(sac) :
        print("Fin de la partie")
        return True
    else:
        completer_main(dico_joueurs[joueur]['main_joueur'],sac)
        return False



#6.1.3
#La fonction prochain_joueur détecte un changement de joueur.
def prochain_joueur(nbj, pos, dj):
    pos = (pos + 1) % nbj
    for nom in dj:
        if dj[nom]['position']==pos:
            return nom, pos

        
print("LA PARTIE DE SCRABBLE COMMENCE")
dico_joueurs={}
dico=init_dico()
sac=init_pioche(dico)
plateau=init_jetons()
bonus=init_bonus()
affichage_jetons(J)
premier_mot = True


import os
dic1=input("Souhaitez-vous utiliser un fichier qui contient les mots autorisés oui/non ?")
while dic1 !='oui' and dic1 !='non':
    dic1=input("Souhaitez-vous utiliser un fichier qui contient les mots autorisés oui/non ?")
if dic1 == 'oui':
    fichier=input("Veuillez entrez le nom du dictionnaire : ")
    if os.path.isfile(fichier):
        dic2=generer_dico(fichier)
        nbmotautorisés=len(dic2)
        print("Dans votre dictionnaire, il y a  ",str(nbmotautorisés)," mots.")
    else:
        dic2=[]
        print("Nom incorrect ")
else:
    dic2=[]



#La première partie du programme principal sert à initialiser le jeu : l’ordinateur demande à l’utilisateur d’entrer un nombre de joueurs, leur nom, crée la pioche, affiche le
#plateau et crée un dictionnaire qui contient le nom de chaque joueur. On nomme ici 6.2.1


nb_joueur=int(input("Entrer le nombre de joueurs : "))

for e in range(nb_joueur):
    texte = " Quel est le prenom du joueur" + str(e+1)
    prenom=input(texte)
    main=piocher(7,sac)
    dico_joueurs[prenom]=dict(point=0,main_joueur=main,position=e)






#6.2.2
position_joueur = -1
partie_finie = False
while partie_finie == False:
    joueur,position_joueur=prochain_joueur(nb_joueur, position_joueur, dico_joueurs)
    joueur_ok = False
    while joueur_ok == False:
        joueur_ok = tour_joueur(joueur,premier_mot)
        premier_mot=False
    if len(dico_joueurs[joueur]['main_joueur']) == 0:
        dico_joueurs[joueur]['point']=dico_joueurs[joueur]['point'] + 50
        print("Super, vous avez fait un scrabble!!!")
    partie_finie = fin_partie(sac,dico_joueurs[joueur]['main_joueur'],joueur)



meilleur=None
for joueur in dico_joueurs:
    mot=dico_joueurs[joueur]['main_joueur']
    malus=valeur_mot(mot,dico)
    dico_joueurs[joueur]['point']=dico_joueurs[joueur]['point']-malus
    print(joueur," votre score est de ",dico_joueurs[joueur]['point']," points")
    if meilleur == None:
        meilleur=dico_joueurs[joueur]['point']
        pers=joueur        
    elif meilleur < dico_joueurs[joueur]['point']:
        meilleur=dico_joueurs[joueur]['point']
        pers=joueur
print('Bravo, Le gagnant est ', pers, ' avec un score de ', meilleur)
print("C'est la fin de cette partie, merci!")
        





