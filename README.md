# Scrabble-Demo

Scrabble est un jeu de mots populaire qui met les joueurs au défi de créer des mots à l'aide de tuiles de lettres et de les placer stratégiquement sur un plateau de jeu. Ce code Python implémente la logique de jeu du Scrabble, permettant aux joueurs de jouer les uns contre les autres ou contre l'ordinateur.


________________________________________________________________________________________________________________________________________________________________
# Guide
1. Utiliser n'importe quel outil qui peut exécuter python
2. Placer le fichier "motscrabble.txt" dans le dossier contenant le fichier de code du projet avant de lancer le programme
3. Jouez selon les instructions de la ligne de commande et suivez les règles que le jeu avait s'il était sorti avant


________________________________________________________________________________________________________________________________________________________________
#  Explication les parties dans le programme

- Partie 1:	Le Scrabble se joue sur un plateau de 15x15 cases. On repr´esente le plateau de jeu par des listes de listes (une liste de
cellules pour chaque ligne du plateau):
	- Une liste bonus (liste de listes de chaˆınes de caract`eres) contient les bonus des cases, tels qu’indiqu´es sur l’image 1. La valeur ”MT” (cases rouges) indique un ”mot compte triple”, la valeur ”MD” (cases oranges, y compris la case centrale) un mot compte double (un mot passant par cette case compte pour respectivement le double ou le triple de sa valeur); la valeur ”LT” (cases bleu foncé) une lettre compte triple, la valeur ”LD” (cases bleu clair) une lettre compte double (la lettre pos´ee sur cette case compte pour respectivement 2 ou 3 fois sa valeur). Les cellules sans bonus (cases vertes) contiennent une chaˆıne vide.
	- Une autre liste jetons (liste de listes de caract`eres) qui indique les positions des jetons lettres dẹà joués sur ce plateau. Chaque cellule contient le caractère du jeton posé sur cette case, ou bien une chaîne vide si la case est vide.

- Partie 2:	La pioche contient des jetons pour les lettres de l’alphabet, chaque lettre étant présente en un certain nombre d’exemplaires, et valant un certain nombre de points. On pourra se référer à "https://www.regles-de-jeux.com/regle-du-scrabble/" pour les nombres de jetons et les valeurs de chaque lettre. Les jetons sont repr´esent´es ici par des lettres majuscules de l’alphabet. La pioche contient aussi 2 jokers, valant 0 point, qu’on représentera par le caractère ”?”.

- Partie 3:	Les joueurs doivent construire des mots avec les lettres de leur main pour les poser sur le plateau. Ils ont le droit d’utiliser les lettres déjà posées (sans les déplacer) pour construire leurs mots. Mais pour commencer simple, on va chercher des mots jouables uniquement avec les jetons de la main du joueur. Pour vérifier qu’un mot est autorisé, on se basera sur une liste exhaustive de tous les mots qu’on lira dans un fichier. Ces mots seront tous en lettres majuscules non accentuées.

- Partie 4:	On veut maintenant calculer la valeur des mots posés. Chaque jeton a une valeur en points (entre 0 pour les jokers, et 10 pour les lettres les plus rares). Pour simplifier on commencera par calculer la valeur des mots indépendamment de leur placement (donc des ´eventuelles cases bonus). On trouvera la valeur de chaque jeton dans un dictionnaire reçu en argument, au format généré par la fonction init dico(). Si un joueur place ses 7 lettres d’un coup, c’est un Scrabble, il re¸coit un bonus de 50 points en plus de la valeur du mot.

- Partie 5:	Les joueurs peuvent placer leurs mots sur la grille, horizontalement ou verticalement, au contact des mots déjà posés. On s’intéresse ici à la vérification du placement des mots sur le plateau de jeu.

- Partie 6:	On va maintenant écrire le programme principal de jeu à plusieurs joueurs. Chaque joueur est identifié par son nom, dispose d’une liste (sa ”main”) de 7 jetons, et d’un score. On pourra stocker toutes ces informations dans un dictionnaire. On pourra aussi stocker un numéro d’ordre de jeu. Les joueurs jouent à tour de rôle : soit il passe; soit il échange un certain nombre de jetons; soit il place un mot, marque les points correspondants, et re-pioche les jetons manquants. Si un joueur doit piocher mais qu’il ne reste plus assez de jetons dans le sac, alors la partie se termine imm´ediatement. Les autres joueurs perdent un nombre de points égal à la somme des valeurs des jetons qu’ils ont encore en main.
